import cv2
from Constants import CameraConstants


class CameraManager:
    __current_camera = None
    __camera_id = None
    __cameras = {}

    def __init__(self, cams):
        for c in cams:
            self.__cameras[c] = cv2.VideoCapture(cams[c])

    def change_camera(self, camera_port):
        if camera_port in self.__cameras:
            self.__current_camera = self.__cameras[camera_port]
        else:
            raise KeyError("camera does not exist!")

    def read_frame(self):
        return self.cam.read()

    def get_camera_id(self):
        return self.camera_id


