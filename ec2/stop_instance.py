import boto3
aws_user = "ec2-developer"
aws_service = "ec2"
aws_region = "us-east-1"
aws_mag_con = boto3.session.Session(profile_name=aws_user)
ec2_con_cli = aws_mag_con.client(service_name=aws_service, region_name=aws_region)
instances = ['i-050600bfcbdbd33aa']


def stopEC2instance():
    ec2_con_cli.stop_instances(InstanceIds=instances)
    print('your instances: ' + str(instances) + ' was stopped!')


stopEC2instance()
