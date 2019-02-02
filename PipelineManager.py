

class PipelineManager:
    __pipelines = {}
    current_pipeline = None

    def __init__(self, pipelines):
        self.__pipelines = pipelines

    def change_current_pipeline(self, pipeline_name):
        if pipeline_name in self.__pipelines:
            self.current_pipeline = self.__pipelines[pipeline_name]
        else:
            raise KeyError("{} does not point to a pipeline!".format(pipeline_name))
