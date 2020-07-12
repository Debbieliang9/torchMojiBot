# Deploying the model on Sagemaker

The first step is to build a docker image that runs our [web server](https://github.com/cw75/torchMojiBot/blob/master/sagemaker/emojibot-sagemaker.py) that responds to Sagemaker's health check (ping) requests and also serves prediction requests.

Before building the image, we need two files for model initialization: `vocabulary.json` for sentence tokenization and `pytorch_model.bin` that stores pre-trained model weights.
`vocabulary.json` is already in the repo here `torchMojiBot/sagemaker/model/vocabulary.json`. To download `pytorch_model.bin`, simply run `python3 scripts/download_weights.py` from the `torchMojiBot/sagemaker` directory. The weights will be downloaded to `torchMojiBot/sagemaker/model/pytorch_model.bin`

Then, go to AWS [ECR console](https://console.aws.amazon.com/ecr) and create a new repository by hitting the "Create repository" button.
Click the repository name, and click "View push commands" to see necessary steps to [authenticate](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth), build and push the docker image to ECR.
In our case, to build the image, run `docker build . -f emojibot-sagemaker.dockerfile -t <Your ECR URI>`.
And push by `docker push <Your ECR URI>`.

Next, create a Sagemaker model:
1. Click the "Models" tab on the [Sagemaker console](https://console.aws.amazon.com/sagemaker/) and click "Create model".
2. Create a name for the model.
3. In container definition, choose "Provide model artifacts and inference image location" and paste the ECR URI into "Location of inference code image".
4. Click "Create model".

We then create an endpoint configuration:
1. Click the "Endpoint configurations" tab and click "Create endpoint configuration".
2. Create a name for the endpoint configuration.
3. Click "Add model" and select the model we just created.
4. Click "Create endpoint configuration".

Finally, create a Sagemaker endpoint:
1. Click the "Endpoints" tab and click "Create endpoint".
2. Create a name for the endpoint.
3. Select "Use an existing endpoint configuration" and choose the endpoint configuration that we just created.
4. Click "Create endpoint".

The above steps can also be accomplished via the [Sagemaker API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html).
