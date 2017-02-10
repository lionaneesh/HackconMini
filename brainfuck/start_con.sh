#docker run -d -p 0.0.0.0:10300:3000 brainfuck


while true;
do
docker kill brainfuck
docker rm  brainfuck
docker run -d --name=brainfuck -p 0.0.0.0:10300:3000 brainfuck 
sleep 600 
done;
