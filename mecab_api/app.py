import json
import os

import MeCab
tagger = MeCab.Tagger('-d{} -r/dev/null'.format(os.path.join(os.getcwd(), 'lib/mecab/dic/ipadic')))

def lambda_handler(event, context):
    """Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    query = event['queryStringParameters']
    if query is None or 'sentence' not in query:
        return {
            'statusCode': 422,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({'message': 'please add sentence query'})
        }

    node = tagger.parseToNode(query['sentence'])
    result = []
    while node:
        if node.surface:
            result.append({'surface': node.surface})
        node = node.next

    res_body = {
      'result': result
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(res_body)
    }
