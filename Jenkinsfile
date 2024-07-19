pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/KM-BD/flaskWebApp.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Clean up any previous containers
                    sh 'docker-compose down'
                }
                // Build the Docker images
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                // Run the Docker containers
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
