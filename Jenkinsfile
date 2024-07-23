// pipeline {
//     agent {
//         docker {
//             image 'composer:latest'
//         }
//     }
//     stages {
//         stage('Checkout') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/KM-BD/flaskWebApp.git'
//             }
//         }
//         stage('Build') {
//             steps {
//                 script {
//                     sh 'docker-compose down || true'
//                     sh 'docker-compose build'
//                 }
//             }
//         }
//         // stage('Deploy') {
//         //     steps {
//         //         script {
//         //             sh 'docker-compose up -d'
//         //         }
//         //     }
//         // }
//     }
// }
pipeline { 
    agent any 
    environment {
        DOCKER_HOST = 'tcp://docker:2376'
        DOCKER_CERT_PATH = '/certs/client'
        DOCKER_TLS_VERIFY = '1'
    }
    stages { 
        stage ('Checkout') { 
            steps { 
                git branch: 'main', url: 'https://github.com/KM-BD/flaskWebApp.git'
            } 
        } 
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose exec flask_app pytest'
            }
        }
        stage('Code Quality Check via SonarQube') { 
           steps { 
               script { 
                def scannerHome = tool 'flaskWebAppSonarQube'; 
                   withSonarQubeEnv('flaskWebAppSonarQube') { 
                   sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=flaskWebApp -Dsonar.sources=." 
                   } 
               } 
           } 
        } 
    } 
    // post { 
    //     always { 
    //         recordIssues enabledForFailure: true, tool: sonarQube() 
    //     } 
    // } 
} 
