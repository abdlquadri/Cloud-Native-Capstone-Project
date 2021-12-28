#!/usr/bin/python

import sys
import grpc

from protobuf import demo_pb2
from protobuf import demo_pb2_grpc

from logger import getJSONLogger
logger = getJSONLogger('adservice-v2-server')

if __name__ == "__main__":
    channel = grpc.insecure_channel("localhost:9556")
    stub = demo_pb2_grpc.AdServiceV2Stub(channel)

    item = demo_pb2.AdRequestV2()
    
    response = stub.Create(item)

    # Uncomment to log the response from the Server
    logger.info(response)
