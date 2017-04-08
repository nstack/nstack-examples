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
    # make sure call the superclass to initialise correctly
    super().__init__()
    self.random_funcs = [mk_gotham, mk_kelvin, mk_lomo, mk_nashville, mk_toaster]
    self.counter = 0

  # MovieRecordImage = (Text, Integer, ByteString) -> (Text, ByteString)
  def _processImage(self, processor, msg):
    title, rating, in_poster_data = msg

    # save bytestring to disk
    tmp_file_name = tempfile.mktemp(suffix=".jpg")
    with open(tmp_file_name, "wb") as f:
      f.write(bytearray(in_poster_data))

    # apply filter
    processor(tmp_file_name)

    # load modified file as bytestring
    with open(tmp_file_name, "rb") as f:
      out_poster_data = f.read()
    os.remove(tmp_file_name)

    return (title, out_poster_data)

  def applyFilter(self, msg):
    filters = {
      'gotham' : mk_gotham,
      'kelvin' : mk_kelvin,
      'lomo' : mk_lomo,
      'nashville' : mk_nashville,
      'toaster' : mk_toaster,
      'random' : random.choice(self.random_funcs)      
    }
    
    filter_name = self.args.get('filtertype', 'gotham')
    print("Applying filter {}".format(filter_name))
    return self._processImage(filters.get(filter_name), msg)

