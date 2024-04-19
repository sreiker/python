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
                  userRemoteConfigs: [[url: 'https://github.com/prashantsharma2608/second.git']]])
      }
    }

    stage('Test') {
      steps {
        bat 'python -m pip install selenium'
        bat 'python -m pip install pytest'
        bat 'python -m pip install pytz'
        bat 'python /Users/sakshamagarwal/Downloads/v3withCaps.py --builds 3 --parallel 3 --error_commands 3 --username lambdatestdemo --access_key 0H7V3MMGoZeafPIJTySEvJR5V4hKuWsJXtGOJ2cuT96YLt7jhu --env prod --test_name "Sample Flaky Test" --build_name "Sample Flaky Build 2"'
      }
    }
  }
  }
