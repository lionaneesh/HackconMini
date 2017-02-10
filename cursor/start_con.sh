#docker run -d -p 0.0.0.0:10080:80 cursor

while true;
do
docker kill cursor
docker rm cursor
docker run -d --name=cursor -p 0.0.0.0:10080:80 cursor
sleep 600 
done;
