pipeline {
    agent any

    parameters {
        string(name: 'AWS_ROL_ARN', defaultValue: '', description: 'ARN del rol a asumir')
    }

    environment {
        AWS_REGION = 'us-east-1'
        STACK_NAME = 'fastapi-stack'
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

        // Etapa 3: Instalar SAM CLI
        stage('Install SAM CLI') {
            steps {
                sh '''
                    pip install --upgrade aws-sam-cli
                    sam --version
                '''
            }
        }

        // Etapa 4: Build 
        stage('Build') {
            steps {
                sh '''
                    sam build
                '''
            }
        }

        // Etapa 5: Deploy
        stage('Build & Deploy') {
            steps {
                sh '''
                    sam build
                    sam deploy --stack-name ${STACK_NAME} \
                        --region ${AWS_REGION} \
                        --resolve-s3 \
                        --capabilities CAPABILITY_IAM \
                        --parameter-overrides StageName=Demo \
                        --no-confirm-changeset \
                        --no-fail-on-empty-changeset
                '''
            }
        }
    }
}
