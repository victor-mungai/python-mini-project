import boto3
#create an s3 client

s3 = boto3.client('s3') 

# define the bucket name and the file to upload

bucket_name = 'botopython27811234'
file_name = input("Enter the path of the file to upload: ")
object_name = file_name
 
#upload file to s3
try:
    
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"File {file_name} uploaded to bucket {bucket_name} as {object_name}.")
except Exception as e:
    print(f"Error uploading file: {e}")
