#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json

import nstack

fruits = set(['apple', 'orange', 'banana'])
vegetables = set(['cabbage', 'carrot', 'potato'])
chaps = set(['leo', 'rafe', 'roman', 'mandeep', 'ed', 'nick'])

def class_of(s):
    if s in fruits:
        return "fruit"
    if s in vegetables:
        return "vegetable"
    if s in chaps:
        return "chap"

class Service(nstack.BaseService):
    def __init__(self):
        super().__init__()
        # Demo.Retry
        self.fail = True

    # Demo.NumChars
    def numChars(self, msg):
        return len(msg)

    # Demo.Classify
    def classify(self, x):
        return "{} is a {}".format(x, class_of(x.lower()))

    # Demo.DigitString
    def digitString (self, xs):
        return (self._transform(x) for x in xs)
    
    def _transform(self, x):
        time.sleep(5) # TODO: Work out how to make this more efficient
        return str(x)

    # Demo.FirstLastName
    def full_name(self, second_name):
        """This method demonstrates environment configuration"""
        full_name = "{} {}".format(self.args.get("first_name", "Tux"), second_name)
        return full_name

    # Demo.Json
    def extract_field(self, x):
        field_name = x[0]
        j = json.loads(x[1])
        return(j[field_name])

    # Demo.Retry
    def faulty_id(self, x):
        if self.fail:
            self.fail = False
            raise RuntimeError("not this time")
        else:
            return x

    # Demo.Sink
    def mylog(self, x):
        print(x)


