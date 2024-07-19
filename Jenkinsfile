pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'github-pat', variable: 'GITHUB_TOKEN')]) {
                        sh 'git clone https://$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@github.com/KM-BD/flaskWebApp.git'
                        sh 'cd your-repo'
                    }
                }
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
