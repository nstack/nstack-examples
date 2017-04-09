#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NStack.Utils:0.0.1-SNAPSHOT Service
"""
import io
import json
import uuid
import boto3

import nstack

class Service(nstack.BaseService):
  def __init__(self):
    # make sure call the superclass to initialise correctly
    super().__init__()

    # load AWS credentials from local file embedded wirhin service
    with open('./credentials.json', 'r') as f:
      creds = json.load(f)

    self.s3 = boto3.client('s3', aws_access_key_id=creds['S3_ACCESS_KEY'], aws_secret_access_key=creds['S3_SECRET_KEY'])

  def _upload(self, upload_name, data, content_type=None):
    upload_name = "{}/{}".format(self.args.get('directory', 'default'), upload_name)

    self.s3.upload_fileobj(data, 'uploads.demo.nstack.com', upload_name)

    upload_url = 'http://uploads.demo.nstack.com.s3.amazonaws.com/{}'.format(upload_name)
    print("Uploaded to {}".format(upload_url))
    return upload_url

  def uploadS3Uuid(self, data):
    """Upload object to S3, creating a unique name on demand"""
    content_type=self.args.get('content_type', 'application/octet-stream')
    return self._upload(uuid.uuid4(), io.BytesIO(data), content_type)

  def uploadS3File(self, msg):
    """Upload object to S3, using the given string as the object name"""
    title, data = msg
    return self._upload(title, io.BytesIO(data))

  def uploadTest(self, title):
    """Upload object to S3, using the given string as the object name"""
    f = open(title, 'rb')
    return self._upload(title, f)

