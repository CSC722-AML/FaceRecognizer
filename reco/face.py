from __future__ import print_function, division
import sys, os
import numpy as np
import cv2
from PIL import Image
import random

sys.dont_write_bytecode = True

HAAR_PATH = "haarconfigs/"
face_cascade = cv2.CascadeClassifier(HAAR_PATH + 'haarcascade_frontalface_default.xml')

# sift = cv2.SIFT()
# faces = face_cascade.detectMultiScale(img)
#
# kp = sift.detect(img, None)
#
# img2 = cv2.drawKeypoints(img, kp)
#
# cv2.imwrite('sift_keypoints.jpg',img2)

# folder = "yalefaces_gifs"
folder = "att_faces_pgm"
training_file = "trainer.txt"


def get_train_data(path):
    paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith(".txt")]
    images, classes = [], []
    with open(path + "/" + training_file) as data_file:
        for line in data_file:
            im_path = path + "/" + line.split(",")[1][:-1]
            image_obj = Image.open(im_path).convert("L")
            image = np.array(image_obj, 'uint8')
            clazz = int(line.split(",")[0])
            faces = face_cascade.detectMultiScale(image)
            for (x_coord, y_coord, width, height) in faces:
                images.append(image[y_coord:y_coord + height, x_coord:x_coord + width])
                classes.append(clazz)
                #cv2.imshow("Adding faces to traning set...", image[y_coord:y_coord+height, x_coord:x_coord+width])
                #cv2.waitKey(50)
    return images, classes

ims, cls = get_train_data(folder)


def get_train_data_no_haar(path):
    images, classes = [], []
    with open(path + "/" + training_file) as data_file:
        for line in data_file:
            im_path = path + "/" + line.split(",")[1][:-1]
            image_obj = Image.open(im_path).convert("L")
            image = np.array(image_obj, 'uint8')
            clazz = int(line.split(",")[0])
            images.append(image)
            classes.append(clazz)
    return images, classes


ims_nh, cls_nh = get_train_data_no_haar(folder)


def split_train_test(ips, ops):
    img_map = {}
    for ip, op in zip(ips, ops):
        imgs = img_map.get(op, [])
        imgs.append(ip)
        img_map[op] = imgs
    tests_ip, tests_op, trains_ip, trains_op = [], [], [], []
    for op, ips in img_map.items():
        i = random.randint(0, len(ips) - 1)
        tests_ip.append(ips[i])
        tests_op.append(op)
        trains_ip.extend(ips[:i] + ips[i + 1:])
        trains_op.extend([op] * (len(ips) - 1))
    return tests_ip, tests_op, trains_ip, trains_op


class Recognizer:
    def __init__(self, ips, ops):
        tests_ip, tests_op, trains_ip, trains_op = split_train_test(ips, ops)
        self.tests_ip = tests_ip
        self.tests_op = tests_op
        self.trains_ip = trains_ip
        self.trains_op = trains_op
        self.recognizer = None

    def train(self):
        self.recognizer.train(self.trains_ip, np.array(self.trains_op))

    def test(self):
        correct, total = 0, 0
        for img, clazz in zip(self.tests_ip, self.tests_op):
            total += 1
            pred, conf = self.recognizer.predict(img)
            if pred == clazz:
                # print("%d is Identified with confidence %f"%(clazz, conf))
                cv2.imshow("Classified Right", img)
                cv2.waitKey(200)
                correct += 1
            else:
                # print("%d is InCorrectly Recognized as %d"%(clazz, pred))
                cv2.imshow("Classified Wrong", img)
                cv2.waitKey(200)
                pass
        return correct, total


class Eigen_Recognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self, ims_nh, cls_nh)
        self.recognizer = cv2.createEigenFaceRecognizer()


class LBPH_Recognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self, ims, cls)
        self.recognizer = cv2.createLBPHFaceRecognizer()


class Fisher_Recognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self, ims_nh, cls_nh)
        self.recognizer = cv2.createFisherFaceRecognizer()


def test_lbph():
    model = LBPH_Recognizer()
    model.train()
    correct, total = model.test()
    print("LBPH: %d out of %d classified right."%(correct, total))


def test_eigen():
    model = Eigen_Recognizer()
    model.train()
    correct, total = model.test()
    print("Eigen: %d out of %d classified right."%(correct, total))

def test_fisher():
    model = Fisher_Recognizer()
    model.train()
    correct, total = model.test()
    print("Fisher: %d out of %d classified right."%(correct, total))


def test():
    lbfs, eigens, fishers = [], [], []
    for i in range(1):
        print(i)
        model = LBPH_Recognizer()
        model.train()
        correct, total = model.test()
        lbfs.append(correct * 100 / total)
        print("LBPH: %d out of %d classified right."%(correct, total))

        model = Eigen_Recognizer()
        model.train()
        correct, total = model.test()
        eigens.append(correct * 100 / total)
        print("Eigen", correct, total)

        model = Fisher_Recognizer()
        model.train()
        correct, total = model.test()
        fishers.append(correct * 100 / total)
        print("Fisher", correct, total)

    print("LBPH", np.mean(lbfs), np.std(lbfs))
    print("Eigen", np.mean(eigens), np.std(eigens))
    print("Fisher", np.mean(fishers), np.std(fishers))


if __name__ == "__main__":
    args = sys.argv
    cv2.imshow("Classified Right",np.array([[0,0], [0,0]]))
    cv2.imshow("Classified Wrong",np.array([[0,0], [0,0]]))
    if args[1] == "lbph":
        test_lbph()
    elif args[1] == "eigen":
        test_eigen()
    elif args[1] == "fisher":
        test_fisher()
