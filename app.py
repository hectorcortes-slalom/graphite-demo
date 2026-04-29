#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_cdk_app.my_cdk_app_stack import MyCdkAppStack

app = cdk.App()

MyCdkAppStack(
    app,
    "MyCdkAppStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
