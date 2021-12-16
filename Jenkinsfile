pipeline{

	agent any

    stages {

    
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
					execCommand: "cd qa-devops-project && git pull"),
				sshTransfer(
					execCommand: "cd qa-devops-project && docker-compose up -d"),
				sshTransfer(
					execCommand: "docker-compose run flask-app bash cd tests && python3 -m pytest"),
				sshTransfer(
					execCommand: "docker tag flask-app bh909303/flask-app && docker push bh909303/flask-app"),
				sshTransfer(
					execCommand: "docker tag flask-db bh909303/flask-db && docker push bh909303/flask-db")   
                            ]
                        )
                    ]
                )
            }
        }
}
}
