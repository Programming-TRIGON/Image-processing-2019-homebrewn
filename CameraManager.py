import cv2


class CameraManager:
    __current_camera = None  # here we will put the first camera that will capture frames at the beginning of the match
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
        return self.__current_camera.read()
