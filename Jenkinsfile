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
					execCommand: "cd qa-devops-project && sudo docker-compose build && docker-compose up -d"),
                            ]
                        )
                    ]
                )
            }
        }
}
}
