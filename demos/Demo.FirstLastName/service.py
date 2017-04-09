#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nstack

class Service(nstack.BaseService):
    def full_name(self, second_name):
        """This method demonstrates environment configuration""""
        full_name = "{} {}".format(self.args.get("first_name", "Tux"), second_name)
        return full_name

