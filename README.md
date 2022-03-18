# docker_apps
Dockerized Nginx, PostgreSQL &amp; portfolio apps

This repository is a collection of dockerized resources working together to host a number of Django and Flask applications. 
It uses Nginx (nginx:1.21-alpine) to handle requests and to pass them to the corresponding application via gunicorn. 
It also uses python:3.9.6-alpine as the base image for each application container. Finally, it uses PostgreSQL (postgres:13.0-alpine) 
to store each application’s data. 

When testing, I used an AWS Ubuntu 18 LTS instance, but it will work in any environment where docker & docker-compose 
have been installed. 

I created a DNS A record for each application which pointed to the AWS instance I worked on. Then, I used the fully qualified
domain name (FQDN) in each of the nginx configuration files to ensure the applications were accessible to me when running the containers. 

This repository can be cloned but please note that a couple of changes need to me made in order for the applications to be accessible
to you: 

- create new DNS A records to point to your instance (Linux,Windows,Mac) with docker installed 
- modify each file in nginx/*.conf to reflect the changed DNS A records 

Once, you’ve made the necessary changes, change into the cloned repository’s directory and issue: 

docker-compose up -d --build  

Now, the applications will be available to you at the FQDNs you specified. 
