# Start with CUDA Caffe dependencies
# i need to change this to 32 bit 
# isnt that kernel level ?
# what?
# okay
# I will just ibstall the same packages

FROM  ubuntu:trusty
MAINTAINER AAA


# installing SSH :-

RUN apt-get update
RUN apt-get install -y ucspi-tcp
RUN echo 'root:root' |chpasswd
RUN sudo dpkg --add-architecture i386
RUN sudo apt-get update
RUN sudo apt-get install -y libc6:i386

RUN adduser noob
COPY * /
RUN su noob
# WORKDIR /

EXPOSE 31337

RUN chmod +x /start.sh
# RUN chsh -s /start.sh


#CMD ["python" , "main.py"]

CMD bash /start.sh
