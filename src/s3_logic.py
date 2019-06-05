import os
import boto3
import pickle

class S3Logic:

    def __init__(self, client = None, bucket = None):
        # Attempt at running local s3 bucket for local development
        # TODO finish
        #if os.environ.get('IS_OFFLINE'):
            #session = boto3.session.Session()
            #self.client = session.client('s3')
        #self.bucket_name = 'local-bucket'
        self.bucket_name = 'flask-api-bucket'
        if bucket is not None:
            self.bucket = bucket
        else:
            self.bucket = boto3.resource('s3').Bucket(self.bucket_name)

        if client is not None:
            self.client = client
        else:  
            self.client = boto3.client('s3')
    
    def put(self, data):
        serializedObject = pickle.dumps(data)
        response = self.client.put_object(Bucket=self.bucket_name,Key=data['userId'],Body=serializedObject)
        metadata = response['ResponseMetadata']
        return metadata['HTTPStatusCode']

    def get_all_user_ids(self):
        user_list = []
        for key in self.bucket.objects.all():
            if 'key' in self.bucket.__dict__.keys() and type(self.bucket.objects.all()) is dict:
                key = self.bucket.key()
            user_list.append(str(key.key))
        return user_list

# TODO get singular user route
#thing = self.client.get_object(Bucket=self.bucket_name,Key=user_id)
#_thing = pickle.loads(thing['Body'].read())