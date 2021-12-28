# Object Detection using TensorFlow YOLOv3

A starter yolov3 object detection using tensorflow 2

## Features

- Realtime object detection using YOLOv3 and Tensorflow
- Less setup required to start object detection
- Convert trained model to tensorflow serving and tflite
- Create datasets by downloading images from google image search or duckduckgo image search or by extracting frames from video
- Converting images and labels to tfrecords file

## Requirements

### System

There is no specific requirements for inferencing from pretrained models but require GPU for training or finetuning a detection model.

### Python 3

Python 3.6 or higher. Tested with Python 3.7, 3.9 in Windows 10 and Linux.

### Packages

- `tensorflow-gpu>=2.0` or `tensorflow>=2.0`
- `numpy`
- `absl-py`
- `opencv-python`

This implementation is tested with tensorflow cpu and gpu 2.0, 2.2, 2.7 in Windows 10 and Linux

## Installation

### Install Python

There are two ways to install python in windows using [Python 3 installer](https://www.python.org/downloads/) or [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Installing python with anaconda or [miniconda](https://docs.conda.io/en/latest/miniconda.html) is recommended. In linux Python 3 is installed by default but we can also install miniconda or conda into linux.

### Creating Virtual Environment

Create a new python virtual environment using conda or venv and activate it. If Anaconda or Miniconda is installed use `conda` else use `venv` to create virtual environments.

- Using conda

```bash
conda create --name tfod
conda activate tfod
conda install pip
```

- Using venv in linux

```bash
python3 -m venv path/to/create/env/tfod
source path/to/create/env/tfod/bin/activate
```

- Using venv in windows

```bash
python -m venv path\to\create\env\tfod
path\to\create\env\tfod\Scripts\activate
```

### Installing dependencies

#### Installing required python packages

The command below will install the required dependencies from `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Download Pretrained YOLO weights

Download YOLO pretrained coco weights from [Joseph Redmon's website](https://pjreddie.com/yolo/) and convert them using `convert_yolo_weight.py` script (steps are provided in documentation below)

### Additional guides:

If get stuck in installation part follow these additional resources

- [Python Installation](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list)
- [pip and usage](https://www.youtube.com/watch?v=U2ZN104hIcc)
- [Anaconda installation and using conda](https://www.youtube.com/watch?v=YJC6ldI3hWk)

## Documentation

### Detect Objects in Image

```bash
python detect_image.py \
    --image "PATH/TO/IMAGE/FILE" \
    --weights "TRAINED/.tf/MODEL/WEIGHTS" \
    --num_classes 80 \
    --classes "PATH/TO/LABELS/.names/FILE"
```

- `classes` Path to classes .names file which contains names of objects in images. Defaults to `data/labels/coco.names`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `tiny` using yolov3 tiny or not. Defaults to `False`
- `size` resize images to size specified. Defaults to `416`
- `image` Path to input image to detect objects in. Defaults to `None`
- `tfrecord` Path to tfrecord to use instead of image. Defaults to `None`
- `output` Path to save detection output. Defaults to `data/outputs/detection_output.jpg`
- `num_classes` Number of classes model can detect. Defaults to `80`

### Detect Objects in Video Feed

```bash
python detect_video.py \
    --model PATH/TO/MODEL \
    --video PATH/TO/VIDEO \
    --output PATH/TO/SAVE/OUTPUT/VIDEO
```

- `classes` Path to classes .names file which contains names of objects in images. Defaults to `data/labels/coco.names`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `tiny` using yolov3 tiny or not. Defaults to `False`
- `video` Path to input video to detect objects in. Defaults to `None`
- `size` resize images to size specified. Defaults to `416`
- `output_format` codec used in VideoWriter when saving video to file. Defaults to `XVID`
- `output` Path to save detection output. Defaults to `None`
- `num_classes` Number of classes model can detect. Defaults to `80`

### Detect Objects in Camera Feed

```bash
python detect_webcam.py \
    --weights "TRAINED/.tf/MODEL/WEIGHTS" \
    --num_classes 2 \
    --classes "PATH/TO/LABELS/.names/FILE"
```

- `classes` Path to classes .names file which contains names of objects in images. Defaults to `data/labels/coco.names`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `tiny` using yolov3 tiny or not. Defaults to `False`
- `camera` camera to use. Defaults to `0`
- `size` resize images to size specified. Defaults to `416`
- `output_format` codec used in VideoWriter when saving video to file. Defaults to `XVID`
- `output` Path to save detection output. Defaults to `None`
- `num_classes` Number of classes model can detect. Defaults to `80`

### Training an object detection model using TfRecords

```bash
python train.py \
    --dataset "PATH/TO/TRAIN/.tfrecord"
    --val_dataset "PATH/TO/TEST/.tfrecord"
    --transfer darknet \
    --classes "PATH/TO/LABELS/.names/FILE" \
    --epochs 10 \
    --batch_size 5 \
    --weights "PATH/TO/CONVERTED/YOLO/WEIGHTS/.tf/FILE" \
    --output "PATH/TO/SAVE/TRAINED/MODEL" \
    --num_classes 2 \
    --weights_num_classes 80
```

- `dataset` Path to train tfrecords file. Defaults to `data/dataset/tfrecords/train.tfrecord`
- `val_dataset` Path to train tfrecords file. Defaults to `data/dataset/tfrecords/test.tfrecord`
- `tiny` using yolov3 tiny or not. Defaults to `False`
- `classes` Path to classes .names file which contains names of objects in images. Defaults to `data/labels/coco.names`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `output` Path to save trained model
- `transfer` Define options for training, choices include `none` Training from scratch, `darknet` Transfer darknet, `no_output` Transfer all but output, `frozen` Transfer and freeze all, `fine_tune` Transfer all and freeze darknet only

### Converting Trained model to tf serving

```bash
python convert_tfserving.py \
    --weights "PATH/TO/CONVERTED/YOLO/WEIGHTS/.tf/FILE" \
    --tiny False \
    --output "PATH/TO/SAVE/TFSERVING/FILES" \
    --image "PATH/TO/TEST/IMAGE"
    --output "path/to/exported_model_directory"
    --num_classes 80
```

- `tiny` using yolov3 tiny or not. Defaults to `False`
- `classes` Path to classes .names file which contains names of objects in images. Defaults to `data/labels/coco.names`
- `image` Path to input image to detect objects in. Defaults to `None`
- `output` Path to save tfserving files. Defaults to `data/outputs/serving`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `num_classes` Number of classes model can detect. Defaults to `80`

### Converting Trained model as tflite

```bash
python convert_tflite.py \
    --weights "PATH/TO/CONVERTED/YOLO/WEIGHTS/.tf/FILE" \
    --tiny False \
    --output "PATH/TO/SAVE/TFLITE/MODEL" \
    --num_classes 80
```

- `tiny` using yolov3 tiny or not. Defaults to `False`
- `output` Path to save tflite model. Defaults to `data/outputs/tflite/yolov3.tflite`
- `weights` Path to weights file .tf file, Defaults to `data/models/yolov3/yolov3.tf`
- `num_classes` Number of classes model can detect. Defaults to `80`
- `size` resize images to size specified. Defaults to `416`

### Downloading images from Duckduckgo or Google Image search (collecting data)

```bash
python download_images.py \
    --config PATH/TO/DOWNLOADER/JSON
```

- `config` Path to config file of downloader. Defaults to `configs/download_config.json`

### Creating Detection dataset

```bash
python create_detection_data.py \
    --image_dir "PATH/TO/DIRECTORY/WITH/TRAIN/TEST/FILES"
    --outputpath "PATH/TO/SAVE/TFRECORDS/FILES"
    --classes "PATH/TO/LABELS/.names/FILE"
```

### Converting YOLO .weights file into TF

```bash
python covert_yolo_weights.py \
    --weights "PATH/TO/YOLO/.weights/FILE"
    --output "PATH/TO/SAVE/CONVERTED/TF/CHECKPOINT"
    --num_classes 80
    --tiny False
```

- `weights` Path to pretrained yolo weights file, can be downloaded from [Joseph Redmon's website](https://pjreddie.com/yolo/). Defaults to `data/weights/yolov3.weights`
- `output` Path to save tf checkpoints model. Defaults to `models/yolov3/yolov3.tf`
- `tiny` using yolov3 tiny or not. Defaults to `False`
- `num_classes` Number of classes model can detect. Defaults to `80`

## References

- YOLOv3 TensorFlow implementation by [zzh8829](https://github.com/zzh8829/yolov3-tf2)
- YOLO pretrained coco weights from [Joseph Redmon's website](https://pjreddie.com/yolo/)
