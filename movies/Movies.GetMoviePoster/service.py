#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.GetMoviePoster Service
"""
import tempfile
import os
from imdbpie import Imdb
import requests

import nstack

MAX_SIZE_KB = 512 # Max size of a poster to return

class Service(nstack.BaseService):
    def __init__(self):
        self.imdb = Imdb()
        # self.imdb = Imdb(anonymize=True) # to proxy requests

    # (Title, Score) -> [(Title, Image)]
    def getMoviePoster(self, msg):
        title, _ = msg

        # get the movie title
        movie_id = self.imdb.search_for_title(title)[0]['imdb_id']
        movie_title = self.imdb.get_title_by_id(movie_id)

        if movie_title.poster_url is not None:
          # download the poster into a bytearray
          r = requests.get(movie_title.poster_url)

          # filter content greater than MAX_SIZE_KB
          if len(r.content) <= MAX_SIZE_KB * 1000:
            return [('{}.jpg'.format(title), r.content)]

        return []

