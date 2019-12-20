import boto3

s3 = boto3.resource('s3') #S3オブジェクトを取得

bucket = s3.Bucket('manibacket')
bucket.upload_file('/Users/imanishiyuujin/onigiri/media/frame.jpg', 'https://manibacket.s3-ap-northeast-1.amazonaws.com/media/test.jpg')