pipeline {
    agent any

    stages {

        stage('Secret Scan') {
            steps {
                script {
                    def result = sh(script: "grep -r 'SECRET_KEY' . || true", returnStdout: true)

                    if (result.trim()) {
                        error "Secret Detected in Code!"
                    } else {
                        echo "No Secrets Found"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-app .'
            }
        }

    }
}
