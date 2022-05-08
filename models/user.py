from uuid import uuid4; 
from datetime import datetime
from email.policy import default
from xmlrpc.client import DateTime
from sqlalchemy import Integer, Table,Column, String, DateTime
from config.db import meta
from sqlalchemy.sql import func

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(255)),
    Column('encrypted_password', String(255)),
    Column('api_key', String(255), default=str(uuid4())),
    Column('created_on', DateTime(timezone=True), default=func.now())
    )