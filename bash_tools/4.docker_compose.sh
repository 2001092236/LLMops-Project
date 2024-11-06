set -e

# remove all previous dependencies
# sudo docker-compose down -v

# start docker
docker-compose build
docker-compose up
