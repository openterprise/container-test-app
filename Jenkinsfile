
properties(
    [
        parameters(
            [choice(name: 'color',
            choices: "blue\ngreen\nred\nyellow\norange\nbrown\npurple",
            description: 'Passing the color')]
        ),
        pipelineTriggers([cron('0 23 * * *')])
    ])

node('docker-host') {
    stage '[test] pull code from GitHub'
        checkout scm
        echo "${params.color}"

    stage '[test] build container'
        def customImage = docker.build("openterprise/${params.color}:latest", "./${params.color}/")

    stage '[test] run container'
        try {
            sh 'docker stop `docker ps | grep 8000 | awk \'{print $1}\'`'
        } catch (err) {
            echo "There was no running old test container, nothing to stop"
        }
        try {
            sh "docker rm app_${params.color}"
        } catch (err) {
            echo "There was no old test container, nothing to remove"
        }
        sh "docker run -d -p 8000:5000 --name app_${params.color} openterprise/${params.color}:latest"
        sleep 2
        sh 'curl --connect-timeout 3 http://docker-host:8000'

    stage '[test] push container to DockerHub'
        customImage.push()
        customImage.push('latest')

    stage '[test] cleanup'
        try {
            sh 'docker stop `docker ps | grep 8000 | awk \'{print $1}\'`'
        } catch (err) {
            echo "There was no running old test container, nothing to stop"
        }
        try {
            sh "docker rm app_${params.color}"
        } catch (err) {
            echo "There was no old test container, nothing to remove"
        }
        sh 'docker container prune -f'
        sh 'docker image prune -f'
}

node('docker-host-public') {
    stage '[prod] pull cointainer'
        sh "docker pull openterprise/${params.color}:latest"

    stage '[prod] run container'
        try {
            sh 'docker stop `docker ps | grep 8000 | awk \'{print $1}\'`'
        } catch (err) {
            echo "There was no running old container, nothing to stop"
        }
        try {
            sh "docker rm app_${params.color}"
        } catch (err) {
            echo "There was no old container, nothing to remove"
        }
        sh "docker run -d -p 8000:5000 --name app_${params.color} openterprise/${params.color}:latest"
        sleep 2
        sh 'curl --connect-timeout 3 http://docker.openterprise.it:8000'

    stage '[prod] cleanup'
        sh 'docker container prune -f'
        sh 'docker image prune -f'
}
