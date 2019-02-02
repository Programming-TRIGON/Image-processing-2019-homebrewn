xfrom PipelineManager import PipelineManager
import cv2
import logging

logging.basicConfig(level=logging.DEBUG)



pipelines = {

}

pipeline_manager = PipelineManager(pipelines)

cameras = []
camera_id = 0
cam = cv2.VideoCapture(camera_id)

def nt_settings_listener(table, key, value, isNew):
    if key == 'target':
        pipeline_manager.change_current_pipeline(value)


if __name__ == '__main__':


    while True:
        has_frame, frame = cam.read()

        if has_frame:
            target_contours = pipeline_manager.current_pipeline.process(frame)

            target_x = cv2.boundingRect(target_contours[0])
            nt.putNumber(target_x)
