#docker run -d -p 0.0.0.0:31338:31337 pwn100

while true;
do
docker kill pwn_100
docker rm pwn_100
docker run -d --name=pwn_100 -p 0.0.0.0:31338:31337 pwn100 
sleep 600 
done;
