pipeline {
    agent any 
    stages {
        stage('Set environment variables') {
            steps{
                sh "export DATABASE_URI=${path}"
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
