🚀 DevSecOps Pipeline using Jenkins & Docker
📌 Overview

This project demonstrates a DevSecOps CI/CD pipeline that integrates security checks and automated containerization into the development lifecycle. The pipeline ensures that insecure code (e.g., hardcoded secrets) is detected early before building and deploying the application.

🎯 Objectives
Implement a CI/CD pipeline
Integrate basic secret scanning
Automate Docker image build
Demonstrate secure development workflow

🏗️ Architecture
Developer → GitHub → Jenkins Pipeline → Secret Scan → Docker Build → Container Run
🔹 Architecture Flow
Developer pushes code to GitHub
Jenkins triggers pipeline
Secret scan checks for sensitive data
If safe → Docker image build

🗂️ Project Structure
DevSecOps-Pipeline/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
└── requirements.txt

⚙️ Technologies Used
Python (Flask)
Jenkins
Docker
Git & GitHub

📅 Weekly Progress
✅ Week 1 – Setup & Environment
Installed Ubuntu in VirtualBox
Installed Git, Docker, Jenkins
Created GitHub repository

Why?
To establish a development and CI/CD environment

✅ Week 2 – Pipeline Implementation
Created Jenkins pipeline
Integrated GitHub with Jenkins
Implemented secret scanning
Built Docker image

Why?
To automate secure build process

🔐 Secret Scan Logic
Jenkinsfile Snippet
stage('Secret Scan') {
    steps {
        script {
            def result = sh(
                script: "grep -E 'SECRET_KEY\\s*=\\s*\".*\"' app.py || true",
                returnStdout: true
            )

            if (result.trim()) {
                error "Secret Detected in Code!"
            } else {
                echo "No Secrets Found"
            }
        }
    }
}

🔍 Explanation
Searches for hardcoded secrets
If found → build fails
If not → pipeline continues
🐳 Docker Configuration
Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python","app.py"]

🧪 Application Code
app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Pipeline Running Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    🔄 Pipeline Flow
Code Push → Jenkins Trigger → Secret Scan → Docker Build → Deployment Ready
▶️ Commands Used
🔹 Git Commands
git add .
git commit -m "Initial commit"
git push origin main

🔹 Jenkins Trigger
Open Jenkins dashboard
Click Build Now
Check Console Output

📊 Pipeline Results
Condition	Result
Secret present	❌ Build Failed
No secret	✅ Build Success

🧠 Key Learnings
CI/CD pipeline automation
DevSecOps integration
Docker containerization
Debugging real-world issues
Jenkins pipeline configuration

🚀 Future Improvements
Integrate SAST tools
Add dependency scanning
Implement Kubernetes deployment
Add monitoring tools (Prometheus, Grafana)

🎤 Conclusion

This project successfully demonstrates a basic DevSecOps pipeline where:

Security is integrated into CI/CD
Automated build ensures consistency
Pipeline prevents insecure code deployment
🙏 Acknowledgment

Completed as part of internship at Infotact Solutions, gaining hands-on experience in DevSecOps tools and practices.

🔗 Output

Access application:

http://localhost:5000
Container runs application

