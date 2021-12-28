#!/usr/bin/python

import os
import random
import time
import traceback
from concurrent import futures

import grpc

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

from protobuf import demo_pb2
from protobuf import demo_pb2_grpc

from logger import getJSONLogger
logger = getJSONLogger('adservice-v2-server')

channel = grpc.insecure_channel("localhost:30007")
stub = demo_pb2_grpc.ProductCatalogServiceStub(channel)

class AdServiceV2():
    
    def GetAds(self, request, context):
        product_request = {}
        product = stub.Create(product_request)
        ad_item = demo_pb2.AdV2(product.id, "AdV2 - Items with 25% discount!")
        response = demo_pb2.AdResponseV2(ad_item)
        return response


    # Uncomment to enable the HealthChecks for the Ad service
    # Note: These are needed for the liveness and readiness probes
    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)
    
    def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED)


if __name__ == "__main__":
    logger.info("initializing adservice-v2")

   # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    demo_pb2_grpc.add_AdServiceV2Servicer_to_server(AdServiceV2(), server)


    logger.info("Server starting on port 9556...")
    server.add_insecure_port("[::]:9556")
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)   

    # Uncomment to add the HealthChecks to the gRPC server to the Ad-v2 service
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
