docker stop orange-county-lettings-DEV 2>NUL
docker rm orange-county-lettings-DEV 2>NUL
docker rmi pierrebulgare/orange-county-lettings:dev 2>NUL
docker pull pierrebulgare/orange-county-lettings:dev
docker run -d --name orange-county-lettings-DEV -p 8000:8000 pierrebulgare/orange-county-lettings:dev