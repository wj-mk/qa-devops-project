pipeline {
    agent any 
    stages {
        stage('TEST') {
            steps {
                echo "TEST"
            }
        }
        stage('SSH transfer') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "test-build",
                        verbose: true,
                        transfers: [
                            sshTransfer(echo: "testing")
                        ]
                    )
                ]
            )
        }
    }
    }

}
