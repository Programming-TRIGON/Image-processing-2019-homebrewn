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


def nt_settings_listener(table, key, value, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)
        camera_manager.change_camera(value)


if __name__ == '__main__':

    while True:
        has_frame, frame = camera_manager.read_frame()

        if has_frame:
            target_contours = pipeline_manager.current_pipeline.process(frame)

            target_x = cv2.boundingRect(target_contours[0])
            nt.putNumber(target_x)
        else:
            nt.putNumber(9999)
