pipeline {
    agent any

    stages {

        stage('Clean') {
            steps {
                deleteDir()
            }
        }

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/SUHOSAMA/aceest-devops.git'
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                python3 --version
                pip3 --version

                pip3 install --break-system-packages -r requirements.txt
                pip3 install --break-system-packages pytest

                python3 -m pytest
                '''
            }
        }

        stage('Success') {
            steps {
                echo "BUILD SUCCESS"
            }
        }
    }
}