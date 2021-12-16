pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                sh 'echo "building the repo"'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        
    }
}
