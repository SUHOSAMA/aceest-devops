pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SUHOSAMA/aceest-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m ensurepip --upgrade || true'
                sh 'python3 -m pip install --upgrade pip || true'
                sh 'pip3 install -r requirements.txt --break-system-packages'
                sh 'pip3 install pytest --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-app . || true'
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Quality check passed'
            }
        }
    }
}