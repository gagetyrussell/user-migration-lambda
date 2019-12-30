import requests
import logging
#from Util import Response

log = logging.getLogger()
log.setLevel(logging.INFO)

api_url = 'https://qcp3xrmpmj.execute-api.us-east-1.amazonaws.com/dev/'

def cognitoUserToRDS(event, context):
    endpoint = 'cognitoUserToRDS'
    url = api_url + endpoint
    payload = {"email": event["request"]["userAttributes"]["email"],
     "email_verified": event["request"]["userAttributes"]["email_verified"],
      "userPoolId":event["userPoolId"]}
    r = requests.post(url=url, data=payload)
    return event
