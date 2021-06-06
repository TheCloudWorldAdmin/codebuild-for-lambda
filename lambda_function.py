
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('lambda deployment using CI CD.. Last work for today-- modified')
    }
