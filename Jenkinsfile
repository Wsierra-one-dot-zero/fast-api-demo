pipeline {
    agent any

    parameters {
        string(name: 'AWS_ROL_ARN', defaultValue: '', description: 'ARN del rol a asumir')
    }

    environment {
        AWS_REGION = 'us-east-1'
    }

    stages {
        stage('Assume Role') {
            steps {
                withCredentials([
                    string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                        set -e
                        echo "Asumiendo el rol ${AWS_ROL_ARN}"

                        ASSUME_ROLE_OUTPUT=$(aws sts assume-role \
                            --role-arn "${AWS_ROL_ARN}" \
                            --role-session-name "jenkins-session" \
                            --duration-seconds 3600 \
                            --output json)

                        export AWS_ACCESS_KEY_ID=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.AccessKeyId')
                        export AWS_SECRET_ACCESS_KEY=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SecretAccessKey')
                        export AWS_SESSION_TOKEN=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SessionToken')

                        aws sts get-caller-identity
                    '''
                }
            }
        }
    }
}
