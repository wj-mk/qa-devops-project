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
					execCommand: "docker push bh909303/flask-app"),
				sshTransfer(
					execCommand: "docker push bh909303/flask-db")   
                            ]
                        )
                    ]
                )
            }
        }
}
}
