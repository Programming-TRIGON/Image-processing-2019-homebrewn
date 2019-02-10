

class PipelineManager:

    def __init__(self, pipelines):
        self.current_pipeline = None
        self.__pipelines = pipelines
        if type(pipelines) is dict or len(self.__pipelines) != 0:
            self.current_pipeline = self.__pipelines[0]
        else:
            raise NotADirectoryError("parameter is not a dictionary!")

    def change_current_pipeline(self, pipeline_name):
        if pipeline_name in self.__pipelines:
            self.current_pipeline = self.__pipelines[pipeline_name]
        else:
            raise KeyError("{} does not point to a pipeline!".format(pipeline_name))
