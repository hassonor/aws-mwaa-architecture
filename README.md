[### How to run first time

# AWS Credentials Setup Guide

## Prerequisites

Before setting up AWS credentials, ensure you have:

- An AWS account with necessary permissions.
- AWS CLI installed on your local machine.
- Required access to AWS services (e.g., Secrets Manager, IAM, etc.).

## Steps to Set Up AWS Credentials

### Step 1: Install AWS CLI

If you haven't already installed the AWS CLI, download and install it from:
[https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

Verify installation with:

```sh
aws --version
```

### Step 2: Configure AWS CLI Credentials

Run the following command to configure your AWS credentials:

```sh
aws configure
```

You'll be prompted to enter:

1. **AWS Access Key ID**
2. **AWS Secret Access Key**
3. **Default region name** (e.g., `us-east-1`)
4. **Default output format** (choose `json`, `yaml`, or `table`)

Example input:

```
AWS Access Key ID [None]: AKIAXXXXXXXXXXXXXX
AWS Secret Access Key [None]: wJalrXXXXXXXXXX
Default region name [None]: us-east-1
Default output format [None]: json
```

### Step 3: Verify Configuration

To confirm that your credentials are set up correctly, run:

```sh
aws sts get-caller-identity
```

This should return your AWS account details.

### Step 4: Set Up Environment Variables (Optional)

If you prefer, you can set AWS credentials via environment variables:

```sh
export AWS_ACCESS_KEY_ID="AKIAXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="wJalrXXXXXXXXXX"
export AWS_REGION="us-east-1"
```

To make these settings persistent, add them to your `~/.bashrc` or `~/.zshrc` file.

### Step 5: Test AWS Services Access

Run a sample command to ensure access, for example:

```sh
aws s3 ls
```

If the credentials are set up correctly, this should list available S3 buckets.

## Troubleshooting

- If you encounter `InvalidClientTokenId`, ensure your AWS Access Key is correct.
- If you get `AccessDenied`, check your IAM policies.
- Use `aws configure list` to inspect your current AWS credential settings.

## Next Steps

1. Follow the steps on `docs/CONFLUENT_CLOUD_STEPS.md`
2. Follow the steps on `docs/AWS_CONSOLE_STEPS_1`
3. Follow the steps on `docs/GITHUB_STEPS`
4. Follow the steps on `docs/AWS_CONSOLE_STEPS_2`
5. Run Dags On `Airflow UI`  (Get the link from AWS console)