pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/prashantsharma2608/second.git'
      }
    }

    stage('Test') {
      steps {
        sh 'python test1.py'
      }
    }
  }
}
