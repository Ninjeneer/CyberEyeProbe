import boto3
import os
import json

from model import ScanResult
from mongo_saver import close_connection, save_object

sqs = boto3.client('sqs',
                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                   aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
                   )
queue_url = os.getenv('AWS_QUEUE_URL')

def send_message(scan_result: ScanResult) -> bool:
    saved_object_id = save_object(scan_result.__to_dict__())

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({
            "probeUid": os.getenv('PROBE_UID'),
            "objectId": saved_object_id
        })
    )

    close_connection()

    return True if response['MessageId'] else False
