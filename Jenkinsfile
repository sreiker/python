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
     stage('builName') {
      steps {
        // This block will be executed for all build results
        script {
          // Add the script to update LambdaTest build name here
          LT_USERNAME = "username"
          LT_ACCESS_KEY = "accesskey"
          LT_BUILD_NAME = "Jenkins Build ${BUILD_NUMBER}"
          LT_API_ENDPOINT = "https://api.lambdatest.com/api/v1/builds/${LT_USERNAME}"

          bat "curl -X PUT -u ${LT_USERNAME}:${LT_ACCESS_KEY} -H 'Content-Type: application/json' -d '{\"build\": \"${LT_BUILD_NAME}\"}' ${LT_API_ENDPOINT}"
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
  }
  }
