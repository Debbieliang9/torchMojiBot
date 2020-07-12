# torchMojiBot

This repo contains the code and detailed instruction to reproduce the intelligent Slack bot I built in this blog post (TODO: add link). Powered by the [torchMoji](https://github.com/cw75/torchMoji) model, the bot automatically reacts to Slack messages with emoji.

Overall, there are 5 steps:
1. Set up the Slack bot by completing steps 1-4 [here](https://github.com/cw75/torchMojiBot/tree/master/slack).
2. Deploy the torchMoji model on [Sagemaker](https://aws.amazon.com/sagemaker/) or [Algorithmia](https://algorithmia.com/) (or both!). See [here](https://github.com/cw75/torchMojiBot/tree/master/sagemaker) for Sagemaker deployment and [here](https://github.com/cw75/torchMojiBot/tree/master/algorithmia) for Algorithmia deployment.
3. Deploy the AWS Lambda function that performs request authorization and routes traffic between Slack and the prediction service. Instruction [here](https://github.com/cw75/torchMojiBot/tree/master/lambda).
4. Set up the API gateway that routes traffic to the Lambda function and exposes a REST endpoint to Slack. Instruction [here](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/) (Section: Create an API Gateway – Integration request setup).
5. Finish setting up the Slack bot by completing step 5 [here](https://github.com/cw75/torchMojiBot/tree/master/slack).

After completing all the steps above, send a direct message "this is great!" to your bot in the Slack workspace. You should see the following.

![Slack](https://github.com/cw75/torchMojiBot/blob/master/images/slack.png)

When you are done having fun, remember to delete all the AWS resources you created!
