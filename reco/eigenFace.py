"""
Not in use
"""
import cv2
import numpy as np
import random

img1 = cv2.imread('yalefaces_jpgs/subject01.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
img2 = cv2.imread('yalefaces_jpgs/subject02.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

data_dict = {}

input_files = []


def create_train_test(file):
    all_images = []
    f = open(file, 'r')
    for line in f:
        all_images.append(line[:-1])
    random.shuffle(all_images)
    l = len(all_images)
    return all_images[:int(0.7 * l)], all_images[int(0.7 * l) + 1:], all_images


def create_data_dict(training_data):
    for line in training_data:
        idx = int(line.split(".")[0][7:])
        if data_dict. has_key(idx):
            curr_files = data_dict[idx]
            np.append(curr_files, cv2.imread('yalefaces_jpgs/' + line[:-1], cv2.CV_LOAD_IMAGE_GRAYSCALE))
        else:
            data_dict[idx] = cv2.imread('yalefaces_jpgs/' + line, cv2.CV_LOAD_IMAGE_GRAYSCALE)


def run(model, test_cases):
    correct = 0
    incorrect = 0
    for test in test_cases:
        actual = int(test.split(".")[0][7:])
        op = model.predict(cv2.imread('yalefaces_jpgs/' + test, cv2.CV_LOAD_IMAGE_GRAYSCALE))
        if actual == op[0]:
            correct += 1
        else:
            incorrect += 1
        # print "Actual " + str(actual) + " Predicted " + str(op[0]) + " Confidence " + str(op[1])
    print "Correct" + str(correct) + "incorrect" + str(incorrect)


training_data, test_data, all = create_train_test('reco/trainer.txt')
create_data_dict(training_data)
model = cv2.createEigenFaceRecognizer()
model.train(data_dict.values(), np.array(data_dict.keys()))
run(model, test_data)

"""
print model.predict(cv2.imread('yalefaces_jpgs/subject01.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject02.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject03.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject04.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject05.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject06.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject07.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject08.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject09.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
print model.predict(cv2.imread('yalefaces_jpgs/subject10.centerlight.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE))
"""
