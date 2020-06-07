### (YOLO V3 Implementation from)[https://github.com/zzh8829/yolov3-tf2]

commands:
- Training a model
python train.py --transfer=darknet --classes=data/labels/theft.names --epochs=10 --batch_size=5 --weights=models/checkpoints/yolov3/yolov3.tf --output=models/checkpoints/theft --num_classes=2 --weights_num_classes=80

- webcam detection
python webcam_detect.py --weights=models/checkpoints/theft/yolov3.tf --num_classes=2 --classes=data/labels/theft.names

python webcam_detect.py --weights=models/checkpoints/theft/yolov3_train_5.tf --num_classes=2 --classes=data/labels/theft.names