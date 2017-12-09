#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

class Module(nstack.Module):
    def classify(self, x):
        return "{} is a {}".format(x, class_of(x.lower()))

