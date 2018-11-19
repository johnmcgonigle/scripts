############################################################
# Ubuntu base image
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

# Install OpenJDK 7 JRE
RUN apt-get update && apt-get install --yes \
    openjdk-7-jre \
    perl \
    unzip

ENV version=0.11.5

# Download FastQC
ADD http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${version}.zip /tmp/

# Install FastQC
RUN cd /usr/local && \
    unzip /tmp/fastqc_*.zip && \
    chmod 755 /usr/local/FastQC/fastqc && \
    nln -s /usr/local/FastQC/fastqc /usr/local/bin/fastqc && \
    rm -rf /tmp/fastqc_*.zip
