pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'lunidep-pythonapp-image'
        DOCKER_PORT = '8081'
    }

    stages {
        stage('Clone src from GitHub') {
            steps {
                sh 'pwd'
                git credentialsId: 'github-ssh-key', url: 'git@github.com:Lunidep/python-project.git', branch: 'main'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 manage.py test'
            }
        }
        stage('Build docker container') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Check and Free Port ${DOCKER_PORT}') {
            steps {
                script {
                    // есть ли работающий контейнер на порту 8081
                    def containerId = sh(script: "docker ps -q --filter 'publish=${DOCKER_PORT}'", returnStdout: true).trim()
                    if (containerId) {
                        echo "Port ${DOCKER_PORT} is in use by container ${containerId}. Stopping it..."
                        sh "docker stop ${containerId}"
                        sh "docker rm ${containerId}"
                        echo "Container ${containerId} has been stopped and removed."
                    } else {
                        echo "Port ${DOCKER_PORT} is free."
                    }
                }
            }
        }
        stage('Run app') {
            steps {
                script {
                    sh 'docker run -d -p ${DOCKER_PORT}:8000 ${DOCKER_IMAGE}'
                }
            }
        }
        stage('Run PostgreSQL') {
            steps {
                script {
                    // существует ли контейнер PostgreSQL
                    def postgresContainerId = sh(script: "docker ps -q --filter 'name=postgres-db'", returnStdout: true).trim()
                    if (!postgresContainerId) {
                        echo "Starting PostgreSQL container..."
                        sh '''
                            docker run -d \
                            --name postgres-db \
                            -e POSTGRES_USER=admin \
                            -e POSTGRES_PASSWORD=admin \
                            -e POSTGRES_DB=default \
                            -p 5432:5432 \
                            postgres:latest
                        '''
                    } else {
                        echo "PostgreSQL container is already running with ID ${postgresContainerId}."
                    }
                }
            }
        }
    }
}
