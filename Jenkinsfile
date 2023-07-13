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
        bat 'C:\Users\prashantsharma\AppData\Local\Programs\Python\Python310\python.exe -m pip install selenium'
        bat 'C:\Users\prashantsharma\AppData\Local\Programs\Python\Python310\python.exe -m pip install pytest'
        bat 'C:\Users\prashantsharma\AppData\Local\Programs\Python\Python310\python.exe test1.py'
      }
    }
  }
}
