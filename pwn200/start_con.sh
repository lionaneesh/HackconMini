while true;
do
docker kill pwn_200
docker rm pwn_200
docker run -d --name=pwn_200 -p 0.0.0.0:31337:31337 pwn200 
sleep 600 
done;
