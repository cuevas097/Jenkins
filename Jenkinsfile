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
                git poll: true, url:'https://github.com/cuevas097/Ensamblador_MIPS.git'
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