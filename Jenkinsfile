pipeline {
    agent any 
    stages {
        stage('Set environment variables') {
            steps{
                sh "export DATABASE_URI=${env.path}"
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
