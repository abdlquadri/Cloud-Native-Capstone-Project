FROM ubuntu:bionic

WORKDIR .

RUN apt-get update
RUN apt-get install python3 python3-pip -y

# show python logs as they occur
ENV PYTHONUNBUFFERED=0

# download the grpc health probe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.6 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 9556

COPY . .
CMD ["python3", "adservice-v2_server.py"]
