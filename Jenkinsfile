pipeline {
    agent any 
    stages {
        stage('Set environment variables') {
            steps{
                echo "${DATABASE_URI}"
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
