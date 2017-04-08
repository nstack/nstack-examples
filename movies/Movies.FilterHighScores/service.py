#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.FilterHighScores Service
"""
import nstack

class Service(nstack.BaseService):
    # (Title, Score) -> [(Title, Score)]
    def filterHighScores(self, msg):
        (title, score) = msg
        if score >= int(self.args.get('score', '9')): 
            # we only want good films :)
            return [msg]
        else:
            return []

