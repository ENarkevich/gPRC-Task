import grpc
from concurrent import futures
import time
import cv2
import numpy as np
import base64
import os 
import logging

import data_pb2
import data_pb2_grpc


def crop_file(image, number_parts):
    height, width, _ = image.shape
    parts = []
    ratio = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    # search for X-proportion
    ratio_x = [i for i in ratio if number_parts%i==0]     
    ratio_x = ratio_x[-1]
    # Y-proportion for cropp
    ratio_y = int(number_parts/ratio_x)
    if (height>width and ratio_x>ratio_y):  
        ratio_x, ratio_y = ratio_y, ratio_x
    # if number of parts is unreal
    if(ratio_x>width or ratio_y>height):
        return None, None, None
    # shift for new points
    x_offset, y_offset = int(width/ratio_x), int(height/ratio_y)  
    x1, y1 = 0, 0     
    x2, y2 = x_offset, y_offset   
    # cropp picture
    for i in range(ratio_y):
        for j in range(ratio_x): 
            parts.append(image[y1:y2,x1:x2])  
            x1 = x1 + x_offset
            x2 = x2 + x_offset
            if (j==ratio_x-1):
                x2 =  width
        y1 = y1 + y_offset
        y2 = y2 + y_offset
        if(i==ratio_y-1):
            y2 = height
        x1, x2 = 0, x_offset  
    return parts, ratio_y, ratio_x

class CroppImageServicer(data_pb2_grpc.CroppImageServicer):
    def cropp(self, request, context):
        if (not(os.path.exists(f["path_file"]))):
            context.set_details('cart_not_found')
            return context
        image = cv2.imread(request.path)
        # add if number of parts is unreal
        parts, ratio_x, ratio_y = crop_file(image, request.part_number)
        """if (parts==None):
            return """
        responce_data = []
        for i in range(request.part_number):
            responce_data.append(base64.b64encode(cv2.imencode('.jpg', parts[i])[1]).decode())
        return data_pb2.ImageParts(ratio_x=ratio_x, ratio_y=ratio_y, parts=bytes(12))

class ConcatenateImageServicer(data_pb2_grpc.ConcatenateImageServicer):
    def concatenate(self, request, context):
        ratio_x = request.ratio_x
        ratio_y = request.ratio_y
        parts = []
        reqparts = request.parts
        # decode from bytes
        for part in reqparts:
            pict = base64.b64decode(part)
            parts.append(cv2.imdecode(np.frombuffer(pict, dtype=np.uint8), flags=1))
        all_picture=np.array([])
        # concatenate horizontal lines to picture
        for i in range(ratio_y):
            frame = parts.pop()
        # concatenate parts to horizontal lines
            for j in range(ratio_x-1):
                frame = np.concatenate((parts.pop(), frame), axis=1)
            if (i>0):
                all_picture = np.concatenate((frame, all_picture), axis=0)
            else:
                all_picture = frame
        all_picture = cv2.bitwise_not(all_picture)
        responce_data={}
        # encode data to bytes
        all_picture = base64.b64encode(cv2.imencode('.jpg', all_picture)[1]).decode() 
        return data_pb2_grpc.ImageResult(result_image=all_picture)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    data_pb2_grpc.add_CroppImageServicer_to_server(CroppImageServicer(), server)
    data_pb2_grpc.add_ConcatenateImageServicer_to_server(ConcatenateImageServicer(), server)

    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    #logging.DEBUG
    serve()
