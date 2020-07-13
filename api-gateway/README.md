# Setting up the API Gateway

1. Go to the API Gateway [console](https://console.aws.amazon.com/apigateway) and click "Create API".
2. Click "Build" under "REST API", create a name for the API and click "Create API".
3. From the "Actions" drop-down list, click "Create Resource", enter "events" as the resource name and click "Create Resource".
4. Click `/events` in the "Resources" directory, from the "Actions" drop-down list, click "Create Method".
5. Select "POST" from the drop-down list and click the tick mark.
6. Choose "Lambda Function" as the integration type and specify the region and the name of your Lambda function.
7. **Important**: check "Use Lambda Proxy integration". This lets the API Gateway preserves the HTTP headers when forwarding the request. We need the information in the header to perform Slack's authentication.
8. Click "Save" and "OK".
9. From the "Actions" drop-down list, click "Deploy API". Select "New Stage" and name the stage "slack". Then click "Deploy".
10. Append "/events" to the "Invoke URL" (it should look like "https://xxx.amazonaws.com/slack/events") and paste it to the Slack bot event subscription page (see step 6 [here](https://github.com/cw75/torchMojiBot/tree/master/slack)).
