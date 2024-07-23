pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flaskwebapp'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Unit Test') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'pytest test_app.py'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.compose.up('-d')
                }
            }
        }

        stage('Integration and UI Test') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'pytest integration_ui_tests.py'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                docker.compose.down()
            }
        }
    }
}
