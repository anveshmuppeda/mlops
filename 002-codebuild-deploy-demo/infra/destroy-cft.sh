#!/bin/bash

# Script to destroy (delete) a CloudFormation stack
# destroy-cft.sh: Script to delete a CloudFormation stack

STACK_NAME="dev-appserver-stack"
REGION="us-east-1"

if [ -z "$STACK_NAME" ]; then
    echo "Usage: $0 <stack-name> [region]"
    exit 1
fi

echo "Deleting CloudFormation stack: $STACK_NAME in region: $REGION"

aws cloudformation delete-stack --stack-name "$STACK_NAME" --region "$REGION"

echo "Waiting for stack deletion to complete..."
aws cloudformation wait stack-delete-complete --stack-name "$STACK_NAME" --region "$REGION"

if [ $? -eq 0 ]; then
    echo "Stack $STACK_NAME deleted successfully."
else
    echo "Failed to delete stack $STACK_NAME."
    exit 2
fi