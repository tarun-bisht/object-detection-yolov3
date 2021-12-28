from absl import app, flags, logging
from absl.flags import FLAGS
import tensorflow as tf
from src.yolov3.models import YoloV3, YoloV3Tiny

flags.DEFINE_string("weights", "data/models/yolov3/yolov3.tf", "path to weights file")
flags.DEFINE_boolean("tiny", False, "yolov3 or yolov3-tiny")
flags.DEFINE_string(
    "output", "data/outputs/tflite/yolov3.tflite", "path to saved_model"
)
flags.DEFINE_integer("num_classes", 80, "number of classes in the model")
flags.DEFINE_integer("size", 416, "image size")


def main(_argv):
    if FLAGS.tiny:
        yolo = YoloV3Tiny(size=FLAGS.size, classes=FLAGS.num_classes)
    else:
        yolo = YoloV3(size=FLAGS.size, classes=FLAGS.num_classes)

    yolo.load_weights(FLAGS.weights)
    logging.info("weights loaded")

    converter = tf.lite.TFLiteConverter.from_keras_model(yolo)
    converter.target_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS,
        tf.lite.OpsSet.SELECT_TF_OPS,
    ]
    converter.allow_custom_ops = True
    tflite_model = converter.convert()
    open(FLAGS.output, "wb").write(tflite_model)
    logging.info("model saved to: {}".format(FLAGS.output))


if __name__ == "__main__":
    app.run(main)
