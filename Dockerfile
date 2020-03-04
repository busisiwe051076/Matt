FROM python:3
MAINTAINER busisiwe zulu "busi@riot.network"
WORKDIR /home/zynq5/Desktop/EX1
COPY . /home/zynq5/Desktop/EX1
RUN pip3 install numpy
CMD python3 app.py
