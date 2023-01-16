pipeline {
    agent {
        label 'ec2'
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-repo/your-app.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t your-app .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -p 8501:8501 your-app'
            }
        }
    }
}