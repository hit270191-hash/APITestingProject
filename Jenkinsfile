pipeline {
    agent any

    stages {

        stage('Verify Workspace') {
            steps {
                bat 'dir'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'run.bat'
            }
        }

        stage('List Allure Results') {
            steps {
                bat 'dir allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'reports/report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Build completed successfully'
        }

        failure {
            echo 'Build failed'
        }
    }
}