# -*- coding:utf-8 -*-
import os, time, re
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import platform

__settings: Dict = None
__chrome_driver = None
__page_pattern = "<b>Found: ([0-9,]{1,10}) Places, ([0-9,]{1,10}) Pages</b>"
__p_xpath = '//div[@class="six columns"]/p'


def start_crawl(**settings) -> None:
    print("start crawl data ......")
    __settings = settings
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    placemap_url = "https://placesmap.net/"
    driver_path = "chromedriver.exe"
    if platform.system() == "Darwin":
        driver_path = "/Users/Nick/Dev/Python-In-Action/placemap/chromedriver"
    __chrome_driver = webdriver.Chrome(executable_path=driver_path,
                                       options=chrome_options)
    __chrome_driver.set_page_load_timeout(30)
    __chrome_driver.get(placemap_url)
    country_name = __settings["COUNTRY_NAME"]
    href = __parse_country_href(__chrome_driver, country_name)
    print(f"提取{country_name}信息链接地址:{href}")
    for city_name in __settings["CITY_LIST"]:
        city_href = __build_city_href(href, city_name)
        print(f"提取{city_name}信息链接地址:{city_href}")
        __chrome_driver.get(city_href)
        for pattern in __settings["MATCHES"]:
            target_href = str(pattern).lower().replace(" ", "-")
            if pattern not in __chrome_driver.page_source:
                print(f"没有找到目标链接:{pattern}")
                continue
            target_href = city_href + target_href
            print(f"目标信息链接:{target_href}")
            __chrome_driver.get(target_href)
            match = re.search(__page_pattern, __chrome_driver.page_source)
            if match == None:
                continue
            page_size = int(match.group(2))
            print(f"page size: {page_size}")
            for page_num in range(1, page_size + 1):
                page_href = target_href + f"/{page_num}/"
                print(f"页面链接:{page_href}")
                __chrome_driver.get(page_href)
                p_el_list: List[
                    WebElement] = __chrome_driver.find_elements_by_xpath(
                        __p_xpath)
                for p_el in p_el_list:
                    if str(p_el.text).strip() == '':
                        continue
                    title = p_el.find_element_by_xpath("./b/a").text
                    cordinate = p_el.find_element_by_xpath("./a").text
                    detail_list = str(p_el.text).split("\n")
                    address = detail_list[1]
                    detail = detail_list[3] if len(detail_list) == 4 else None
                    print(f"""
                    {title}
                    {address}
                    {cordinate}
                    {detail}
                    """)


def __parse_country_href(chrome_driver, country_name) -> str:
    all_country_el_list: List[
        WebElement] = chrome_driver.find_elements_by_tag_name("a")
    country_el_list: List[WebElement] = list(
        filter(lambda a: a.text == country_name, all_country_el_list))
    if len(country_el_list) == 0:
        raise ValueError(f"没有找到该国家链接信息: {country_name}")
    country_el = country_el_list[0]
    return country_el.get_attribute("href")


def __build_city_href(href, city_name) -> str:
    f_city_name = city_name.replace(" ", "-")
    city_href = f"{href}{f_city_name}/"
    return city_href
