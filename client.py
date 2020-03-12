import grpc
import data_pb2
import data_pb2_grpc
import cv2
import numpy as np
import base64
from config import CLIENT_FOLDER

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:5000')

    stub1 = data_pb2_grpc.CroppImageStub(channel)
    stub2 = data_pb2_grpc.ConcatenateImageStub(channel)
    input_data = data_pb2.InputImage(path=f'{CLIENT_FOLDER}pict.jpg', part_number=42)
    # request for cropp
    responce = stub1.cropp(input_data)
    if (responce.flag):
        # request for concatenate 
        from_conc = stub2.concatenate(responce)
        pict = base64.b64decode(from_conc.result_image)
        decoded = cv2.imdecode(np.frombuffer(pict, dtype=np.uint8), flags=1)
        cv2.imwrite(f'{CLIENT_FOLDER}result.jpg', decoded)
    else:
        print(responce.parts)


