import boto3

aws_mag_con = boto3.session.Session(profile_name="sergeip")

iam_con_re = aws_mag_con.resource(service_name="iam", region_name="us-east-1")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
s3_con_re = aws_mag_con.resource(service_name="s3", region_name="us-east-1")

# List all iam users
for user in iam_con_re.users.all():
    print(user.user_name)

print('--------------------------------')

# List all S3 Buckets
for bucket in s3_con_re.buckets.all():
    print(bucket.name)

print('--------------------------------')

# List all ec2 instances
for instance in ec2_con_re.instances.all():
    print(instance)