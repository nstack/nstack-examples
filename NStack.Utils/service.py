#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NStack.Utils:0.0.1-SNAPSHOT Service
"""
import json
import uuid
import tinys3

import nstack

class Service(nstack.BaseService):
  def __init__(self):
    # make sure call the superclass to initialise correctly
    super().__init__()
    # load AWS credentials from local file embedded wirhin service
    with open('./credentials.json', 'r') as f:
      creds = json.load(f)

    self.conn = tinys3.Connection(creds['S3_ACCESS_KEY'], creds['S3_SECRET_KEY'])

  def _upload(output_name, data, content_type=None):
    output_name = "{}/{}".format(self.args.get('directory', 'default'), output_name)

    self.conn.upload(output_name, data, bucket='uploads.demo.nstack.com', expires='max', 
                     content_type=content_type)

    output_url = 'http://uploads.demo.nstack.com.amazonaws.com/{}'.format(output_name)
    print("Uploaded to {}".format(output_url))

    return output_url

  def uploadS3Uuid(self, data):
    """Upload object to S3, creating a unique name on demand"""
    content_type=self.args.get('content_type', 'application/octet-stream')
    return self._upload(uuid.uuid4(), data, content_type)

  def uploadS3File(self, msg):
    """Upload object to S3, using the given string as the object name"""
    title, data = msg
    return self._upload(title, data)

