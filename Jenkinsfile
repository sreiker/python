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

    stage('Enviournment'){
      environment {
     env.PATH = env.PATH + ";c:\\Windows\\System32"
 }
    }

    stage('Test') {
      steps {
        bat 'python -m pip install selenium'
        bat 'python -m pip install pytest'
        bat 'python C://Users//prashantsharma//PycharmProjects//selenium//second//test1.py'
      }
    }
  }
}
