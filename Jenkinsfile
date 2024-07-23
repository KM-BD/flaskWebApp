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
    stages { 
        stage ('Checkout') { 
            steps { 
                git branch: 'main', url: 'https://github.com/KM-BD/flaskWebApp.git'
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
