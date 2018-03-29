from itty import *
import json 
import urllib , urllib2
import os
import boto3

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

# Let's use Amazon S3
s3 = boto3.client(
    's3',
    # Hard coded strings as credentials, but not recommended.
    aws_access_key_id ='YOUR_S3_ID',
    aws_secret_access_key ='YOUR_S3_KEY'
)


@post('/')
def index(request):
    response =  request.body
    headers = request.headers
    data = json.loads(response)
    print "incoming data", data
    with open("json.txt","w+") as filetest:
        json.dump(data, filetest)
     
    with open("json.txt", "rb") as f:
        s3.upload_fileobj(f, "YOUR_BUCKET_NAME_HERE", "cdr_test.txt")
    
    filepath = dname + "/json.txt"
    os.remove(filepath)
    
    return 'Ok'
    
run_itty(host=os.getenv('IP', '0.0.0.0') , port=int(os.getenv('PORT', 8888)))