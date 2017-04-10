#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NStack.Utils:0.1.0 Service
"""
import io
import json
import mimetypes
import uuid
from urllib.parse import quote
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
    self.bucket = creds['BUCKET']

  def _upload(self, upload_name, data, content_type=None):
    upload_name = "{}/{}".format(self.args.get('directory', 'default'), upload_name)

    content_type = 'application/octet-stream' if content_type is None else content_type
    self.s3.upload_fileobj(data, self.bucket, upload_name, ExtraArgs={'ContentType': content_type})

    # generate the url (hardcoded to AWS us-east-1 atm)
    upload_url = quote('http://{}.s3.amazonaws.com/{}'.format(self.bucket, upload_name), safe=':/')
    print("Uploaded to {}".format(upload_url))
    return upload_url

  def uploadS3Uuid(self, data):
    """Upload object to S3, creating a unique name on demand"""
    return self._upload(uuid.uuid4(), io.BytesIO(data), self.args.get('content_type', None))

  def uploadS3File(self, msg):
    """Upload object to S3, using the given string as the object name"""
    title, data = msg
    return self._upload(title, io.BytesIO(data), mimetypes.guess_type(title)[0])

  def uploadTest(self, title):
    """Upload object to S3, using the given string as the object name"""
    f = open(title, 'rb')
    return self._upload(title, f, mimetypes.guess_type(title)[0])

  # NOTE - move to DSL
  def fst(self, msg):
    """Return the first element of a tuple"""
    return msg[0]

  # NOTE - move to DSL
  def snd(self, msg):
    """Return the second element of a tuple"""
    return msg[1]


