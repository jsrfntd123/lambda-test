import json


def hello(event, context):
    body = {
        "message": "Github Actions Test Final!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
