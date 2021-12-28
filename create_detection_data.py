import os
from src.utils.xml_to_csv import xml_to_csv
from src.utils.generate_tfrecord import tfrecord_generate
from absl import app, flags
from absl.flags import FLAGS

flags.DEFINE_string(
    "image_dir",
    "data/dataset",
    "path to train and test directory with image files and xml annotations for converting to tfrecords",
)
flags.DEFINE_string(
    "outputpath",
    "data/dataset/tfrecords",
    "output path to save tfrecords and respective csv",
)
flags.DEFINE_string("classes", "data/labels/coco.names", "path to classes names file")


def main(_argv):
    for folder in ["test", "train"]:
        image_path = os.path.join(FLAGS.image_dir, folder)
        csv_output = os.path.join("data", "csv", f"{folder}_labels.csv")
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(csv_output, index=None)
        print(f"Successfully converted {folder} annotations to csv at {csv_output}")
        tfrecord_output = os.path.join(FLAGS.outputpath, f"{folder}.tfrecord")
        images_dir = os.path.join(FLAGS.image_dir, folder)
        tfrecord_generate(csv_output, images_dir, tfrecord_output, FLAGS.classes)


if __name__ == "__main__":
    try:
        app.run(main)
    except SystemExit:
        pass
