# Deploy simple html application using AWS CodeBuild and CodeDeploy

# This example demonstrates how to deploy a simple HTML application using AWS CodeBuild and CodeDeploy.

## Prerequisites
- AWS account with necessary permissions to create CodeBuild, CodeDeploy, and S3 resources.
- AWS CLI installed and configured with your credentials.
- Basic understanding of AWS CodeBuild, CodeDeploy, and S3.
- Clone this repository to your local machine:
    ```bash
    git clone
    ```
- Navigate to the `002-codebuild-deploy-demo` directory:
    ```bash
    cd 002-codebuild-deploy-demo
    ```
- This directory contains the necessary files and scripts to set up the deployment pipeline.
    ```bash
    > tree 002-codebuild-deploy-demo
    002-codebuild-deploy-demo
    ├── README.md
    ├── app
    │   └── index.html
    ├── appspec.yml
    ├── buildspec.yaml
    ├── infra
    │   ├── appservers-tmp.yaml
    │   ├── destroy-cft.sh
    │   └── launch-cft.sh
    └── scripts
        ├── after_install.sh
        ├── install_dependencies.sh
        ├── start_server.sh
        ├── stop_server.sh
        └── validate_service.sh

    4 directories, 12 files
    ```

Let's first create a CodeBuild project that will build our application and then deploy it using CodeDeploy.

## Step 1: Create CodeBuild Project from the AWS Management Console
1. Go to the [AWS CodeBuild console](https://console.aws.amazon.com/codesuite/codebuild/projects).
2. Click on **Create build project**.
3. Fill in the project name, e.g., `Html-CodeBuild-Project`.
4. In the **Source** section, choose **GitHub** or **CodeCommit** as the source provider and connect your repository containing the HTML files.
5. In the **Environment** section, choose the following:
   - **Environment image**: Managed image
    - **Compute**: EC2
    - **Running Mode**: Instance
    - **Operating system**: Amazon Linux
    - **Servce role**: Create a new service role or use an existing one with proper permissions.
6. In the **Buildspec** section, choose **Use the buildspec.yml file** if you have one in your repository, or you can create a new one. (See below for an example buildspec.yml)
7. Artifacts:
   - In the **Artifacts** section, choose **Amazon S3** and specify the S3 bucket where you want to store the build artifacts.
8. Click on **Create build project**.

## Step 2: Create CodeDeploy Application
1. Go to the [AWS CodeDeploy console](https://console.aws.amazon.com/codesuite/codedeploy/applications).
2. Click on **Create application**.
3. Fill in the application name, e.g., `Html-CodeDeploy-Application`.
4. Choose the compute platform as **EC2/On-premises**.
5. Click on **Create application**.

## Step 3. Deploy Development Servers using CloudFormation
1. Navigate to "002-codebuild-deploy-demo/infra" directory.
2. Then run the following command to launch the CloudFormation stack:
```bash
cd 002-codebuild-deploy-demo/infra
./launch-cft.sh
```
This script will create a CloudFormation stack that sets up the necessary infrastructure, including EC2 instances for deployment.

## Step 4: Create CodeDeploy Deployment Group
1. In the CodeDeploy application you just created, click on **Create deployment group**.
2. Fill in the deployment group name, e.g., `Development-Html-CodeDeploy-Deploy-Group`.
3. Choose the service role that has proper permissions for CodeDeploy. (i.e., `arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole`)
4. In the **Environment configuration** section, choose the deployment type as **In-place deployment**.
    - Choose the deployment group type as **Amazon EC2 instances**.
    - Select the EC2 instances where you want to deploy the application by using tags.
5. In the **Deployment settings**, choose the deployment type as **CodeDeployDefault.OneAtATime**.
6. In the **Load balancer** section, you can skip this if you are not using a load balancer.
7. Click on **Create deployment group**.    

## Step 5: Run CodeBuild 
1. Go to the CodeBuild project you created.
2. Click on **Start build**.
3. It will start the build process, and once completed, it will upload the build artifacts to the specified S3 bucket.

## Step 5: Create CodeDeploy Deployment
1. Go to the CodeDeploy application you created.
2. Click on **Create deployment**.
3. Fill in the deployment group name you created earlier.
4. In the **Revision type**, choose **My application is stored in Amazon S3**.
5. Specify the S3 bucket and the path to the build artifact (e.g., `s3://your-bucket-name/build-artifact.zip`).
6. Select **Revision File Type** as build artifact type extension (e.g., `zip`).
7. Click on **Create deployment**.

## Step 6: Verify Deployment
1. Go to the EC2 instances where you deployed the application.
2. SSH into the instance and navigate to the `/var/www/html/` directory.
3. You should see the `index.html` file deployed there.
4. Open a web browser and navigate to the public IP address of the EC2 instance to see your HTML application running.

## Step 7: Clean Up
To clean up the resources created during this demo, you can run the `destroy-cft.sh` script in the `infra` directory:
```bashcd 002-codebuild-deploy-demo/infra
./destroy-cft.sh
```
This will delete the CloudFormation stack and all associated resources.

And delete the CodeBuild and CodeDeploy resources manually from the AWS Management Console if needed.