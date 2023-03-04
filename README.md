# Nginx RTMP Server
Its a Template Repository For creating RTMP server with nginx

Docker compose has 2 services one is a Nginx server which creates a RTMP server and another one is a simple Flask app to manage authentication
check the diagram below
<img width="1920" alt="Untitled" src="https://user-images.githubusercontent.com/47270636/222917086-2e5d02fc-b49a-4b20-b738-0e8a390a7a69.png">
Check the nginx/nginx.conf to change:
- video save location
- url of server
- and other parameters

use docker-compose to make docker image

