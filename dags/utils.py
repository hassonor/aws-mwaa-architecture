import json

import boto3

import logging

logger = logging.getLogger(__name__)


def get_secrets(secret_name, region_name='us-east-1'):
    """Retrieve secrets from AWS secret Manager"""
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.load(response['SecretString'])
    except Exception as e:
        logger.error(f"Secret retrieval error: {e}")
        raise
