pipeline {
    agent any 
    stages {
        stage('TEST') {
            steps {
                echo "TEST"
            }
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
                                    execCommand: "rm -rf qa-devops-project"),
                                sshTransfer(
                                    execCommand: "git clone -b jenkins1 https://github.com/wj-mk/qa-devops-project.git"),
                                sshTransfer(
                                    execCommand: "cd qa-devops-project/ && sudo docker-compose up -d"),
                                sshTransfer(
                                    execCommand: "cd qa-devops-project/ && sudo docker-compose run qa-devops-project-1 python3 -m pytest")
                            ]
                        )
                    ]
                )
            }
        }
    }

}
