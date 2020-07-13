# Setting up the Slack bot

Before deploying the model, Lambda function, and setting up the API gateway:

1. [Create](https://slack.com/create) a Slack workspace for testing the bot.
2. Go to the Slack [app directory](https://api.slack.com/apps) and click “Create New App”.
3. Create a name for the app (bot) and link it to the test workspace.

![slack-create](https://github.com/cw75/torchMojiBot/blob/master/images/slack-create.png)

4. Go to the “OAuth & Permissions” tab and add `channels:history`, `im:history`, and `reactions:write` to the “Bot Token Scopes”.

![slack-auth](https://github.com/cw75/torchMojiBot/blob/master/images/slack-auth.png)

5. Click "Install App to Workspace".

After deploying the model, Lambda function, and setting up the API gateway:

6. On the “Event Subscriptions” tab, subscribe to bot events `message.channels` and `message.im` and paste the API gateway's REST endpoint URL to the "Request URL" box. You should see the green "Verified" with a checkmark, meaning Slack's [url verification](https://api.slack.com/events/url_verification) succeeded.

![slack-sub](https://github.com/cw75/torchMojiBot/blob/master/images/slack-sub.png)
