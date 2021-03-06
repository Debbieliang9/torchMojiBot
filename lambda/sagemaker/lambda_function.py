import json

import hmac
import hashlib

from slack import WebClient
from slack.errors import SlackApiError

import boto3

# Replace xxx with your bot user's OAuth access token.
slack_web_client = WebClient(token='xxx')
# Replace xxx with your Slack app's signing secret.
signing_secret = 'xxx'

client = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    headers = event['headers']
    raw_data = event['body']
    payload = json.loads(raw_data)
    if 'challenge' in payload:
        # Respond to Slack's url verification request.
        return {
            'statusCode': 200,
            'body': json.dumps(payload['challenge'])
        }
    else:
        # First, perform authentication.
        request_timestamp = headers['X-Slack-Request-Timestamp']
        sig_basestring = 'v0:' + request_timestamp + ':' + raw_data
        my_signature = 'v0=' + hmac.new(signing_secret.encode(), sig_basestring.encode(), hashlib.sha256).hexdigest()
        slack_signature = headers['X-Slack-Signature']
        if hmac.compare_digest(my_signature, slack_signature):
            print('authorized!')
            event = payload['event']
            if event['type'] == 'message':
                channel_id = event['channel']
                ts = event['ts']
                text = event['text']
                # Send the text to our model deployed on SageMaker
                # and get the emoji response.
                response = client.invoke_endpoint(
                    EndpointName='emojibot', 
                    ContentType='text/plain',
                    Body=text.encode()
                    )
                emoji = response['Body'].read().decode()
                try:
                    # Add the emoji returned by our model to the text.
                    slack_web_client.reactions_add(channel=channel_id, name=emoji, timestamp=ts)
                except SlackApiError as e:
                    print(e.response)
        else:
            print('signature does not match!')

        return {
            'statusCode': 200,
            'body': json.dumps('')
        }