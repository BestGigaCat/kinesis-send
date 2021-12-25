import json
import boto3

STREAM_NAME = "ShimingExampleInputStream"

def show(stream_name, kinesis_client):
    kinesis_client.get_
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey="partitionkey")


if __name__ == '__main__':
    show(STREAM_NAME, boto3.client('kinesis'))
