# db.py

import os
import mysql.connector

from .aws import get_secret_json

def get_db():
    db_hostname = os.environ.get('DB_HOSTNAME', 'localhost')
    db_username = os.environ.get('DB_USERNAME', 'admin')
    db_password = os.environ.get('DB_PASSWORD', 'admin')
    db_database = os.environ.get('DB_DATABASE', 'application')

    if 'SECRET_NAME' in os.environ:
        secret_name = os.environ['SECRET_NAME']
        aws_region = os.environ.get('AWS_REGION', 'us-east-1')
        db_secret = get_secret_json(secret_name, aws_region)
        db_username = db_secret['username']
        db_password = db_secret['password']

    db = mysql.connector.connect(
        host=db_hostname,
        user=db_username,
        password=db_password,
        database=db_database
    )

    return db
