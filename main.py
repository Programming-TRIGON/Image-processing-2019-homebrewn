from PipelineManager import PipelineManager
from CameraManager import CameraManager
from Constants import CameraConstants
from NTManager import NTManager
from ReflectorPipeline import ReflectorPipeline
from CargoPipeline import CargoPipeline
from HatchPipeline import HatchPipeline
from DirectionFunctions import *
import logging

logging.basicConfig(level=logging.DEBUG)


def nt_settings_listener(table, key, value, isNew):
    global current_target
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)
        camera_manager.change_camera(value)
        current_target = value


if __name__ == '__main__':
    pipelines = {
        'cargo': (CargoPipeline(), one_contour_xy_direction),
        'hatch': (HatchPipeline(), one_contour_xy_direction),
        'reflector': (ReflectorPipeline(), two_contour_xy_direction)
    }

    cameras_ports = {
        'cargo': CameraConstants.port_matrix['bottom_right'],
        'hatch': CameraConstants.port_matrix['bottom_right'],
        'reflector': CameraConstants.port_matrix['top_right']
    }

    pipeline_manager = PipelineManager(pipelines)
    camera_manager = CameraManager(cameras_ports)
    nt_manager = NTManager("ImageProcessing", nt_settings_listener)
    # the first target to be searched
    current_target = 'hatch'

    while True:
        has_frame, frame = camera_manager.read_frame()
        current_pipeline = pipeline_manager.current_pipeline
        if has_frame:
            nt_manager.put_string("direction", current_pipeline[1](current_pipeline[0].process(frame)))
        else:
            nt_manager.put_string("direction", "9999")
