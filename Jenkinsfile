node {
    stage('Build') {
        
        checkout scm
        updateGitlabCommitStatus name: 'Build', state: 'pending'

        // Harbor
        docker.withRegistry("http://192.168.0.137:9002", "f7a40b45-282e-41c7-ba25-fc1cbfa9f96e") {
            echo "====++++${env.BUILD_ID}++++===="
            def customImage = docker.build("distributed/aiot-api-new")
            customImage.push("v${env.BUILD_ID}")
            customImage.push("latest")
        }

        updateGitlabCommitStatus name: 'Build', state: 'success'
    }
    stage('Test') {
    //
    }
    stage('Deploy') {
    //
    }
}
