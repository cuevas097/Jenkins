pipeline {
    agent any 
    stages {
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
        stage('Build') {
             steps {
                 echo 'Building...'
             }
             post {
                 always {
                     jiraSendBuildInfo site: 'carloscuevas.atlassian.net'
                 }
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

