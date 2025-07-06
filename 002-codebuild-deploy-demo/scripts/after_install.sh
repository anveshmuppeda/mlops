#!/bin/bash

TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" -s)
EC2_INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id)
EC2_INSTANCE_TYPE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-type)
EC2_AZ=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/placement/availability-zone)

echo "EC2_INSTANCE_ID: $EC2_INSTANCE_ID"
echo "EC2_INSTANCE_TYPE: $EC2_INSTANCE_TYPE"
echo "EC2_AZ: $EC2_AZ"

sed -i "s/Application successfully deployed via AWS CICD Pipeline/This is currently runnining on $EC2_INSTANCE_TYPE with id - $EC2_INSTANCE_ID on AZ - $EC2_AZ/g" /var/www/html/index.html
chmod 664 /var/www/html/index.html