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
                                sshTransfer(
                                    execCommand: "rm -rf qa-devops-project"),
                                sshTransfer(
                                    execCommand: "git clone -b jenkins1 https://github.com/wj-mk/qa-devops-project.git"),
                                sshTransfer(
                                    execCommand: "cd qa-devops-project/ && sudo docker-compose up -d")
                            ]
                        )
                    ]
                )
            }
        }
    }

}
