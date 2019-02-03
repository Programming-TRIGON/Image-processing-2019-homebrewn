from PipelineManager import PipelineManager
from CameraManager import CameraManager
from Constants import CameraConstants
import cv2
import logging

logging.basicConfig(level=logging.DEBUG)


pipelines = {

}

pipeline_manager = PipelineManager(pipelines)
# here we will put the first camera that will capture frames at the beginning of the match
camera_manager = CameraManager(CameraConstants.port_matrix['bottom_right'])


def nt_settings_listener(table, key, value, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)


if __name__ == '__main__':
#TODO: make a thread that will run CameraManager and set global variables: frame and has_frame
    while True:

        if camera_id_from_networkTable not camera_manager.get_camera_id():
            camera_manager.change_camera(camera_id_from_networkTable)

        has_frame, frame = camera_manager.read_frame()

        if has_frame:
            target_contours = pipeline_manager.current_pipeline.process(frame)

            target_x = cv2.boundingRect(target_contours[0])
            nt.putNumber(target_x)
        else:
            nt.putNumber(9999)
