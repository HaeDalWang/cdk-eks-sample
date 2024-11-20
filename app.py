#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_eks_sample.cdk_eks_sample_stack import CdkEksSampleStack


app = cdk.App()
CdkEksSampleStack(app, "CdkEksSampleStack",)


app.synth()
