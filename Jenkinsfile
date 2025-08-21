pipeline {
  agent any

  stages {
    stage('buildNumber') {
            steps {
                script {
                    // Store the Jenkins build number in a variable
                    def myBuildNumber = env.BUILD_NUMBER

                    // Now you can use 'myBuildNumber' for further processing
                    echo "Current build number is: ${myBuildNumber}"
                }
            }
        }
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/sreiker/python']]])
      }
    }

    stage('Test') {
      steps {
        sh 'python -m pip install selenium'
        sh 'python -m pip install pytest'
        sh 'python test1.py'
      }
    }
    stage('Report'){
    steps{
      lambdaTestReportPublisher 'automation'
    }
    }
  }
  }
