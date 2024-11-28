#!/usr/bin/env python3
import aws_cdk as cdk
from loan_app_stack import LoanAppStack

app = cdk.App()
LoanAppStack(app, "LoanAppStack")
app.synth()
