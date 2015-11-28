from __future__ import print_function, division
import sys, os
sys.dont_write_bytecode = True
import Image

def convert_all():
  for f in os.listdir("yalefaces_gifs"):
    if f.endswith(".gif"):
      convert2JPG("yalefaces_gifs/"+f)

def convert2JPG(file_name):
  im = Image.open(file_name)
  im.save("yalefaces_jpgs/"+file_name.split("/")[-1][:-4]+".jpg", "JPEG")