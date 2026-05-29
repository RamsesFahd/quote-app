pipeline {
    agent any

    environment {
        APP_NAME  = 'quote-app'
        PORT      = '5000'
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Build') {
            steps {
                echo "Installing dependencies for ${APP_NAME}..."
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests with pytest...'
                bat 'python -m pytest test_app.py -v'
            }
            post {
                failure {
                    echo 'Tests failed — pipeline stopped. Fix tests before deploying.'
                }
            }
        }

        stage('Package') {
            steps {
                echo "Building Docker image: ${APP_NAME}:${IMAGE_TAG}"
                bat "docker build -t ${APP_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying ${APP_NAME} on port ${PORT}..."
                bat "docker rm -f ${APP_NAME}-container || exit 0"
                bat "docker run -d -p ${PORT}:${PORT} --name ${APP_NAME}-container ${APP_NAME}:${IMAGE_TAG}"
                echo "App deployed successfully at http://localhost:${PORT}"
            }
        }

    }

    post {
        success {
            echo "Pipeline complete. ${APP_NAME} is live at http://localhost:${PORT}"
        }
        failure {
            echo "Pipeline failed. Check the logs above for details."
        }
        always {
            echo "Pipeline finished. Status: ${currentBuild.currentResult}"
        }
    }
}
