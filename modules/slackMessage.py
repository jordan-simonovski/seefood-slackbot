import requests
import json

def buildSlackMessage(imageUrl, hotdogAnswer):
    slackMessage = {
        "response_type": "in_channel",
        "attachments": [{
            "title": hotdogAnswer,
            "fallback": "This is going to rollback your deployment",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "image_url": imageUrl
        }]
    }

    return slackMessage

def notifySlackChannel(requestForm, hotdogAnswer):
    myMessage = buildSlackMessage(requestForm['text'], hotdogAnswer)
    return myMessage
    # webHookUrl = requestForm['response_url']
    # response = requests.post(webHookUrl, data=json.dumps(myMessage))
    # if response.status_code == 200:
        # return "ok"
    # return "there was an error getting a response from slack"