import os
import shutil
import random

random.seed(0)


def split_data(file_path, new_file_path, train_rate, val_rate, test_rate):
    eachclass_image = []
    for image in os.listdir(file_path):
        eachclass_image.append(image)
    total = len(eachclass_image)
    random.shuffle(eachclass_image)
    train_images = eachclass_image[0:int(train_rate * total)]
    val_images = eachclass_image[int(train_rate * total):int((train_rate + val_rate) * total)]
    test_images = eachclass_image[int((train_rate + val_rate) * total):]

    for image in train_images:
        print(image)
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'train' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
    new_name = os.listdir(new_file_path + '/' + 'train' + '/' + 'images')

    for im in new_name:
        old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
        new_xmlpath1 = new_file_path + '/' + 'train' + '/' + 'labels'
        if not os.path.exists(new_xmlpath1):
            os.makedirs(new_xmlpath1)
        new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
        shutil.copy(old_xmlpath, new_xmlpath)

    for image in val_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'val' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
    new_name = os.listdir(new_file_path + '/' + 'val' + '/' + 'images')

    for im in new_name:
        old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
        new_xmlpath1 = new_file_path + '/' + 'val' + '/' + 'labels'
        if not os.path.exists(new_xmlpath1):
            os.makedirs(new_xmlpath1)
        new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
        shutil.copy(old_xmlpath, new_xmlpath)

    for image in test_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'test' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
    new_name = os.listdir(new_file_path + '/' + 'test' + '/' + 'images')

    for im in new_name:
        old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
        new_xmlpath1 = new_file_path + '/' + 'test' + '/' + 'labels'
        if not os.path.exists(new_xmlpath1):
            os.makedirs(new_xmlpath1)
        new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
        shutil.copy(old_xmlpath, new_xmlpath)


if __name__ == '__main__':
    file_path = "C:/Users/admin/Desktop/111/img"
    xmlpath = 'C:/Users/admin/Desktop/111/lab/'
    new_file_path = "E:/Tang/c"
    split_data(file_path, new_file_path, train_rate=0.8, val_rate=0.1, test_rate=0.1)