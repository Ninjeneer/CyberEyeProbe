import boto3
import os
import json

from model import ScanResult

print(os.getenv('AWS_DEFAULT_REGION'))

s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                  aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
                  )

sqs = boto3.client('sqs',
                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                   aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
                   )
queue_url = os.getenv('AWS_QUEUE_URL')

def _save_object_to_s3(bucket_name: str, key: str, data: str):
    s3.put_object(Bucket=bucket_name, Key=key, Body=data)


def send_message(scan_result: ScanResult) -> bool:
    _save_object_to_s3(
        os.getenv('AWS_BUCKET_NAME'), 
        os.getenv('PROBE_UID'), 
        json.dumps(scan_result.__to_dict__())
    )

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=os.getenv('PROBE_UID')
    )
    return True if response['MessageId'] else False
