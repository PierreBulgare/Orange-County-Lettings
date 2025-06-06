docker pull pierrebulgare/orange-county-lettings:latest
docker stop orange-county-lettings || true
docker rm orange-county-lettings || true
docker run -d --name orange-county-lettings -p 8000:8000 pierrebulgare/orange-county-lettings:latest