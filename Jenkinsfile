pipeline {

    agent any 

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
}
