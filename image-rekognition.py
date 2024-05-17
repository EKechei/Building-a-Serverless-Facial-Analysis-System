import boto3

def lambda_handler(event, context):
    # Initialize the S3 client, Rekognition client, DynamoDB client, and SNS client
    s3_client = boto3.client('s3')
    rekognition_client = boto3.client('rekognition')
    dynamodb = boto3.client('dynamodb')
    sns = boto3.client('sns')

    # Define the S3 bucket name
    bucket_name = 'totsdemo'

    # List all objects in the S3 bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Process each object in the bucket
    if 'Contents' in response:
        for obj in response['Contents']:
            object_key = obj['Key']
            # Your processing logic for S3 objects here…

            # Detect faces in the current object
            response_faces = rekognition_client.detect_faces(
                Image={
                    'S3Object': {
                        'Bucket': bucket_name,
                        'Name': object_key
                    }
                },
                Attributes=['ALL']
            )

            # Print information about detected faces
            if 'FaceDetails' in response_faces:
                faces = response_faces['FaceDetails']
                for face in faces:
                    gender = face['Gender']['Value']
                    age_range = f"{face['AgeRange']['Low']} - {face['AgeRange']['High']}"
                    print(f"Detected face in object {object_key} - Gender: {gender}, Age Range: {age_range}")

                    # Store face information in DynamoDB
                    dynamodb.put_item(
                        TableName='rekognitioninfo',
                        Item={
                            'ImageKey': {'S': object_key},
                            'Gender': {'S': gender},
                            'AgeRange': {'S': age_range}
                        }
                    )

                    # Publish a message to the SNS topic
                    sns.publish(
                        TopicArn='arn:aws:sns:us-east-1:4xxxxxxxxxx5:dynamoalert',
                        Message="New item added to DynamoDB: Gender - {}, Age Range - {}".format(gender, age_range),
                        Subject='DynamoDB Notification'
                    )
            else:
                print(f"No faces detected in object {object_key}.")
    else:
        print("No objects found in the bucket.")
