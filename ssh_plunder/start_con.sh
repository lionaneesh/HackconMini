while true;
do
docker kill ssh_plunder
docker rm ssh_plunder
docker run -d --name=ssh_plunder -p 0.0.0.0:10022:22 ssh_plunder
sleep 600 
done;
