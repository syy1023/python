pipeline {
  agent {
    node {
      label 'tag1'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'encho "hello world"'
      }
    }

  }
}