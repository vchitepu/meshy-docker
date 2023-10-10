import os
from pyvirtualdisplay import Display
from src import core


class Meshy:
    def __init__(self):
        self.output_dir = ''


    def sample(self):
        with Display(backend='xvfb', size=(1024, 768), color_depth=24) as disp:
            os.environ['DISPLAY'] = ':0'
            core.run_makevideo('/output/extras/depthmap-0001.obj', '300', '40', 1, '-0.015, 0.0, -0.05', '0.03, 0.03, 0.05, 0.03', False, 'mp4', '3')
