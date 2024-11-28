# Authenticate Docker to ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

# Build Docker image
docker build -t loan-app .

# Tag the image
docker tag loan-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/loanapprepository:latest

# Push the image
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/loanapprepository:latest