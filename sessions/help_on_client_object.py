import boto3

aws_mag_con = boto3.session.Session(profile_name="sergeip")

# iam, ec2 and s3
iam_con_cli = aws_mag_con.client(service_name="iam", region_name="us-east-1")
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
s3_con_cli = aws_mag_con.client(service_name="s3", region_name="us-east-1")

# List all iam users using client object
response = iam_con_cli.list_users()
for user in response['Users']:
    print(user['UserName'], ':', user['Arn'])
print('------------------------------')

# List all ec2 instances ids
response = ec2_con_cli.describe_instances()
for each_item in response['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])
    print('------------------------------')

# List all buckets
response = s3_con_cli.list_buckets()
for each_bucket in response['Buckets']:
    print(each_bucket['Name'])

