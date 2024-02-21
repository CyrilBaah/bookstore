pipeline {
    agent any

    environment {
        VENV_ACTIVATE = 'venv/bin/activate'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh "source ${VENV_ACTIVATE} && pip install --upgrade pip && pip install -r requirements.txt"
            }
        }

        stage('Static Analysis') {
            parallel {
                stage('Flake8') {
                    steps {
                        sh 'flake8 .'
                    }
                }
                stage('Black') {
                    steps {
                        sh 'black --check .'
                    }
                }
                stage('isort') {
                    steps {
                        sh 'isort --check-only .'
                    }
                }
            }
        }

        stage('Deploy to Dev') {
            steps {
                // TODO
                sh "echo done"
            }
        }
    }

    post {
        always {
            sh 'deactivate'
            sh "rm ${VENV_ACTIVATE}"
            cleanWs()
        }

        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
