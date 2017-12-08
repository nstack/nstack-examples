#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo.Json:0.0.1-SNAPSHOT Service
"""
import nstack
import json

class Module(nstack.Module):
    def extract_field(self, x):
        field_name = x[0]
        j = json.loads(x[1])
        return(j[field_name])
