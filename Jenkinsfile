pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/prashantsharma2608/second.git']]])
      }
    }

    stage('Test') {
      steps {
        sh 'python -m pip install selenium'
        sh 'python -m pip install pytest'
        sh 'python C:\Users\prashantsharma\PycharmProjects\selenium\second\test1.py'
      }
    }
  }
}
