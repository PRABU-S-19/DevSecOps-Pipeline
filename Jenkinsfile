pipeline {
    agent any

    stages {

        stage('Secret Scan') {
            steps {
                script {
                    def result = sh(
                        script: "grep -E 'SECRET_KEY\\s*=\\s*\".*\"' app.py || true",
                        returnStdout: true
                    )

                    if (result.trim()) {
                        error "Secret Detected in app.py"
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
