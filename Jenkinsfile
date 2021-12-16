pipeline{

	agent any

<<<<<<< HEAD
    enviroment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stage('Build and Test Application') {
            steps([$class: 'BapSshPromotionPublisherPlugin']) {
                sshPublisher(
                    continueOnError: false, failOnError: true,
                    publishers: [
                        sshPublisherDesc(
                            configName: "test-build",
                            verbose: true,
                            transfers: [
                                sshTransfer(
                                    execCommand: "git pull origin jenkins1"),
                            ]
                        )
                    ]
                )
            }
        }
}
=======
	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker-compose up -d'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push bh909303/qa-devops-project:tagname'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

>>>>>>> 154c18562c9338dad092050d38e52a43873cf04a
}
