import os
import random
import shutil
import xml.etree.ElementTree as ET


def extract_jpgs(path):
    files = os.listdir(path)
    jpgs = []
    for file in files:
        if os.path.isfile(os.path.join(path, file)) and file.endswith(".jpg"):
            jpgs.append(file)
    return jpgs


def copy_file(filename, src, dest, alias=""):
    jpg_file = filename + ".jpg"
    xml_file = filename + ".xml"
    shutil.copy(os.path.join(src, jpg_file), os.path.join(dest, alias + "_" + jpg_file))
    shutil.copy(os.path.join(src, xml_file), os.path.join(dest, alias + "_" + xml_file))


def xml_write(xml_file, new_name, folder):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    root.find("filename").text = new_name
    root.find("folder").text = folder
    root.find("path").text = new_name + ".jpg"
    tree.write(xml_file)


def write_files(dir_path, folder, copy_path):
    path = os.path.join(dir_path, folder)
    alias = folder.replace(" ", "_")
    train_count = 0
    test_count = 0
    if os.path.isdir(path):
        jpgs = extract_jpgs(path)
        num_files = len(jpgs)
        random.shuffle(jpgs)
        test_num = round(test_size * num_files)
        train_num = num_files - test_num
        print("On ", alias)
        print("Number of Test Images: ", test_num)
        print("Number of Train Images: ", train_num)
        train_files = jpgs[0:train_num]
        test_files = jpgs[train_num:]
        if not os.path.isdir(os.path.join(copy_path, "train")):
            os.mkdir(os.path.join(copy_path, "train"))
        if not os.path.isdir(os.path.join(copy_path, "test")):
            os.mkdir(os.path.join(copy_path, "test"))

        for file in train_files:
            name = file.split(".jpg")[0]
            copy_file(name, path, os.path.join(copy_path, "train"), alias)
            xml_write(
                os.path.join(copy_path, "train", alias + "_" + name + ".xml"),
                alias + "_" + name,
                "train",
            )
            train_count += 1

        for file in test_files:
            name = file.split(".jpg")[0]
            copy_file(name, path, os.path.join(copy_path, "test"), alias)
            xml_write(
                os.path.join(copy_path, "test", alias + "_" + name + ".xml"),
                alias + "_" + name,
                "test",
            )
            test_count += 1
    return train_count, test_count


dir_path = "data/downloads"
copy_path = "data/images"
folders = os.listdir(dir_path)
test_size = 0.1

test_num = 0
train_num = 0
for folder in folders:
    train_c, test_c = write_files(dir_path, folder, copy_path)
    test_num += test_c
    train_num += train_c
print("Total Test Images: ", test_num)
print("Total Train Images: ", train_num)
