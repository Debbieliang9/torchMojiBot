# torchMojiBot

This repo contains the code and detailed instruction to reproduce the intelligent Slack bot I built in this blog post (TODO: add link). Powered by the [torchMoji](https://github.com/cw75/torchMoji) model, the bot automatically reacts to Slack messages with emoji.

Overall, there are 5 steps:
1. Create a Slack app [here](https://api.slack.com/apps/), link it to your workspace and grant permissions/subscriptions as outlined in my blog post (TODO: add link).
2. Deploy the torchMoji model on [Sagemaker](https://aws.amazon.com/sagemaker/) or [Algorithmia](https://algorithmia.com/) (or both!).
3. Deploy the AWS Lambda function that performs request authorization and routes traffic between Slack and the prediction service.
4. Set up an API gateway that routes traffic to the Lambda function and exposes a REST endpoint to Slack.
5. Paste the REST endpoint URL to the Slack bot's event subscription page.

For step 2, see [here](https://github.com/cw75/torchMojiBot/tree/master/sagemaker) for Sagemaker deployment and [here](https://github.com/cw75/torchMojiBot/tree/master/algorithmia) for Algorithmia deployment.

For step 3, see [here](https://github.com/cw75/torchMojiBot/tree/master/lambda).

For step 4, see [here](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/) (Section: Create an API Gateway – Integration request setup).
