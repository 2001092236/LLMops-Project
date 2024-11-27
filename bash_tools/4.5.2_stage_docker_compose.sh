set -e

# remove info about previous runs
sudo docker-compose -f docker-compose.yaml -f rag_service/docker-compose.yaml down -v

docker-compose -f ./docker-compose.yaml -f rag_service/docker-compose.yaml build

docker-compose -f ./docker-compose.yaml -f rag_service/docker-compose.yaml up

