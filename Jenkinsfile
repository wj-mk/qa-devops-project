pipeline {

    agent any 

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {

        stage('Build') {
            steps {

                sh 'docker-compose build'
            }
        
    }
}
}
