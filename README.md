# Building-a-Serverless-Facial-Analysis-System

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/8669feb1-c343-45a4-89d6-38abe3add150)

# Overview

For this project, we will explore both serverless and machine-learning services. A serverless service does not eliminate the need for servers to run your apps; rather, you will let AWS manage the servers so you can focus on development. While artificial intelligence has many components that you can use depending on your needs, we’ll use the image recognition feature of Amazon Rekognition. After finishing the project, you can integrate it into an online application form to analyze the uploaded images.

# Objectives

- Create an Amazon S3 bucket with event notifications to trigger the Lambda function.
- Use Amazon Rekognition to detect faces in the uploaded image.
- If the image contains a face, populate the DynamoDB table and trigger Amazon SNS to send email notifications.

# Services:

 - Amazon S3
 - AWS Lambda
 - Amazon Rekognition
 - Amazon DynamoDB
 - Amazon SNS

# 1. Create the Lambda Function

In the AWS Lambda console, choose ‘Create Function’.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/f9fd30e0-7712-48d2-9a0f-207b602c13a4)
![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/efed5d7d-2d5c-4354-be86-cd5c42a48c0d)

# 2. Create an S3 Bucket

On the Amazon S3 console, click ‘Create bucket’ and create your bucket.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/b00d52c6-0ccd-425b-b9de-12ecc3e23918)

Under properties, choose ‘create event notification’. Give the event a name and; choose the event type. Under ‘destination’ choose Lambda function, select your Lambda function from the drop-down, and save changes. This will trigger the Lambda function whenever an image is uploaded.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/e0714d6a-31d1-43f2-ba04-70693a6ed31c)

# 3. Create DynamoDB Table

On the DynamoDB console, click ‘create table’. Give your table a name and create the table. As you can see below, there are no items in the table.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/12cbd58f-2b77-4a46-a4d9-8020aba1cff1)

# 4. Create an SNS Topic

On the SNS console, create your SNS topic and create a subscription.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/5fc66668-f8cb-428b-86ee-913486391120)

# 5. Add your code to the Lambda function.

Replace the default code with the image-rekognition.py and deploy the changes.

# 6. Test

We can now test and see if everything is working as it should. I will upload some images to the S3 bucket.

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/2a8866b5-59d8-4e98-adce-bdceea2ea86e)

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/bb826307-310c-4c6b-a11a-4c00f4d0fc87)

![image](https://github.com/EKechei/Building-a-Serverless-Facial-Analysis-System/assets/128794751/1510fb9b-ca87-4fb3-9ebc-4ac4014d83a9)

My DynamoDB table was populated and I received SNS notifications.







