
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    environment {
        DEPLOY_DIR = '/opt/student-management-system'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Deployment') {
            steps {
                sh '''
                    set -eu

                    test -f "$WORKSPACE/docker-compose.yml"
                    test -f "$WORKSPACE/backend/Dockerfile"
                    test -f "$WORKSPACE/frontend/react-learning/Dockerfile"
                    test -f "$WORKSPACE/nginx/default.conf"
                    test -r "$DEPLOY_DIR/.env"

                    rsync -a \
                      --exclude='.git/' \
                      --exclude='.env' \
                      "$WORKSPACE/" "$DEPLOY_DIR/"

                    cd "$DEPLOY_DIR"
                    docker compose config -q
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                    set -eu
                    cd "$DEPLOY_DIR"
                    docker compose build
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    set -eu
                    cd "$DEPLOY_DIR"
                    docker compose up -d --remove-orphans
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    set -eu
                    cd "$DEPLOY_DIR"

                    for i in $(seq 1 30); do
                        if curl -fsS http://localhost/api/health; then
                            echo
                            echo "Deployment successful"
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
            sh '''
                if [ -f "$DEPLOY_DIR/docker-compose.yml" ]; then
                    cd "$DEPLOY_DIR"
                    docker compose ps || true
                fi
            '''
        }
    }
}
