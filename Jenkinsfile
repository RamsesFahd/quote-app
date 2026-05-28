pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'pytest'
            }
        }
        stage('Package') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t quote-app .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                bat 'docker rm -f quote-app-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name quote-app-container quote-app'
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed — deployment stopped to protect the app.'
        }
        success {
            echo 'Success! App is live at http://localhost:5000'
        }
    }
}