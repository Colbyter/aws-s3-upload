import json
import urllib, urllib2
import os
import boto3
import random
from datetime import datetime

# Let's use Amazon S3
s3 = boto3.client(
    's3',
    # Hard coded strings as credentials, but not recommended.
    aws_access_key_id ='AWS_ACCESS_KEY',
    aws_secret_access_key ='AWS_SECRET_KEY'
)


def lambda_handler(event, context):
    print 'inside the handler'
    print 'incoming payload', event
    with open("/tmp/json.txt","w+") as filetest:
        json.dump(event, filetest)
    
    with open("/tmp/json.txt", "rb") as f:
        s3.upload_fileobj(f, "transcription-s3", "cdr_test_{0}.txt".format(datetime.utcnow()))
    
    os.remove("/tmp/json.txt")
    return 'ok'
    #raise Exception('Something went wrong')
   
   
