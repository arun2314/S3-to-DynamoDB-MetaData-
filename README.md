# S3 to DynamoDB Metadata

## Step 1: Create an S3 Bucket
1. Go to **AWS S3** → Click **Create Bucket**.
2. Set a **unique bucket name** and **region**.
3. Enable **event notifications** for the bucket.

## Step 2: Create a DynamoDB Table
1. Go to **AWS DynamoDB** → Click **Create Table**.
2. Set **Table Name**: `ImageMetadata`.
3. Set **Primary Key**: `image_id` (String).
4. Click **Create table**.

## Step 3: Create an AWS Lambda Function
1. Go to **AWS Lambda** → Click **Create Function**.
2. Choose **Author from scratch**.
3. Set **Function Name**: `S3ToDynamoDB`.
4. Choose **Runtime**: `Python 3.x`.
5. Attach the following permissions:
   - `AmazonS3ReadOnlyAccess`
   - `AmazonDynamoDBFullAccess`

## Step 4: Link S3 Event to Lambda
1. Go to **S3** → Select your bucket.
2. Click **Properties** → Scroll down to **Event Notifications**.
3. Click **Create Event Notification**.
4. Set **Name**: `ImageUploadTrigger`.
5. Choose **Event Type**: `PUT` (for new uploads).
6. Click **Save**.

## Step 5: Test the Setup
1. Upload an image to **S3**.
2. Check **DynamoDB**, and the metadata should be added automatically! 🎉

