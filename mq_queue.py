import boto3
import os
import json

from model import ScanResult
from mongo_saver import close_connection, save_object

sqs = boto3.client('sqs',
                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                   aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
                   )
queue_url = os.getenv('AWS_QUEUE_RESPONSE_URL')


def send_message(scan_result: ScanResult) -> bool:
    print("[SAVE] Saving results to database")
    saved_object_id = save_object(scan_result.__to_dict__())
    print("[SAVE] Saved results to database")


    print("[NOTIFICATION] Sending notification to SQS")
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({
            "probeId": os.getenv('PROBE_ID'),
            "objectId": saved_object_id
        })
    )
    print("[NOTIFICATION] Sent notification to SQS")

    close_connection()

    return True if response['MessageId'] else False
