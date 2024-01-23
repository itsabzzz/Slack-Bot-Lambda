# Slack  Bot

## Overview

Slack Joke Bot is a simple bot designed to bring humor to your Slack channels. The bot responds with a joke when called through a specified command. The project is hosted on AWS Lambda, providing a serverless and scalable solution.

## How to Use

To get a joke from the Slack Joke Bot, use the following command /telljoke in any Slack channel where the bot is present:

![image](https://github.com/itsabzzz/Slack-Bot-Lambda/assets/61920580/c550d291-0400-4247-82a0-ba1614da9481)

The bot will respond with a lighthearted joke to brighten up your day.

## AWS Lambda Setup

The Slack Joke Bot is hosted on AWS Lambda, taking advantage of serverless architecture for cost-effectiveness and ease of deployment. Below are key details about the Lambda function setup:

- **Function Name:** project_jokes_bot
- **Runtime:** Python 3.12
- **Permissions:**
  - AWS Lambda Execution Role with necessary permissions.

## Dependencies

The project relies on the following dependencies:

- [slack_sdk](https://github.com/slackapi/python-slack-sdk): Python Slack SDK for interacting with the Slack API.

## Code Structure

The code is organized into the following structure:

![image](https://github.com/itsabzzz/Slack-Bot-Lambda/assets/61920580/6afc97a3-827c-4317-bb7b-5ce90672cb4e)
