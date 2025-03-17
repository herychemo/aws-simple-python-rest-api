# aws.py

import boto3
import base64
import json

def get_secret_value(secret_name, aws_region):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=aws_region)

    secret_response = client.get_secret_value(SecretId=secret_name)
    if 'SecretString' in secret_response:
        return secret_response['SecretString']
    else:
        binary_secret = secret_response['SecretBinary']
        return base64.b64encode(binary_secret)

def get_secret_json(secret_name, aws_region):
    secret_str = get_secret_value(secret_name, aws_region)
    return json.loads(secret_str)
