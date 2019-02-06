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

cameras = {
    'cargo': CameraConstants.port_matrix['bottom_right'],
    'hatch': CameraConstants.port_matrix['bottom_right'],
    'reflector': CameraConstants.port_matrix['top_right']
}

pipeline_manager = PipelineManager(pipelines)
camera_manager = CameraManager(cameras)
nt_manager = NTManager("ImageProcessing")
# the first target to be searched
current_target = "hatch"


def nt_settings_listener(table, key, value, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)
        camera_manager.change_camera(value)
        current_target = key


if __name__ == '__main__':
    while True:
        has_frame, frame = camera_manager.read_frame()

        if has_frame:
            target_contours = pipeline_manager.current_pipeline.process(frame)
            if current_target == "reflector":
                # compute the center of the contour
                moment1 = cv2.moments(target_contours[0])
                moment2 = cv2.moments(target_contours[1])
                target_x = (int(moment1["m10"] / moment1["m00"])+int(moment2["m10"] / moment2["m00"]))/2
                target_y = (int(moment1["m01"] / moment1["m00"]+int(moment1["m01"] / moment1["m00"])))/2
                nt_manager.put_string("direction", str(target_x)+' '+str(target_y))
        else:
            nt_manager.put_string("direction", "9999")
