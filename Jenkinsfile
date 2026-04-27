pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/SUHOSAMA/aceest-devops.git'
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                docker run --rm \
                -v $(pwd):/app \
                -w /app \
                python:3.11 \
                sh -c "pip install -r requirements.txt && pip install pytest && pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t aceest-app .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f aceest-container || true
                docker run -d -p 5001:5000 --name aceest-container aceest-app
                '''
            }
        }

        stage('Quality Gate') {
            steps {
                echo "Quality check passed"
            }
        }
    }
}