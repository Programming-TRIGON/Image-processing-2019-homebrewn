from PipelineManager import PipelineManager
from CameraManager import CameraManager
from Constants import CameraConstants
from NTManager import NTManager
import cv2
import logging

logging.basicConfig(level=logging.DEBUG)


pipelines = {
    'cargo': CargoPipline,
    'hatch': HatchPipline,
    'reflector': ReflectorPipline
}

cameras_ports = {
    'cargo': CameraConstants.port_matrix['bottom_right'],
    'hatch': CameraConstants.port_matrix['bottom_right'],
    'reflector': CameraConstants.port_matrix['top_right']
}

pipeline_manager = PipelineManager(pipelines)
camera_manager = CameraManager(cameras_ports)
nt_manager = NTManager("ImageProcessing")
# the first target to be searched
current_target = "hatch"


def nt_settings_listener(table, key, target, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(target)
        camera_manager.change_camera(target)
        current_target = key  # current_target should be equals target


if __name__ == '__main__':
    while True:
        has_frame, frame = camera_manager.read_frame()

        if has_frame:
            contours = pipeline_manager.current_pipeline.process(frame)
            if current_target == "reflector":
                # compute the center of two contours
                moment1 = cv2.moments(contours[0])
                moment2 = cv2.moments(contours[1])
                target_x = (int(moment1["m10"] / moment1["m00"])+int(moment2["m10"] / moment2["m00"]))/2
                target_y = (int(moment1["m01"] / moment1["m00"]+int(moment1["m01"] / moment1["m00"])))/2
                nt_manager.put_string("direction", str(target_x)+' '+str(target_y))
            else:
                moment = cv2.moments(contours[0])
                target_x = int(moment["m10"] / moment["m00"])
                target_y = int(moment["m01"] / moment["m00"])
                nt_manager.put_string("direction", str(target_x) + ' ' + str(target_y))
        else:
            nt_manager.put_string("direction", "9999")
