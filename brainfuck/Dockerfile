FROM  node:latest

RUN cd / &&  npm install brainfuck-javascript && npm install md5 && npm install express

COPY bf.js ./
COPY startup.sh ./

# it'll be interesting to see  

EXPOSE 3000

 
CMD ["bash" , "startup.sh" ]

