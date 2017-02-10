FROM ubuntu:trusty

# Install Dependencies :
RUN apt-get update && \
	apt-get install -y make g++ python git curl software-properties-common phantomjs && \
	add-apt-repository ppa:eugenesan/ppa && \
	apt-get update && \
	apt-get install -y php5

# Setup the workspace
RUN  mkdir xss-sessionhijack-challenge 
WORKDIR xss-sessionhijack-challenge 

# Copy all the files
COPY * ./

EXPOSE 8000

# Run the services
CMD ["bash" , "startup.sh" ]
