from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )
import csv    
import datetime
        
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()        

class UserAccess(Base):
    __tablename__ = 'user_access'
    
    user_access_id = Column('user_access_id', INTEGER(), primary_key=True, nullable=False)
    access_datetime = Column('access_datetime', DATETIME(), nullable=False)
    ip_address = Column('ip_address', TEXT(), nullable=True)
    method = Column('method', TEXT(), nullable=False)
    url = Column('url', TEXT(), nullable=False)        
    query_string = Column('query_string', TEXT(), nullable=True)
    body = Column('body', TEXT(), nullable=True)

    def __init__(self, ip_address, method, url, query_string, body):
        self.access_datetime = datetime.datetime.now()
        self.ip_address = ip_address
        self.method = method
        self.url = url        
        self.query_string = query_string
        self.body = body
        
    def __str__(self):
        return self.method + ' - ' + self.url

