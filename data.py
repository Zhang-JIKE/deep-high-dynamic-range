import cv2
import numpy as np
import os
import util
from config import Config

def preprocess_training_data(config: Config):
    """
    preprocess training data, pack it into h5 file
    """
    scene_paths = util.read_dir(config.TRAINING_RAW_DATA_PATH)
    print(scene_paths)
    for scene_path in scene_paths:
        exposures = read_exposure(scene_path)
        print(f"exposures: {exposures}")
        ldr_imgs, hdr_img = read_ldr_hdr_images(scene_path)
        # inputs, label = compute_training_examples(ldr_imgs, exposures, hdr_img)
        # write_training_examples(inputs, label, config.TRAINING_DATA_PATH, "TrainingSequence.h5")


def read_exposure(path: str):
    """
    read exposure data from exposures.txt

    exposures are specified in exponent representation
    thus, return 2 ** x
    """
    paths = [f.path for f in os.scandir(path) if f.name.endswith('.txt')]
    if len(paths) < 1:
        print("[read_exposure]: cannot find exposure file")
        return None
    exposure_file_path = paths[0]
    exposures = []
    with open(exposure_file_path) as f:
        for line in f:
            exposures.append(2 ** float(line))
    return exposures


def read_ldr_hdr_images(path: str):
    paths = [f for f in os.scandir(path)]
    ldr_paths = [x.path for x in paths if x.name.endswith(".tif")]
    hdr_path = [x.path for x in paths if x.name.endswith(".hdr")]
    if len(ldr_paths) < 3 or len(hdr_path) < 1:
        print("[read_ldr_hdr_images]: cannot find enough ldr/hdr images")
    ldr_images = []
    for i in range(3):
        img = util.im2single(cv2.imread(ldr_paths[i], -1))
        # img = util.clamp() :TODO
        ldr_images.append(img)
    hdr_image = cv2.imread(hdr_path[0], -1)
    return ldr_images, hdr_image


def compute_training_examples(ldr_imgs, exposures, hdr_img):
    pass


def writing_training_examples(inputs, label, path, filename):
    pass