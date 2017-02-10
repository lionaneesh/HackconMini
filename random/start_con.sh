while true;
do
docker kill random
docker rm random
docker run -d --name=random -p 0.0.0.0:31339:31337 random 
sleep 600 
done;
