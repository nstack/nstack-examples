#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.GetMoviePoster Service
"""
import tempfile
import os
from imdbpie import Imdb
import wget

import nstack

class Service(nstack.BaseService):
    def __init__(self):
        self.imdb = Imdb()
        # self.imdb = Imdb(anonymize=True) # to proxy requests

    # (Title, Category, Score) -> (Title, Category, Score, Image)
    def getMoviePoster(self, msg):
        title, category, rating = msg
        x = self.imdb.search_for_title(title)[0]['imdb_id']
        y = self.imdb.get_title_by_id(x)

        tmp_file_name = tempfile.mktemp(suffix=".tmp")
        wget.download(y.poster_url, out=tmp_file_name, bar=None)
        with open(tmp_file_name, "rb") as f:
            poster_data = f.read()
            with open("./img_orig_saved.jpg", "wb") as g:
              g.write(poster_data)

        os.remove(tmp_file_name)

        return (title, category, rating, poster_data)

