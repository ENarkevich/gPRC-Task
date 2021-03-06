# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class CroppImageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.cropp = channel.unary_unary(
        '/CroppImage/cropp',
        request_serializer=data__pb2.InputImage.SerializeToString,
        response_deserializer=data__pb2.ImageParts.FromString,
        )


class CroppImageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def cropp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CroppImageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'cropp': grpc.unary_unary_rpc_method_handler(
          servicer.cropp,
          request_deserializer=data__pb2.InputImage.FromString,
          response_serializer=data__pb2.ImageParts.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CroppImage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ConcatenateImageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.concatenate = channel.unary_unary(
        '/ConcatenateImage/concatenate',
        request_serializer=data__pb2.ImageParts.SerializeToString,
        response_deserializer=data__pb2.ImageResult.FromString,
        )


class ConcatenateImageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def concatenate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConcatenateImageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'concatenate': grpc.unary_unary_rpc_method_handler(
          servicer.concatenate,
          request_deserializer=data__pb2.ImageParts.FromString,
          response_serializer=data__pb2.ImageResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ConcatenateImage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
