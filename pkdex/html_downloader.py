# /usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        header = {'User-Agent': user_agent}
        try:
            req = request.Request(url, headers=header)
            res = request.urlopen(req)
            return res.read().decode('utf-8')
        except Exception as e:
            print('fail to download')
