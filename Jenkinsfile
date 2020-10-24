
node('docker-host') {
    stage 'Pull code from Git on test'
        checkout scm

    stage 'Build new app container on test'
        def customImage = docker.build("openterprise/blue:latest", "./blue/")

    stage 'Test new app'
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

    stage 'Docker push to DockerHub repo'

        customImage.push()

        customImage.push('latest')


    stage 'Cleanup on test'
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

node('docker-host-public') {

    stage 'Run new container app on prod'
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
        
    stage 'Cleanup on prod'
        sh 'docker image prune -f'
}

