pipeline {
    agent any

    parameters {
        string(name: 'AWS_ROL_ARN', defaultValue: '', description: 'AWS ROL')
    }

    environment {
        AWS_REGION = 'us-east-1'
        STACK_NAME = 'fastapi-stack'
    }

    stages {
        // Etapa 1: Checkout del código
        stage('Checkout') {
            steps {
                git branch: 'devops-jenkins', url: 'https://github.com/Wsierra-one-dot-zero/fast-api-demo'
            }
        }

        // Etapa 2: Configurar AWS (OIDC o Access Keys)
        stage('Configure AWS') {
            steps {
                script {
                    sh '''
                        ASSUME_ROLE_OUTPUT=$(aws sts assume-role \
                            --role-arn "${parameters.AWS_ROL_ARN}" \
                            --role-session-name "Rol_from_Jenkins" \
                            --duration-seconds "3600" \
                            --profile "default" \
                            --output json 2>&1)

                        if [ $? -ne 0 ]; then
                            echo "Error al asumir el rol:"
                            echo "$ASSUME_ROLE_OUTPUT"
                            exit 1
                        fi

                        AWS_ACCESS_KEY_ID=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.AccessKeyId')
                        AWS_SECRET_ACCESS_KEY=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SecretAccessKey')
                        AWS_SESSION_TOKEN=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SessionToken')
                        EXPIRATION=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.Expiration')

                        export AWS_ACCESS_KEY_ID
                        export AWS_SECRET_ACCESS_KEY
                        export AWS_SESSION_TOKEN
                        export AWS_DEFAULT_REGION=us-east-1

                        echo "Credenciales temporales configuradas con éxito!"

                        echo "Ahora puedes usar los comandos de AWS CLI con el rol asumido."
                        echo "Estas credenciales son temporales y solo durarán hasta la expiración."
                    '''
                }
            }
        }

        // Etapa 3: Instalar SAM CLI
        stage('Install SAM CLI') {
            steps {
                sh '''
                    aws s3 ls
                '''
            }
        }

        // Etapa 3: Instalar SAM CLI
        //stage('Install SAM CLI') {
        //     steps {
        //         sh '''
        //             pip install --upgrade aws-sam-cli
        //             sam --version
        //         '''
        //     }
        // }

        // Etapa 4: Build 
        // stage('Build') {
        //     steps {
        //         sh '''
        //             sam build
        //         '''
        //     }
        // }

        // Etapa 5: Deploy
        // stage('Build & Deploy') {
        //     steps {
        //         sh '''
        //             sam build
        //             sam deploy --stack-name ${STACK_NAME} \
        //                 --region ${AWS_REGION} \
        //                 --resolve-s3 \
        //                 --capabilities CAPABILITY_IAM \
        //                 --parameter-overrides StageName=Demo \
        //                 --no-confirm-changeset \
        //                 --no-fail-on-empty-changeset
        //         '''
        //     }
        // }
    }

    post {
        always {
            cleanWs()  // Limpia el workspace al finalizar
        }
    }
}