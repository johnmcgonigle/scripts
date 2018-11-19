############################################################
# Ubunt base image
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04
LABEL \
  version="1.9" \
  description="bcftools image for use in Workflows"

RUN apt-get update && apt-get install -y \
  libbz2-dev \
  liblzma-dev \
  xz-utils \
  automake \
  autoconf \
  g++ \
  make \
  ncurses-dev \
  wget \
  zlib1g-dev

ENV version=1.9
ENV BCFTOOLS_INSTALL_DIR=/opt/bcftools-${version}

RUN mkdir $BCFTOOLS_INSTALL_DIR

WORKDIR /opt/
RUN wget https://github.com/samtools/bcftools/releases/download/${version}/bcftools-${version}.tar.bz2 && \
  tar --bzip2 -xf bcftools-${version}.tar.bz2

WORKDIR $BCFTOOLS_INSTALL_DIR
RUN make clean-all && make distclean
RUN ./configure

RUN make prefix=$BCFTOOLS_INSTALL_DIR

WORKDIR /
RUN ln -s $BCFTOOLS_INSTALL_DIR/bcftools /usr/bin/bcftools

