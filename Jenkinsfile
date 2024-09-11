pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/eyadellai1/swm_exam-'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest --cov=src tests/test_ldexp.py --cov-report=term --cov-report=html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/htmlcov/index.html', allowEmptyArchive: true
        }
    }
}
