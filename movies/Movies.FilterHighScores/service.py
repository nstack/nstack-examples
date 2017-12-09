#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movies.FilterHighScores Service
"""
import nstack

class Module(nstack.Module):
    # (Title, Score) -> [(Title, Score)]
    def filterHighScores(self, msg):
        (title, score) = msg
        if score >= float(self.args.get('score', '8')): 
            # we only want good films :)
            return [msg]
        else:
            return []

