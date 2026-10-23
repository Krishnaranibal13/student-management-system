pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Configuration') {
            steps {
                sh '''
                    set -eu
                    test -f docker-compose.yml
                    test -f .env
                    test -f backend/Dockerfile
                    test -f frontend/react-learning/Dockerfile
                    test -f nginx/default.conf
                    docker compose config -q
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d --remove-orphans'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    set -eu
                    for i in $(seq 1 30); do
                        if curl -fsS http://localhost/api/health >/dev/null; then
                            echo "Application and database are healthy"
                            exit 0
                        fi
                        sleep 2
                    done

                    docker compose ps
                    docker compose logs --tail=100
                    exit 1
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose ps || true'
        }
    }
}
