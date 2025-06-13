docker stop orange-county-lettings-PROD 2>NUL
docker rm orange-county-lettings-PROD 2>NUL
docker rmi pierrebulgare/orange-county-lettings:latest 2>NUL
docker pull pierrebulgare/orange-county-lettings:latest
docker run -d --name orange-county-lettings-PROD -p 8009:8000 pierrebulgare/orange-county-lettings:latest