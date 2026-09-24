pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        DATABASE_URL = 'postgresql://postgres:postgres@127.0.0.1:55432/homework30'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv .venv
                            . .venv/bin/activate
                            python -m pip install --upgrade pip
                            python -m pip install -r lesson_30/requirements.txt
                        '''
                    } else {
                        bat '''
                            py -3 -m venv .venv
                            .venv\\Scripts\\python -m pip install --upgrade pip
                            .venv\\Scripts\\python -m pip install -r lesson_30\\requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Start PostgreSQL') {
            steps {
                script {
                    env.POSTGRES_CONTAINER = "homework31-postgres-${env.BUILD_NUMBER}"

                    if (isUnix()) {
                        sh """
                            docker rm -f ${env.POSTGRES_CONTAINER} >/dev/null 2>&1 || true
                            docker run --name ${env.POSTGRES_CONTAINER} -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=homework30 -p 55432:5432 -d postgres:16-alpine
                            . .venv/bin/activate
                            python lesson_31/wait_for_postgres.py
                        """
                    } else {
                        bat """
                            docker rm -f ${env.POSTGRES_CONTAINER} >NUL 2>NUL
                            docker run --name ${env.POSTGRES_CONTAINER} -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=homework30 -p 55432:5432 -d postgres:16-alpine
                            .venv\\Scripts\\python lesson_31\\wait_for_postgres.py
                        """
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            mkdir -p test-results lesson_30/allure-results
                            PYTHONPATH="$WORKSPACE/lesson_30${PYTHONPATH:+:$PYTHONPATH}" .venv/bin/python -m pytest lesson_30/test_homework_30_1.py --junitxml=test-results/pytest-results.xml --alluredir=lesson_30/allure-results
                        '''
                    } else {
                        bat '''
                            if not exist test-results mkdir test-results
                            if not exist lesson_30\\allure-results mkdir lesson_30\\allure-results
                            set "PYTHONPATH=%WORKSPACE%\\lesson_30;%PYTHONPATH%"
                            .venv\\Scripts\\python -m pytest lesson_30\\test_homework_30_1.py --junitxml=test-results\\pytest-results.xml --alluredir=lesson_30\\allure-results
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results/*.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'test-results/*.xml, lesson_30/allure-results/**'

            script {
                mail(
                    to: 'InsertYour@Mail.Here',
                    subject: "Jenkins ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}
Status: ${currentBuild.currentResult}
Build URL: ${env.BUILD_URL}
"""
                )

                if (env.POSTGRES_CONTAINER?.trim()) {
                    if (isUnix()) {
                        sh "docker rm -f ${env.POSTGRES_CONTAINER} >/dev/null 2>&1 || true"
                    } else {
                        bat "docker rm -f ${env.POSTGRES_CONTAINER} >NUL 2>NUL || exit /b 0"
                    }
                }
            }
        }
    }
}
