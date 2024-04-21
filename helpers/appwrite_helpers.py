from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.id import ID
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from appwrite.services.account import Account
from appwrite.services.users import Users
from appwrite.input_file import InputFile
import loguru 


logger = loguru.logger
client = Client()

ENDPOINT = 'https://appwrite.oacey.com:4443/v1'
PROJECT_ID = 'Accounts Receivables'
API_KEY = '__FILL__'

(client
  .set_endpoint(ENDPOINT) # Your API Endpoint
  .set_project(PROJECT_ID) # Your project ID
  .set_key(API_KEY) # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

database = Databases(client=client)
storage = Storage(client=client)
users = Users(client=client)
account = Account(client=client)
# initialize services 
# post entries for database 
class AppwriteDatabaseHandler(object):
    database_id: str
    collection_id: str
    
    def __init__(self, database_id, collection_id) -> None:
        self.database_id = database_id
        self.collection_id = collection_id
        
    def create_document(self, data, document_id=None, permissions=None):
        if document_id is None:
            document_id = ID.unique()
        # this is for creating a new document with unique or optional id
        logger.debug(document_id)
        response = database.create_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=document_id,
            permissions=permissions,
            data=data
        )
        logger.debug(response)
        return response
    
    def update_document(self, document_id:str, data , permissions=None):
        response = database.update_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=document_id,
            data=data,
            permissions=permissions,
        )
        
        logger.debug(response)
        return response
    
    def delete_document(self, document_id):
        response = database.delete_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=document_id
        )
        
        logger.debug(response)
        return response
    
    def list_documents(self, queries=None):
        response = database.list_documents(
            database_id=self.database_id,
            collection_id=self.collection_id,
            queries=queries
        )
        logger.debug(response)
        return response       
    

class AppwriteFileHandler(object):
    
    def __init__(self, bucket_id):
        self.bucket_id = bucket_id
    
    def upload_file(self, filepath, file_id, permissions=[]):
        input_file = InputFile.from_path(filepath)
        storage.create_file(
            bucket_id=self.bucket_id,
            file_id=file_id,
            file=input_file,
            permissions=permissions,
            
        )
        
        
        

from django.db import models
from django import forms
class AppwriteModelMixin(models.Model):
    appwrite_document_id = models.CharField(max_length=255, default='unique()', editable=False)
    
    class Meta:
        abstract = True

class AppwriteUserHandler(object):
    
    def create_user(self, data):
        response = users.create(
            user_id='unique()',
            email=data['email'],
            phone=data['phone'],
            password=data['password'],
            name=data['name'],
        )
        
        return response