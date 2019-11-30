# -*- coding:utf-8 -*-
import sys
from placemap.settings import countrys
from placemap import spider

if __name__ == "__main__":
    country_name = "Serbia"
    try:
        settings = countrys[country_name]
        spider.start_crawl(**settings)
    except:
        print(sys.exc_info())