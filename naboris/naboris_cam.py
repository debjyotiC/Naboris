from atlasbuggy.camerastream.picamera import PiCamera


class NaborisCam(PiCamera):
    def __init__(self, pipeline, logger=None, video_recorder=None, enabled=True):
        super(NaborisCam, self).__init__(enabled, logger=logger, video_recorder=video_recorder)

        self.pipeline = pipeline

    def init_cam(self, cam):
        cam.resolution = (self.width // 2, self.height // 2)
        cam.framerate = 24
        cam.hflip = True
        cam.vflip = True

    def update(self):
        self.frame = self.pipeline.update(self.frame)
