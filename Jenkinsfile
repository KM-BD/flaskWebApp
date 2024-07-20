pipeline {
    agent any
    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KM-BD/flaskWebApp.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose build'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
