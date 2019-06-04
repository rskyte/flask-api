import os
import boto3
import pickle

class S3Logic:

    def __init__(self, client = None, bucket = None):
        self.bucket_name = 'flask-api-bucket'
        if bucket is not None:
            self.bucket = bucket
        else:
            self.bucket = boto3.resource('s3').Bucket(self.bucket_name)
        if client is not None:
            self.client = client
        else:  
            session = boto3.session.Session()
            self.client = session.client('s3',
                                    region_name='eu-west-2',
                                    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                    aws_secret_access_key=os.environ.get('AWS_SECRET_ID'))
    
    def put(self, data):
        serializedObject = pickle.dumps(data)
        response = self.client.put_object(Bucket=self.bucket_name,Key=data['userId'],Body=serializedObject)
        metadata = response['ResponseMetadata']
        return metadata['HTTPStatusCode']

    def get_all_user_ids(self):
        user_list = []
        for key in self.bucket.objects.all():
            if self.bucket.key and type(self.bucket.objects.all()) is dict:
                key = self.bucket.key()
            user_list.append(str(key.key))
        return user_list

s3 = S3Logic()
users = s3.get_all_user_ids()
print(users)
#thing = self.client.get_object(Bucket=self.bucket_name,Key=user_id)
#_thing = pickle.loads(thing['Body'].read())