# -*- coding:utf-8 -*-
import os, time, re
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

__settings: Dict = None
__chrome_driver = None


def start_crawl(**settings) -> None:
    print("start crawl data ......")
    __settings = settings
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    placemap_url = "https://placesmap.net/"
    __chrome_driver = webdriver.Chrome(executable_path="chromedriver.exe",
                                       options=chrome_options)
    __chrome_driver.get(placemap_url)
    country_name = __settings["COUNTRY_NAME"]
    href = __parse_country_href(__chrome_driver, country_name)
    print(f"提取{country_name}信息链接地址:{href}")
    __chrome_driver.get(href)
    for city_name in __settings["CITY_LIST"]:
        __parse_city_href(__chrome_driver.page_source, city_name)
    # \s<a href=".*">Aba</a>


def __parse_country_href(chrome_driver, country_name) -> str:
    all_country_el_list: List[
        WebElement] = chrome_driver.find_elements_by_tag_name("a")
    country_el_list: List[WebElement] = list(
        filter(lambda a: a.text == country_name, all_country_el_list))
    if len(country_el_list) == 0:
        raise ValueError(f"没有找到该国家链接信息: {country_name}")
    country_el = country_el_list[0]
    return country_el.get_attribute("href")


def __parse_city_href(page_source, city_name) -> str:
    city_pattern = r"""\s<a href=\".*?\">%s</a>""" % city_name
    match = re.search(pattern=city_pattern, string=page_source)
    if match == None:
        print(f"没有找到指定城市信息: {city_name}")
    a_el = match.group(0)
    print(a_el)


#     chrome_driver.get(placemap_url)

# if __name__ == "__main__":
#     administration_areas = HUNGARY_CITY_LIST
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     placemap_url = "https://placesmap.net/"
#     chrome_driver = webdriver.Chrome(executable_path="chromedriver.exe",
#                                      options=chrome_options)
#     chrome_driver.get(placemap_url)
#     all_country_alist: List[
#         WebElement] = chrome_driver.find_elements_by_tag_name("a")
#     country_name = "Hungary"
#     country_alist: List[WebElement] = list(
#         filter(lambda a: a.text == country_name, all_country_alist))
#     if len(country_alist) == 0:
#         print("未找到国家信息")
#     country_el = country_alist[0]
#     country_href = country_el.get_attribute("href")
#     print(f"国家页面链接:{country_href}")
#     chrome_driver.get(country_href)

# for administration_area in administration_areas:
