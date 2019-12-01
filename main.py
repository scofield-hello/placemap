# -*- coding:utf-8 -*-
import sys
from placemap import settings, spider

if __name__ == "__main__":
    try:
        config = settings.config
        spider.start_crawl(**config)
    except:
        print(sys.exc_info())