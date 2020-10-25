
pipeline {

agent { node { label 'docker-host' } }  
parameters {
    choice(
      name: 'color',
      choices: "blue\ngreen\nred\nyellow",
      description: 'Passing the color'
    )
  }

stages {

    stage ('[test] pull code from GitHub') {
        steps {
        checkout scm
        echo "${params.color}" 
        }
    }

    stage ('[test] build container') {
        steps {
            def customImage = docker.build("openterprise/blue:latest", "./blue/")
        }
        
    }  

    stage '[test] run container'
        try {
            sh 'docker stop app_blue'
        } catch (err) {
            echo "There was no running old test container, nothing to stop"
        }
        try {
            sh 'docker rm app_blue'
        } catch (err) {
            echo "There was no old test container, nothing to remove"
        }
        sh 'docker run -d -p 8000:5000 --name app_blue openterprise/blue:latest'
        sleep 2
        sh 'curl --connect-timeout 3 http://docker-host:8000'

    stage '[test] push container to DockerHub'
        customImage.push()
        customImage.push('latest')

    stage '[test] cleanup'
        try {
            sh 'docker stop app_blue'
        } catch (err) {
            echo "There was no running old test container, nothing to stop"
        }
        try {
            sh 'docker rm app_blue'
        } catch (err) {
            echo "There was no old test container, nothing to remove"
        }
        sh 'docker image prune -f'
}

agent('docker-host-public') {
    stage '[prod] run container'
        try {
            sh 'docker stop app_blue'
        } catch (err) {
            echo "There was no running old container, nothing to stop"
        }
        try {
            sh 'docker rm app_blue'
        } catch (err) {
            echo "There was no old container, nothing to remove"
        }
        sh 'docker run -d -p 8000:5000 --name app_blue openterprise/blue:latest'
        sleep 2
        sh 'curl --connect-timeout 3 http://docker.openterprise.it:8000'
        
    stage '[prod] cleanup'
        sh 'docker image prune -f'
}

}
