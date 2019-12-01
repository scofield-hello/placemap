# -*- coding:utf-8 -*-
import os, time, re
from typing import List, Dict, NewType, Tuple, Optional
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import platform

Country = NewType("Country", Tuple[str, str])
Area = NewType("Area", Tuple[str, str])
Position = NewType("Position", Tuple[str, str, str, Optional[str],
                                     Optional[str]])
__chrome_driver: WebDriver = None
__page_pattern = "<b>Found: ([0-9,]{1,10}) Places, ([0-9,]{1,10}) Pages</b>"
__p_xpath = '//div[@class="six columns"]/p'
__phone_pattern = r"Phone:\s?([+0-9\s]{3,30})"
__web_pattern = r"\((.*?)\)"


def start_crawl(**settings) -> None:
    print("start crawl data ......")
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
    countrys: List[str] = settings["COUNTRY_LIST"]
    country_list: List[Country] = __parse_country_list(__chrome_driver,
                                                       countrys)
    for country in country_list:
        (country_name, country_href) = country
        print(f"国家[{country_name}]详情链接:{country_href}")
        __chrome_driver.get(country_href)
        area_list: List[Area] = __parse_area_list(__chrome_driver)
        for area in area_list:
            (area_name, area_href) = area
            print(f"国家[{country_name}] 地区[{area_name}]详情链接:{area_href}")
            __chrome_driver.get(area_href)
            for pattern in settings["MATCHES"]:
                target_href = str(pattern).lower().replace(" ", "-")
                if pattern not in __chrome_driver.page_source:
                    print(
                        f"国家[{country_name}] 地区[{area_name}]不存在[{pattern}]信息")
                    continue
                target_href = area_href + target_href
                print(f"地区[{area_name}]的[{pattern}]详情链接:{target_href}")
                __chrome_driver.get(target_href)
                match = re.search(__page_pattern, __chrome_driver.page_source)
                if match == None:
                    continue
                page_size = int(match.group(2))
                print(f"地区[{area_name}] 共有 [{pattern}] 信息 [{page_size}] 页 ")
                for page_num in range(1, page_size + 1):
                    page_href = target_href + f"/{page_num}/"
                    print(f"页面链接:{page_href}")
                    __chrome_driver.get(page_href)
                    p_el_list: List[
                        WebElement] = __chrome_driver.find_elements_by_xpath(
                            __p_xpath)
                    p_el_list = list(
                        filter(lambda el: str(el.text).strip() != '',
                               p_el_list))
                    for p_el in p_el_list:
                        title = p_el.find_element_by_xpath("./b/a").text
                        cordinate = p_el.find_element_by_xpath("./a").text
                        detail_list = str(p_el.text).split("\n")
                        address = detail_list[1]
                        detail = detail_list[3] if len(
                            detail_list) == 4 else ""
                        match_p = re.search(__phone_pattern, detail)
                        match_w = re.search(__web_pattern, detail)
                        phone = "" if not match_p else match_p.group(1).strip()
                        web = "" if not match_w else match_w.group(1).strip()
                        position: Position = (title, address, cordinate, phone,
                                              web)
                        print("\n".join(position))


def __parse_country_list(chrome_driver: WebDriver,
                         countrys: List[str]) -> List[Country]:
    all_country_el_list: List[
        WebElement] = chrome_driver.find_elements_by_tag_name("a")
    country_el_list: List[WebElement] = list(
        filter(lambda a: a.text in countrys, all_country_el_list))
    if len(country_el_list) == 0:
        raise ValueError(f"没有找到对应国家链接信息")
    country_list = list(
        map(lambda el: (el.text, el.get_attribute("href")), country_el_list))
    return country_list


def __parse_area_list(chrome_driver: WebDriver) -> List[Area]:
    area_el_list = chrome_driver.find_elements_by_xpath(
        '//div[@class="four columns"]/a')
    return list(
        map(lambda el: (el.text, el.get_attribute("href")), area_el_list))
