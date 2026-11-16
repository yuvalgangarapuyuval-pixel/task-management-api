
pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Create Artifact') {
            steps {
                sh 'tar -czf task-management-api.tar.gz app.py requirements.txt tests'
                archiveArtifacts artifacts: 'task-management-api.tar.gz'
            }
        }
    }
}
