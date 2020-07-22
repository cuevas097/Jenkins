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
        stage('Deploy') { 
            steps {
                sh '''
                    echo 'Hola mundo'
                '''
            }
        }
    }
}