import requests
import logging
from datetime import datetime as dt
#from Util import Response

log = logging.getLogger()
log.setLevel(logging.INFO)

api_url = 'https://qcp3xrmpmj.execute-api.us-east-1.amazonaws.com/dev/'

def cognitoUserToRDS(event, context):
    # Create RDS Entry
    cognitoRdsUserEndpoint = 'cognitoUserToRDS'
    rds_url = api_url + cognitoRdsUserEndpoint
    datestamp = dt.now().strftime('%Y-%m-%dT%H:%M:%S')
    payload = {"email": event["request"]["userAttributes"]["email"],
     "email_verified": event["request"]["userAttributes"]["email_verified"],
     "datestamp": datestamp,
      "userPoolId":event["userPoolId"],
      "userName": event["userName"]}
    r = requests.post(url=rds_url, data=payload)

    cognitoS3UserEndpoint = 'createCognitoUserKey'
    s3_url = api_url + cognitoS3UserEndpoint
    r = requests.post(url=s3_url, data=payload)

    return event
