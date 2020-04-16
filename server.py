import grpc
from concurrent import futures
import logging
import data_pb2
import data_pb2_grpc
from classes import ImageChanges

class CroppImageServicer(data_pb2_grpc.CroppImageServicer):
    def cropp(self, request, context):
        resp = data_pb2.ImageParts()
        parts, resp.ratio_x, resp.ratio_y, resp.flag = ImageChanges.cropp_image(request.path, request.part_number)
        resp.parts.extend(parts)
        return resp

class ConcatenateImageServicer(data_pb2_grpc.ConcatenateImageServicer):
    def concatenate(self, request, context):
        resp = data_pb2.ImageResult()
        resp.result_image = ImageChanges.concatenate_images(request.ratio_x, request.ratio_y, request.parts)
        return resp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    data_pb2_grpc.add_CroppImageServicer_to_server(CroppImageServicer(), server)
    data_pb2_grpc.add_ConcatenateImageServicer_to_server(ConcatenateImageServicer(), server)

    server.add_insecure_port('0.0.0.0:5000')
    server.start()
    try:
        while True:
            server.wait_for_termination(timeout=3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
