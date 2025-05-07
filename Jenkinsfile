pipeline {
    agent {
        docker {
            image 'myjenkins/aws-sam-cli-python'
        }
    }

    stages {
        stage('Verificar entorno') {
            steps {
                sh '''
                    python --version
                    aws --version
                    sam --version
                '''
            }
        }
    }
}
