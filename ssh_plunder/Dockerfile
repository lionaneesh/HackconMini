# Start with CUDA Caffe dependencies
FROM  ubuntu:trusty
MAINTAINER Divam Gupta <ddivamgupta@gmail.com>


# installing SSH :-

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:toor' |chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config


RUN apt-get update && \
	apt-get install -y make g++ python  python-pip

#RUN  pip install curses

COPY * ./

EXPOSE 22

RUN chmod +x /start.sh
RUN chsh -s /start.sh


#CMD ["python" , "main.py"]

CMD  /usr/sbin/sshd -D
