import boto3

aws_mag_con_admin = boto3.session.Session(profile_name="sergeip")

iam_con_re = aws_mag_con_admin.resource(service_name='iam', region_name='us-central-1')
iam_con_cli = aws_mag_con_admin.client(service_name='iam', region_name='us-central-1')

# Listing iam users with resources object

for each_user in iam_con_re.users.all():
    print(each_user.name)

print("------------------------------")

for each in iam_con_cli.list_users()['Users']:
    print(each['UserName'])