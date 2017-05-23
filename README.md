# Seefood for Slack

## What is the purpose of this?
I got a bit bored last night and decided to replicate the functionality of Jian Yang's app from Silicon Valley using the AWS Rekognition API.

## What does it look like?

![wha if i to you thei is a app on the maket](http://i.imgur.com/xTeoBr2.jpg)


## See referenced clip here.

[![GODDAMMIT JIAN YANG](https://img.youtube.com/vi/FNyi3nAuLb0/0.jpg)](https://www.youtube.com/watch?v=FNyi3nAuLb0 "SeeFood App Demo")

## Prerequisites
1. AWS Account to host the Slackbot
2. AWS Account must have access to Regions where Rekognition is available (us-east-1, us-west-2, eu-west-1)

## Setup
```
cd seefood/
virtualenv env
source env/bin/activate

pip install -r requirements.txt
zappa deploy dev
```

## Setting up the Slash Command

1. Go to: <your slack domain>/apps/manage
2. Open slash commands.
3. Configure your new slash command in the following way.

![slash command](http://i.imgur.com/ox1EuIQ.png)
