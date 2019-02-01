

class PipelineManager:
    pipelines = []

    def __init__(self, pipelines, outputConsumer=lambda x: None):
        self.pipelines = pipelines

