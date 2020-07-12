# torchMojiBot

This repo contains the code and detailed instruction behind this blog post (TODO: add link), which describes my experience deploying the torchMoji model on [Sagemaker](https://aws.amazon.com/sagemaker/) and [Algorithmia](https://algorithmia.com/), and serving prediction to a Slack bot that automatically reacts to Slack messages with emoji.

For Sagemaker deployment, see [here](https://github.com/cw75/torchMojiBot/tree/master/sagemaker). For Algorithmia deployment, see [here](https://github.com/cw75/torchMojiBot/tree/master/algorithmia).

The repo also contains the [code and instruction](https://github.com/cw75/torchMojiBot/tree/master/lambda) for deploying the AWS Lambda function that performs request authorization and routes traffic between Slack and the prediction service.
