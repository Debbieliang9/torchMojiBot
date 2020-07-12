# Authentication and message routing with AWS Lambda

This directory contains the code for the AWS Lambda function that:
1. Accepts and responds to the [URL verification](https://api.slack.com/events/url_verification) request from Slack.
2. Authenticates the Slack subscription message, extracts the text and sends it to our prediction service (Sagemaker or Algorithmia).
3. Receives the prediction response (emoji) and uses the Slack web client to post the emoji reaction to Slack workspace.

The `package` folder contains all the Python dependencies required by `lambda_function.py`.

Before uploading to AWS Lambda, you need to replace the credential placeholders in `lambda_function.py` with yours.

If you deployed the model with Sagemaker, in `sagemaker/lambda_function.py`, provide your Slack bot user's OAuth access token and Slack app's signing secret (lines 12 and 14).

If you deployed the model with Algorithmia, in `algorithmia/lambda_function.py`, in addition to the Slack credentials, provide your Algorithmia API token and path to your deployed model (lines 17 and 19).

Run `cd package && zip -r9 ${OLDPWD}/function.zip . && cd ${OLDPWD}`.

If you deployed the model with Sagemaker, run `cd sagemaker && zip -g ${OLDPWD}/function.zip lambda_function.py && cd ${OLDPWD}`.

If you deployed the model with Algorithmia, run `cd algorithmia && zip -g ${OLDPWD}/function.zip lambda_function.py && cd ${OLDPWD}`.

On the AWS Lambda console,
1. Click "Create function".
2. Name the function "emojize".
3. Select Python3.6 as Runtime.
4. If you deployed the model with Sagemaker, create an IAM role with the `sagemaker:InvokeEndpoint` policy and assign it to the function.
5. Click "Create function".

Install and configure [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

Finally, upload the zip file to AWS Lambda by running `aws lambda update-function-code --function-name emojize --zip-file fileb://function.zip`.