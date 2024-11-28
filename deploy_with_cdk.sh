# Install Python dependencies for CDK
pip install -r cdk/requirements.txt

# Bootstrap CDK (if not done already)
cdk bootstrap

# Deploy the stack
cdk deploy