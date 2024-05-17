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
