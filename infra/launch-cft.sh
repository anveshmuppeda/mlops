#!/bin/bash

# launch-cft.sh: Script to create and deploy a CloudFormation template

STACK_NAME="dev-appserver-stack"
TEMPLATE_FILE="appservers-tmp.yaml"
REGION="us-east-1"

# Check if template file exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: $TEMPLATE_FILE not found!"
    exit 1
fi

# Check if the CloudFormation stack already exists
if aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" >/dev/null 2>&1; then
    echo "Stack '$STACK_NAME' exists. It will be updated."
    aws cloudformation update-stack \
        --stack-name "$STACK_NAME" \
        --template-body file://"$TEMPLATE_FILE" \
        --region "$REGION" \
        --parameters ParameterKey=Environment,ParameterValue=Development \
                    ParameterKey=KeyName,ParameterValue=cicd \
        --capabilities CAPABILITY_NAMED_IAM
else
    echo "Stack '$STACK_NAME' does not exist. It will be created."
    aws cloudformation create-stack \
        --stack-name "$STACK_NAME" \
        --template-body file://"$TEMPLATE_FILE" \
        --region "$REGION" \
        --parameters ParameterKey=Environment,ParameterValue=Development \
                    ParameterKey=KeyName,ParameterValue=cicd \
        --capabilities CAPABILITY_NAMED_IAM
fi

if [ $? -eq 0 ]; then
    echo "CloudFormation stack '$STACK_NAME' deployed successfully."
else
    echo "Failed to deploy CloudFormation stack."
    exit 1
fi