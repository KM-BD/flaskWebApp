pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KM-BD/flaskWebApp.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker-compose down || true'
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
