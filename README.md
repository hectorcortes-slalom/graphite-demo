# AWS Python CDK Starter Template

A starter template for building AWS infrastructure with the [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) in Python.

## What's included

| Resource | Purpose |
|---|---|
| **S3 Bucket** | Versioned, encrypted, private data bucket |
| **Lambda Function** | Python 3.12 function with access to the bucket |
| **IAM Role** | Least-privilege execution role for Lambda |
| **Stack Outputs** | Bucket name & function name exported for easy reference |

## Project layout

```
.
├── app.py                        # CDK app entry point
├── cdk.json                      # CDK toolkit configuration
├── requirements.txt              # Runtime dependencies
├── requirements-dev.txt          # Dev / test dependencies
├── my_cdk_app/
│   ├── __init__.py
│   └── my_cdk_app_stack.py      # CDK stack definition
└── tests/
    └── unit/
        └── test_my_cdk_app_stack.py
```

## Prerequisites

- Python 3.8+
- Node.js 18+ (required by the CDK CLI)
- AWS CLI configured with valid credentials (`aws configure`)
- AWS CDK CLI: `npm install -g aws-cdk`

## Getting started

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements-dev.txt

# 3. Bootstrap your AWS environment (first time only)
cdk bootstrap

# 4. Synthesise the CloudFormation template
cdk synth

# 5. Deploy to AWS
cdk deploy

# 6. Tear down when you're done
cdk destroy
```

## Running the tests

```bash
pytest tests/
```

## Customising the stack

Edit `my_cdk_app/my_cdk_app_stack.py` to add, remove, or change AWS resources.
The [CDK Python API reference](https://docs.aws.amazon.com/cdk/api/v2/python/) lists every available construct.
