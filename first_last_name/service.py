#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nstack
import os
import json

class Service(nstack.BaseService):
    def full_name(self, second_name):
        return self.args["first_name"] + " " + second_name
