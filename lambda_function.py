import json
import urllib.request
import os
import random

def lambda_handler(event, context):
    jokes =["What do you call a pile of cats? A meow-ntain.", "RIP, boiling water.You will be mist.","What do you call an angry carrot? A steamed veggie.", 
    "I ordered a chicken and an egg online. I’ll let you know what comes first." ]
    
    ajoke = random.choice(jokes)
    
    message = {
        "text": ajoke
    }
    hdr = {'Content-Type': 'application/json; charset=utf-8'}
    req = urllib.request.Request(os.environ["MY_WEBHOOK"], json.dumps(message).encode('utf-8'), hdr)
    response = urllib.request.urlopen(req)
    response.read()
    
    return {
        'statusCode': 200,
    }

