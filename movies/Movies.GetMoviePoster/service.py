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

    # (Title, Score) -> (Title, Score, Image)
    def getMoviePoster(self, msg):
        title, rating = msg

        # get the movie title
        movie_id = self.imdb.search_for_title(title)[0]['imdb_id']
        movie_title = self.imdb.get_title_by_id(movie_id)

        # download the poster to a local temp file
        tmp_file_name = tempfile.mktemp(suffix=".tmp")
        wget.download(movie_title.poster_url, out=tmp_file_name, bar=None)

        # load into a bytearray and return it
        with open(tmp_file_name, "rb") as f:
            poster_data = f.read()

        os.remove(tmp_file_name)

        return (title, rating, poster_data)

