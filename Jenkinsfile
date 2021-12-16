pipeline {

    agent any 

    enviroment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {

        stage('Build') {
            steps {

                sh 'docker-compose up -d'
            }
        
    }
}
}
