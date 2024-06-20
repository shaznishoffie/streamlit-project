# Streamlit Project

## Context
In this project, we are deploying a basic Streamlit application with multiple pages
on AWS. The application will show data pulled from [Open-Meteo](https://open-meteo.com/)'s
API.

## Deployment

### Create AWS EC2 instance
Create an EC2 Ubuntu instance on AWS. Since this application is lightweight, we can select
the t2 micro instance type. 

### Setting up the EC2
1. Go to security and add port 8501 to the inbound rules.
2. Connect to the instance. It should bring you to a web terminal.
3. Run the following commands to setup docker
```
sudo apt-get update -y
sudo apt-get upgrade

#Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
4. [Optional] You can run the below line to test if docker is installed
```
docker --version
```
5. Clone the repository. Replace the link below with your own.
```
git clone "https://github.com/shaznishoffie/streamlit-project.git"
```
6. Build the docker image. In the command below, I have decided to name this build 
`streamlit-project-v1` with the `latest` tag.
```
docker build -t shaznishoffie/streamlit-project-v1:latest .
```
Once done, you can check for the image by running `docker images -a`
7. Now we can start running the application's image.
```
docker run -d -p 8501:8501 shaznishoffie/streamlit-project-v1
```
Docker will start running the image and you can check using `docker ps`. You should be able
to see a process ID returned with the status

### Checking the application
Return to AWS EC2 and select the instance. Looking at the details, copy the public IP,
concatenate it with `:8501` and open it in your web browser. You should be able to view
the application.
