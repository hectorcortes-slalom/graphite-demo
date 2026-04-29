import aws_cdk as cdk
from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_iam as iam,
    Duration,
    RemovalPolicy,
)
from constructs import Construct


class MyCdkAppStack(cdk.Stack):
    """Sample CDK stack demonstrating common AWS resources.

    Resources created:
    - S3 bucket for storing application data
    - Lambda function with basic execution role
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket for application data
        data_bucket = s3.Bucket(
            self,
            "DataBucket",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.RETAIN,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # IAM role for the Lambda function
        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                )
            ],
        )

        # Grant the Lambda role read access to the bucket
        data_bucket.grant_read(lambda_role)

        # Lambda function
        handler = lambda_.Function(
            self,
            "AppFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=lambda_.Code.from_inline(
                "def handler(event, context):\n"
                "    print('Hello from Lambda!')\n"
                "    return {'statusCode': 200, 'body': 'OK'}\n"
            ),
            role=lambda_role,
            timeout=Duration.seconds(30),
            environment={
                "BUCKET_NAME": data_bucket.bucket_name,
            },
        )

        # Stack outputs
        cdk.CfnOutput(self, "BucketName", value=data_bucket.bucket_name)
        cdk.CfnOutput(self, "FunctionName", value=handler.function_name)
