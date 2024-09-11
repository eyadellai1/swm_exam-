pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://your-repo-url.git'
            }
        }
        stage('Install Python') {
            steps {
                sh 'apt-get update && apt-get install -y python3'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/test_ldexp.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'coverage-report.txt', allowEmptyArchive: true
        }
    }
}
