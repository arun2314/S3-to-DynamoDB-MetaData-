import json
import boto3
import urllib.parse

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')  # Replace with your table name

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_name = urllib.parse.unquote_plus(record['s3']['object']['key'])
        file_size = record['s3']['object']['size']

        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                'image_id': file_name,
                'bucket_name': bucket_name,
                'file_name': file_name,
                's3_url': s3_url,
                'size': file_size
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Metadata stored in DynamoDB!')
    }
