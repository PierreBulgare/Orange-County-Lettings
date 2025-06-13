docker pull pierrebulgare/orange-county-lettings:latest
docker stop orange-county-lettings-PROD
docker rm orange-county-lettings-PROD
docker run -d --name orange-county-lettings-PROD -p 8000:8000 pierrebulgare/orange-county-lettings:latest
