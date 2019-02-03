from PipelineManager import PipelineManager
from CameraManager import CameraManager
from Constants import CameraConstants
import cv2
import logging

logging.basicConfig(level=logging.DEBUG)


pipelines = {

}

cameras = {
    'front_cam': CameraConstants.port_matrix['top_left']
}

pipeline_manager = PipelineManager(pipelines)
# here we will put the first camera that will capture frames at the beginning of the match
camera_manager = CameraManager(CameraConstants.port_matrix['bottom_right'])


def nt_settings_listener(table, key, value, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)
    if key == 'camera':
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
