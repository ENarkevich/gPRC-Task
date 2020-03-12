import cv2
import numpy as np
import base64
import os 

class ImageChanges():

    @classmethod
    def cropp_image(self, path, part_number):
        if (not(os.path.exists(path))):
            return 'File not found', 0, 0, False
        image = cv2.imread(path)
        parts, ratio_x, ratio_y = self.__crop_file(image, part_number)
        # if number of parts is unreal
        if (parts==None):
            return 'Impossible to cropp to this number of parts', 0, 0, False 
        # encode data
        encodeparts = []
        for i in range(part_number):
            encodeparts.append(base64.b64encode(cv2.imencode('.jpg', parts[i])[1]).decode())
        return encodeparts, ratio_x, ratio_y, True

    @classmethod
    def concatenate_images(self, ratio_x, ratio_y, parts):
        decodeparts = []
        # decode from bytes
        for part in parts:
            pict = base64.b64decode(part)
            decodeparts.append(cv2.imdecode(np.frombuffer(pict, dtype=np.uint8), flags=1))
        all_picture=np.array([])
        # concatenate horizontal lines to picture
        for i in range(ratio_y):
            frame = decodeparts.pop()
        # concatenate parts to horizontal lines
            for j in range(ratio_x-1):
                frame = np.concatenate((decodeparts.pop(), frame), axis=1)
            if (i>0):
                all_picture = np.concatenate((frame, all_picture), axis=0)
            else:
                all_picture = frame
        all_picture = cv2.bitwise_not(all_picture)
        responce_data={}
        # encode data to bytes
        all_picture = base64.b64encode(cv2.imencode('.jpg', all_picture)[1]).decode() 
        return all_picture

    def __crop_file(image, number_parts):
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
        if(ratio_x>width or ratio_y>height or ratio_x<1 or ratio_y<1):
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
        return parts, ratio_x, ratio_y