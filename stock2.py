import datetime
import json
import random
import boto3

# Send to a second stream to mimic data join
STREAM_NAME = "ShimingExampleInputStream2"


def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'name': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'grade': random.random()}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis'))
