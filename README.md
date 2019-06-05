## Flask API

A python api hosted on aws lambda built using the flask/serverless frameworks which persists data to an aws s3 bucket.
An AWSCodePipeline is setup to provide continuous testing/integration.

### Usage

API URL: https://3z6ahlrgci.execute-api.eu-west-2.amazonaws.com/dev

The following endpoints are exposed:
* /api/user/new -> create new user
* /api/user/all -> return list of all stored users

User data must be in JSON format and follow this schema:
```
{
    'userId': <your_user_id_here>
    'name': <your_name_here>
}
```

### Development

#### Prerequisites

AWS Account

Python 3.6^ - get the latest [here](https://www.python.org/downloads/)

Node - get the latest [here](https://nodejs.org/en/download/)

NPM:
```
$ npm install npm@latest -g
```

Serverless Framework:
```
$ npm install -g serverless
```

To setup serverless aws credentials: ([guide here](https://serverless.com/framework/docs/providers/aws/guide/credentials/))
```
$ serverless config credentials --provider aws --key <your_key_here> --secret <your_secret_here>
```

#### Setup Environment
clone the repo, then:
```
$ cd flask-api
$ npm install
$ pip install -r requirements.txt

```

#### Deploying to AWS Lambda
```
$ serverless deploy
```

#### Running Locally(but using aws bucket)
```
$ sls wsgi serve
```

#### Running Unit Tests
```
$ pytest -v
```

### Postman Results
Posting correctly formatted data to api running on AWS
![http post method](/img/pm_post_flaskapi.png)

Retrieving data:
![http get method](/img/pm_get_flaskapi.png)

### TODO
* More comprehensive error handling
* Dedicated release pipelines (dev, staging and production)
* Run app locally using local aws s3 mock
* Add remaining CRUD routes (delete, update)
* Automate integration tests

### Acknowledgements

https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/

https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

https://blog.sicara.com/deploy-serverless-rest-api-lambda-s3-aws-2cf99b8f34ae

The AWS docs - https://docs.aws.amazon.com/

The Serverless docs - https://serverless.com/framework/docs

https://medium.com/@hmajid2301/testing-with-pytest-mock-and-pytest-flask-13cd968e1f24

https://stackoverflow.com/questions/53809090/codebuild-does-not-upload-build-artifact-to-s3 - super helpful!!!

https://dzone.com/articles/boto3-amazon-s3-as-python-object-store

AWS CloudWatch logs were very useful for debugging deployed code