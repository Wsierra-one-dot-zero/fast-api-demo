aws cloudformation delete-stack \
  --stack-name $1

# Check if the delete was successful
if [ $? -ne 0 ]; then
  echo "Delete failed"
  exit 1
else
    echo "Delete succeeded"
fi
# Check if the stack is deleted 
aws cloudformation wait stack-delete-complete \
  --stack-name $1
# Check if the wait was successful
if [ $? -ne 0 ]; then
  echo "Wait failed"
  exit 1
else
    echo "Wait succeeded"
fi