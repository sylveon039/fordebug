# Ubuntu Linux as the base image
FROM ubuntu:16.04

# Install the packages
RUN apt-get update -y && \
    apt-get install -y python-pip && \
    pip install requests && \
    pip install tensorflow && \
    pip install pillow && \
    pip install flask

# Open the following ports
EXPOSE 5000

# Add the files
ADD ./666.tar /
# Define the command which runs when the container starts
CMD ["cd / && python Handwriting\ Recognition.py && while true; do echo hello world; sleep 1000; done"]

# Use bash as the container's entry point
ENTRYPOINT ["/bin/bash", "-c"]
