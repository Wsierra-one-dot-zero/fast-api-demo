# This script deploys the AWS SAM application

sam --version

sam deploy \
  --stack-name $1 \
  --region us-east-1 \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides StageName=$2 \
  --no-confirm-changeset False\