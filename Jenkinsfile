pipeline {
  agent any

  stages {
    stage("build docker image and push to DockerHub") {
      steps {
        script {
          echo "building the docker image..."
          withCredentials([usernamePassword(credentialsId: "dockerhub-creds", passwordVariable: "PASS", usernameVariable: "USER")]) {
            sh "docker build -t dipanshu18/flask_api_jenkins_demo:v3 ."
            sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
            sh "docker push dipanshu18/flask_api_jenkins_demo:v3"
          }
        }
      }
    }
    stage("deploy") {
      steps {
        echo "Deployment started"
      }
    }
  }
}