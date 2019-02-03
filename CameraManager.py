import cv2
from Constants import CameraConstants


class CameraManager:
    cam = None
    camera_id = None

    def __init__(self, camera_id):
        for port in CameraConstants.port_matrix:
            cv2.VideoCapture(port).open()  # opening all cameras
        self.cam = cv2.VideoCapture(CameraConstants.port_matrix[camera_id])
        self.camera_id = camera_id

    def change_camera(self, camera_id):
        self.cam = cv2.VideoCapture(CameraConstants.port_matrix[camera_id])

    def read_frame(self):
        return self.cam.read()

    def get_camera_id(self):
        return self.camera_id
