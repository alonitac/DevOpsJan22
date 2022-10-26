pipeline {
  agent any
  stages {
    stage('Git Clone') {
      
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/alonitac/DevOpsJan22.git'
      }
      
    }
    stage('Upload to artifact') {
      steps {
        dir('20_artifact_repositories/fantastic_ascii/') {
            withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
              sh '''
              pip3 install build twine virtualenv
              python3 -m build
              python3 -m twine upload --repository-url http://13.50.17.185:8081/repository/pypi-internal-packages/ -u $USER -p $PASSWORD dist/*
              '''
            }
        }
      }
    }
  }
}