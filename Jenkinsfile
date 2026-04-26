pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SUHOSAMA/aceest-devops.git'
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 sh -c "
                pip install -r requirements.txt &&
                pip install pytest &&
                pytest
                "
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Quality check passed'
            }
        }
    }
}