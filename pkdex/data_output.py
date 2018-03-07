# /usr/bin/env python3
# -*- coding: utf-8 -*-


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        import json
        with open('pokedex.json', 'w+') as f:
            json.dump(data, f, indent=4)
