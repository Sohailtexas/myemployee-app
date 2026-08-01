
Official:
https://www.jenkins.io/doc/book/installing/linux/


sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins

sudo systemctl start jenkins
sudo systemctl enable jenkins

sudo systemctl status jenkins

## Initial Password

sudo cat /var/lib/jenkins/secrets/initialAdminPassword





## to build docker file 

sudo usermod -aG docker jenkins
sudo systemctl restart jenkins



## code

pipeline {
    agent any 

    environment {
        IMAGE_NAME = "sammu.azurecr.io/myemployee:v1"
    }  
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'acr-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login sammu.azurecr.io -u $USER --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }        
    }
}
         
