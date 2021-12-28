# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import demo_pb2 as demo__pb2


class ProductCatalogServiceStub(object):
    """---------------Product Catalog----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListProducts = channel.unary_unary(
                '/hipstershop.ProductCatalogService/ListProducts',
                request_serializer=demo__pb2.Empty.SerializeToString,
                response_deserializer=demo__pb2.ListProductsResponse.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/hipstershop.ProductCatalogService/GetProduct',
                request_serializer=demo__pb2.GetProductRequest.SerializeToString,
                response_deserializer=demo__pb2.Product.FromString,
                )
        self.SearchProducts = channel.unary_unary(
                '/hipstershop.ProductCatalogService/SearchProducts',
                request_serializer=demo__pb2.SearchProductsRequest.SerializeToString,
                response_deserializer=demo__pb2.SearchProductsResponse.FromString,
                )


class ProductCatalogServiceServicer(object):
    """---------------Product Catalog----------------

    """

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductCatalogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=demo__pb2.Empty.FromString,
                    response_serializer=demo__pb2.ListProductsResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=demo__pb2.GetProductRequest.FromString,
                    response_serializer=demo__pb2.Product.SerializeToString,
            ),
            'SearchProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchProducts,
                    request_deserializer=demo__pb2.SearchProductsRequest.FromString,
                    response_serializer=demo__pb2.SearchProductsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.ProductCatalogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductCatalogService(object):
    """---------------Product Catalog----------------

    """

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.ProductCatalogService/ListProducts',
            demo__pb2.Empty.SerializeToString,
            demo__pb2.ListProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.ProductCatalogService/GetProduct',
            demo__pb2.GetProductRequest.SerializeToString,
            demo__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.ProductCatalogService/SearchProducts',
            demo__pb2.SearchProductsRequest.SerializeToString,
            demo__pb2.SearchProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CurrencyServiceStub(object):
    """-----------------Currency service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSupportedCurrencies = channel.unary_unary(
                '/hipstershop.CurrencyService/GetSupportedCurrencies',
                request_serializer=demo__pb2.Empty.SerializeToString,
                response_deserializer=demo__pb2.GetSupportedCurrenciesResponse.FromString,
                )
        self.Convert = channel.unary_unary(
                '/hipstershop.CurrencyService/Convert',
                request_serializer=demo__pb2.CurrencyConversionRequest.SerializeToString,
                response_deserializer=demo__pb2.Money.FromString,
                )


class CurrencyServiceServicer(object):
    """-----------------Currency service-----------------

    """

    def GetSupportedCurrencies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Convert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurrencyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSupportedCurrencies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSupportedCurrencies,
                    request_deserializer=demo__pb2.Empty.FromString,
                    response_serializer=demo__pb2.GetSupportedCurrenciesResponse.SerializeToString,
            ),
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=demo__pb2.CurrencyConversionRequest.FromString,
                    response_serializer=demo__pb2.Money.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.CurrencyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CurrencyService(object):
    """-----------------Currency service-----------------

    """

    @staticmethod
    def GetSupportedCurrencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.CurrencyService/GetSupportedCurrencies',
            demo__pb2.Empty.SerializeToString,
            demo__pb2.GetSupportedCurrenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.CurrencyService/Convert',
            demo__pb2.CurrencyConversionRequest.SerializeToString,
            demo__pb2.Money.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AdServiceStub(object):
    """------------Ad service------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAds = channel.unary_unary(
                '/hipstershop.AdService/GetAds',
                request_serializer=demo__pb2.AdRequest.SerializeToString,
                response_deserializer=demo__pb2.AdResponse.FromString,
                )


class AdServiceServicer(object):
    """------------Ad service------------------
    """

    def GetAds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAds,
                    request_deserializer=demo__pb2.AdRequest.FromString,
                    response_serializer=demo__pb2.AdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.AdService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdService(object):
    """------------Ad service------------------
    """

    @staticmethod
    def GetAds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.AdService/GetAds',
            demo__pb2.AdRequest.SerializeToString,
            demo__pb2.AdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AdServiceV2Stub(object):
    """------------Ad service Version 2------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAds = channel.unary_unary(
                '/hipstershop.AdServiceV2/GetAds',
                request_serializer=demo__pb2.AdRequestV2.SerializeToString,
                response_deserializer=demo__pb2.AdResponseV2.FromString,
                )


class AdServiceV2Servicer(object):
    """------------Ad service Version 2------------------
    """

    def GetAds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdServiceV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAds,
                    request_deserializer=demo__pb2.AdRequestV2.FromString,
                    response_serializer=demo__pb2.AdResponseV2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.AdServiceV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdServiceV2(object):
    """------------Ad service Version 2------------------
    """

    @staticmethod
    def GetAds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.AdServiceV2/GetAds',
            demo__pb2.AdRequestV2.SerializeToString,
            demo__pb2.AdResponseV2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
