# /usr/bin/env python3
# -*- coding: utf-8 -*-
from pkdex.data_output import DataOutput
from pkdex.html_downloader import HtmlDownloader
from pkdex.html_parser import HtmlParser
from pkdex.url_manager import UrlManager


class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                poke_info = self.parser.parse_index(html)
                self.output.store_data(poke_info)
            except Exception as e:
                print('Ooooops! some errors occured when crawling.')

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('http://www.pokemon.name/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8')
