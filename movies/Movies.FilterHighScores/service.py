#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.FilterHighScores Service
"""
import nstack

class Service(nstack.BaseService):
    # (Title, Category, Score) -> (Title, Category, Score)
    def filterHighScores(self, msg):
        print("In filterHighScores")
        (title, category, score) = msg
        if score >= 9: # we only want good films
            print("Out filterHighScores")
            return [msg]
        else:
            print("Out filterHighScores")
            return []

