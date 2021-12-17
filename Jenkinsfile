
pipeline{
    agent any
    stages {
    stage('Build and Test Application, Push Images to DockerHub') {
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
					execCommand: "export DATABASE_URI='${database_uri}' && export MYSQL_ROOT_PASSWORD=${password}"),
                sshTransfer(
					execCommand: "cd qa-devops-project && docker-compose build && docker-compose up -d"),
				sshTransfer(
					execCommand: "docker exec qa-devops-project-flask-app-1 bash -c 'cd tests && python3 -m pytest'"),
				sshTransfer(
					execCommand: "docker tag flask-app bh909303/flask-app:${env.BUILD_NUMBER} && docker push bh909303/flask-app:${env.BUILD_NUMBER}"),
				sshTransfer(
					execCommand: "docker tag flask-db bh909303/flask-db:${env.BUILD_NUMBER} && docker push bh909303/flask-db:${env.BUILD_NUMBER}")   
                            ]
                        )
                    ]
                )
            }
        }
    stage('Deploy to DockerSwarm') {
            steps([$class: 'BapSshPromotionPublisherPlugin']) {
                sshPublisher(
                    continueOnError: false, failOnError: true,
                    publishers: [
                        sshPublisherDesc(
                            configName: "swarm",
                            verbose: true,
                            transfers: [
                                sshTransfer(
					execCommand: "docker pull bh909303/flask-app:${env.BUILD_NUMBER}"),
				sshTransfer(
					execCommand: "docker pull bh909303/flask-db:${env.BUILD_NUMBER}"),
				sshTransfer(
					execCommand: "docker service update --image bh909303/flask-app:${env.BUILD_NUMBER} app-stack_flask-app"),
				sshTransfer(
					execCommand: "docker service update --image bh909303/flask-db:${env.BUILD_NUMBER} app-stack_mysql")
                            ]
                        )
                    ]
                )
            }
        }	    
    }
}
