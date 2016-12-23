#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NStack.ImageFilters Service
"""
import tempfile
import random
import os
import nstack
from imaging import *

class Service(nstack.BaseService):
  def __init__(self):
    self.random_funcs = [mk_gotham, mk_kelvin, mk_lomo, mk_nashville, mk_toaster]
    self.counter = 0

  def _processImage(self, processor, msg):
    #  type MovieRecordImage = (Text, Text, Integer, ByteString)
    (title, category, rating, in_poster_data) = msg

    # tmp_file_name = tempfile.mktemp(suffix=".jpg")
    tmp_file_name = "output-{}.jpg".format(self.counter)
    self.counter += 1
    with open(tmp_file_name, "wb") as f:
      f.write(bytearray(in_poster_data))

    processor(tmp_file_name)

    with open(tmp_file_name, "rb") as f:
      out_poster_data = f.read()

    # os.remove(tmp_file_name)
    # return (title, category, rating, out_poster_data)
    return title # out_poster_data

  def random(self, msg):
    print("In imaging")
    fn = random.choice(self.random_funcs)
    x = self._processImage(fn, msg)
    print("Out imaging")
    return x

  def gotham(self, msg):
    return self._processImage(mk_gotham, msg)

  def kelvin(self, msg):
    return self._processImage(mk_kelvin, msg)

  def lomo(self, msg):
    return self._processImage(mk_lomo, msg)

  def nashville(self, msg):
    return self._processImage(mk_nashville, msg)

  def toaster(self, msg):
    return self._processImage(mk_toaster, msg)

