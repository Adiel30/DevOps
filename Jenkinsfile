pipeline {
 agent any
 stages {
  stage("checkout") {
   steps {
    git "https://github.com/Adiel30/DevOps.git"
    }
   }
  stage("Python"){
      steps {
          sh 'python "Guess Game.py"'
      }
  }
 }
 }
