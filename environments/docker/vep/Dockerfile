### docker container for ensembl-vep
FROM ubuntu:16.04

ENV VEP_VERSION 90
ENV OPT /opt/vep

WORKDIR $OPT
RUN apt update -y && apt upgrade -y && apt install git cpanminus \
build-essential mysql-client curl libssl-dev wget openssl libmysqlclient-dev unzip wget -y \
&& cpanm -n install DBI DBD::mysql Set::IntervalTree JSON PerlIO::gzip Bio::Root::Version \

RUN git clone https://github.com/Ensembl/ensembl-vep.git \
&& cd ensembl-vep && git checkout release/$VEP_VERSION \
&& perl INSTALL.pl --NO_TEST --NO_UPDATE --AUTO a \
&& apt autoclean -y &&  apt autoremove -y



