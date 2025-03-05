# S3-to-DynamoDB-MetaData-
Step 1: Create an S3 Bucket
Go to AWS S3 → Click Create Bucket.
Set a unique bucket name and region.
Enable event notifications for the bucket.

Step 2: Create a DynamoDB Table
Go to AWS DynamoDB → Click Create Table.
Table Name: ImageMetadata
Primary Key: image_id (String)
Click Create table.

Step 3: Create an AWS Lambda Function
Go to AWS Lambda → Click Create Function.
Choose Author from scratch.
Function Name: S3ToDynamoDB
Runtime: Python 3.x
Permissions: Attach AmazonS3ReadOnlyAccess & AmazonDynamoDBFullAccess.

Step 4: Link S3 Event to Lambda
Go to S3 → Select your bucket.
Click Properties → Scroll down to Event Notifications.
Click Create Event Notification.
Name: ImageUploadTrigger
Event Type: "PUT" (for new uploads).
Click Save.

Step 5: Test the Setup
Upload an image to S3.
Check DynamoDB, and the metadata should be added automatically! 🎉
   
