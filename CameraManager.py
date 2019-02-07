import cv2


class CameraManager:

    def __init__(self, cameras_ports):
        """
        constructs new cameras manager and initialize its cameras list
        :param cameras_ports: a dictionary of cameras ports
        """
        self._target_to_port_dic = cameras_ports
        self._current_target = None
        self.__current_camera = None
        self.__cameras = {target: cv2.VideoCapture(port) for target, port in cameras_ports.items()}

    def change_camera(self, new_target):
        """
        change the current camera to be the camera that suitable to the new_target
        :param new_target: the current target from the dashboard
        """
        if new_target not in self.__cameras.keys():
            raise KeyError("Target does not exist")

        if new_target == self._current_target:
            return
        self._current_target = new_target
        self.__current_camera = self.__cameras[self._current_target]

    def read_frame(self):
        """:return: the current frame from the camera"""
        return self.__current_camera.read()
