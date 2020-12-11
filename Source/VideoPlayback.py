"""
Simple Video Playback using Python Components (UPBGE), assuming the video file is in the same directory as the blend-file.
Adapted by Guilherme Teres Nunes (Uniday Studio).
"""
import bge
from collections import OrderedDict


class VideoPlayback(bge.types.KX_PythonComponent):
    """ VideoPlayback Component:
        This component will replace a texture by a video. 
    You need to create a material with a texture (image) in the
    object to make this work.
    """
    
    args = OrderedDict([
        ("Source Video Directory", "Video1.avi"),
        ("End Function", ""),
    ])

    def start(self, args):
        self.onEndName = args["End Function"]
        # create a dynamic texture that will replace the static texture
        self.video = bge.texture.Texture(self.object)
        
        # define a source of image for the texture, here a movie                
        self.movie = bge.logic.expandPath("//" + args["Source Video Directory"])
            
        self.video.source = bge.texture.VideoFFmpeg(self.movie)
        self.video.source.scale = True
        
        if self.onEndName == "":
            self.video.source.repeat = -1
        
        # quick off the movie, but it wont play in the background
        self.video.source.play()

    def update(self):
        self.video.refresh(True)
        
        status = self.video.source.status
        
        if self.onEndName != "":
            if status != 2:
                print("Done!")
