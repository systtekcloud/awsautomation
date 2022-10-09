# Script to see/list all aim users
# ================================
# Get AWS IAM Users
import boto3

aws_mag_con=boto3.session.Session(profile_name="sergeip")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)