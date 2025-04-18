import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        text = body['text']

        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
        sentiment_score = response['SentimentScore']

        return {
            'statusCode': 200,
            'body': json.dumps({
                'sentiment': sentiment,
                'scores': sentiment_score,
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    console.log("Response body:", JSON.stringify({
  sentiment: sentiment,
  scores: sentimentResult.SentimentScore,
}));