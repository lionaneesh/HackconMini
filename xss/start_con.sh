while true;
do
docker kill xss
docker rm xss
docker run -d --name=xss -p 0.0.0.0:18000:8000 xss 
sleep 600 
done;
