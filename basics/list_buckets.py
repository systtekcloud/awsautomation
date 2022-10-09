# Script to see/list all aim users
# ================================
# Get AWS Buckets
import boto3

aws_mag_con=boto3.session.Session(profile_name="sergeip")
s3_con=aws_mag_con.resource('s3')

for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)