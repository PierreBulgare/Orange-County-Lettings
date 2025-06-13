docker pull pierrebulgare/orange-county-lettings:dev
docker stop orange-county-lettings-DEV
docker rm orange-county-lettings-DEV
docker run -d --name orange-county-lettings-DEV -p 8000:8000 pierrebulgare/orange-county-lettings:dev
