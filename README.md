# Object Detection using YOLOv3 Tensorflow 2

>> A starter yolov3 object detection template using tensorflow 2

### (YOLO v3 Implementation from)[https://github.com/zzh8829/yolov3-tf2]

### Features:
- Realtime object detection using YOLOv3 and Tensorflow
- Not more to setup
- Save model to tensorflow serving and tflite
- Create datasets by downloading images from google image search or extracting frames from video
- Converting images and labels to tfrecords file

commands:
- Training a model
python train.py --transfer=darknet --classes=data/labels/theft.names --epochs=10 --batch_size=5 --weights=models/checkpoints/yolov3/yolov3.tf --output=models/checkpoints/theft --num_classes=2 --weights_num_classes=80

- webcam detection
python webcam_detect.py --weights=models/checkpoints/theft/yolov3.tf --num_classes=2 --classes=data/labels/theft.names

python webcam_detect.py --weights=models/checkpoints/theft/yolov3_train_5.tf --num_classes=2 --classes=data/labels/theft.names