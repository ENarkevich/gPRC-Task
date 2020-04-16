import requests
import cv2
import numpy as np
import base64
import json
from config import CLIENT_FOLDER, SERV

if __name__ == "__main__":
    parts_number = 42
    request_data = {}
    #request fot cropp
    request_data["part_number"] = parts_number
    request_data["path"] = f'{CLIENT_FOLDER}pict.jpg'
    responce_parts = requests.post(f'{SERV}cropp', json=request_data)  
    parts = responce_parts.json()
    if (responce_parts.status_code==200):
        # request for concatenate 
        from_conc = requests.post(f'{SERV}concatenate', json=parts)
        # decode result from json 
        from_conc = from_conc.json()
        pict = base64.b64decode(from_conc["result_image"])
        decoded = cv2.imdecode(np.frombuffer(pict, dtype=np.uint8), flags=1)
        cv2.imwrite(f'{CLIENT_FOLDER}result.jpg', decoded)
    else:
        print(parts["parts"])
