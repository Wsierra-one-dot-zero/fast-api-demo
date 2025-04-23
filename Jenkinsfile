pipeline {
    agent {
        docker {
            image 'public.ecr.aws/sam/build-python3.12:latest'  // Imagen oficial de AWS SAM
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Necesario para builds con Docker
        }
    }

    environment {
        AWS_REGION = 'us-east-1'
        STACK_NAME = 'fastapi-stack'
    }

    stages {
        // Etapa 1: Checkout del código
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Wsierra-one-dot-zero/fast-api-demo'
            }
        }

        // Etapa 2: Configurar AWS (OIDC o Access Keys)
        stage('Configure AWS') {
            steps {
                script {
                    // Opción A: Usar OIDC (requiere plugin "AWS Credentials" y configuración previa)
                    withAWS(role: 'arn:aws:iam::111383061799:role/github-actions-role', roleAccount: '111383061799', region: env.AWS_REGION) {
                        // Tus comandos AWS aquí
                    }
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

    post {
        success {
            slackSend channel: '#devops',
                     message: "✅ Despliegue exitoso: ${env.JOB_NAME} (#${env.BUILD_NUMBER})"
        }
        failure {
            slackSend channel: '#devops',
                     message: "❌ Falló el despliegue: ${env.JOB_NAME} (#${env.BUILD_NUMBER})"
        }
    }
}