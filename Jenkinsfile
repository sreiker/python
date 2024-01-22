pipeline {
  agent any

  stages {
    stage('Job name') {
            steps {
                script {
                    // Store the Jenkins job name in a variable
                    def myJobName = env.JOB_NAME

                    // Now you can use 'myJobName' for further processing
                    echo "Current Jenkins job name is: ${myJobName}"
                }
            }
        }
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/prashantsharma2608/second.git']]])
      }
    }

    stage('Test') {
      steps {
        bat 'python -m pip install selenium'
        bat 'python -m pip install pytest'
        bat 'python test1.py'
      }
    }
    stage('Report'){
      steps{
        lambdaTestReportPublisher 'app-automation'
      }
    }
  }
}
