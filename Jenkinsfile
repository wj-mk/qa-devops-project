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
                                    execCommand: "git pull https://github.com/wj-mk/qa-devops-project"),
                            ]
                        )
                    ]
                )
            }
        }
}
}
