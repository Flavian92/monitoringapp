import boto3
#Imports the Boto3 library, which is the official AWS SDK for Python

ecr_client = boto3.client('ecr')
#Creates an ECR client object, which will be used to make requests to the ECR service.

repository_name = "my_monitoring_app_image"
#The variable repository_name is set to the desired name for the Docker image repository. In this example, it is set to "my_monitoring_app_image."

response = ecr_client.create_repository(repositoryName=repository_name)
#The create_repository method is called on the ECR client to create a new repository with the specified name. 
# The response from the API call is stored in the response variable.

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)