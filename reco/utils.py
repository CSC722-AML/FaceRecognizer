from __future__ import print_function, division
import sys, os

sys.dont_write_bytecode = True
import Image


def convert_all():
    for f in os.listdir("yalefaces_gifs"):
        if f.endswith(".gif"):
            convert2JPG("yalefaces_gifs/" + f)


def convert2JPG(file_name):
    im = Image.open(file_name)
    im.save("yalefaces_jpgs/" + file_name.split("/")[-1][:-4] + ".jpg", "JPEG")


def convert_att():
    jpg_folder = "att_faces_jpgs"
    os.mkdir(jpg_folder)
    for fold in os.walk("att_faces_pgm"):
        new_fol = jpg_folder + "/" + fold[0].split("/")[-1] + "/"
        print(new_fol)
        os.mkdir(new_fol)
        try:
            for f in os.listdir(fold[0]):
                if f.endswith(".pgm"):
                    im = Image.open(fold[0] + "/" + f)
                    print("***%s" % f)
                    print(im)
                    im.save(new_fol + f.split("/")[-1][:-4] + ".jpg", "JPEG")
        except:
            print("Exception")
        print("***********")

