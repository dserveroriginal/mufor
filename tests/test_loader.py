from tests import os_functions
import unittest

from mufor import loader,config

# class TestLoader(unittest.TestCase):
    # TODO: convert

    # def test_video_download(self):
    #     file=config.load()
    #     try:
    #         filename=loader.download("https://www.youtube.com/watch?v=fRh97wohgJ4",file,os_functions.fl_gen(""))
    #     except:
    #         raise
    #     result=os_functions.exist(filename)
    #     os_functions.try_rm(filename)
        
    #     self.assertTrue(result)
        
    # def test_playlist_download(self):
    #     file=config.load()
    #     try:
    #         filename=loader.download("https://www.youtube.com/playlist?list=PLtyo3aqsNv_Oe686OmaAi1heDjjnxYRmw",file,os_functions.fl_gen(""),playlist=True,load=False)
    #     except:
    #         raise
    #     result=filename.__eq__("")
        
    #     self.assertTrue(result)
        
        