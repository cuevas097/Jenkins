pipeline {
    agent any 
    stages {
        
        stage('Build') {
            steps {
                 echo 'Building...'
            }
            post {
                 always {
                     jiraSendBuildInfo site: 'example.atlassian.net'
                 }
            }
         }
        stage('Build') { 
            steps {
                sh '''
                    echo "Hola"
                '''
            }
        }
        stage('Test') { 
            steps {
                sh '''
                python DistanciaEuclidiana.py
                '''
            }
        }
        stage('Deploy') { 
            steps {
                sh '''
                    echo 'Hola mundo'
                '''
            }
        }
    }
}
