# This script builds the AWS SAM application

sam --version

sam build

# Check if the build was successful
if [ $? -ne 0 ]; then
  echo "Build failed"
  exit 1
else
    echo "Build succeeded"
fi
