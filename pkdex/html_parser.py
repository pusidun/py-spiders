# /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_content):
        # TODO
        if page_url is None or html_content is None:
            return
        bs_obj = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(page_url, bs_obj)
        new_data = self._get_new_data(page_url, bs_obj)
        return new_urls, new_data

    def parse_index(self, html_content):
        '''
        :param html_content:
        :return: dict poke_info
                  title:pokemon name
                  href:pokemon detailed info
        '''
        if html_content is None:
            return
        poke_info = dict()
        bs_obj = BeautifulSoup(html_content, 'html.parser')
        for sp in bs_obj.findAll('span', class_='sprite sprite-pi'):
            a = sp.next_sibling.next_sibling
            title = a.get('title')
            href = a.get('href')
            poke_info[title] = href
        return poke_info

    def _get_new_urls(self, page_url, soup):
        pass

    def _get_new_data(self, page_url, soup):
        pass
