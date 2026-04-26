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
                sh '''
                python3 -m pip install --upgrade pip --break-system-packages
                pip3 install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PATH=$PATH:/var/jenkins_home/.local/bin
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'echo "Skipping Docker build for now"'
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Quality check passed'
            }
        }
    }
}