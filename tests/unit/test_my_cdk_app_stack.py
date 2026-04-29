import aws_cdk as cdk
from aws_cdk.assertions import Template, Match

from my_cdk_app.my_cdk_app_stack import MyCdkAppStack


def _get_template() -> Template:
    app = cdk.App()
    stack = MyCdkAppStack(app, "TestStack")
    return Template.from_stack(stack)


def test_s3_bucket_created():
    template = _get_template()
    template.resource_count_is("AWS::S3::Bucket", 1)


def test_s3_bucket_versioning_enabled():
    template = _get_template()
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    )


def test_s3_bucket_encryption():
    template = _get_template()
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "ServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            }
        },
    )


def test_s3_bucket_blocks_public_access():
    template = _get_template()
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            }
        },
    )


def test_lambda_function_created():
    template = _get_template()
    template.resource_count_is("AWS::Lambda::Function", 1)


def test_lambda_function_runtime():
    template = _get_template()
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Runtime": "python3.12",
        },
    )


def test_lambda_has_bucket_env_var():
    template = _get_template()
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Environment": {
                "Variables": {
                    "BUCKET_NAME": Match.any_value(),
                }
            }
        },
    )


def test_iam_role_created():
    template = _get_template()
    template.has_resource_properties(
        "AWS::IAM::Role",
        {
            "AssumeRolePolicyDocument": {
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {"Service": "lambda.amazonaws.com"},
                    }
                ]
            }
        },
    )


def test_stack_outputs():
    template = _get_template()
    template.has_output("BucketName", {})
    template.has_output("FunctionName", {})
