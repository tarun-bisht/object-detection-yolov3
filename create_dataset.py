import json
import os
from absl import app, flags, logging
from absl.flags import FLAGS
from data_generator.image_downloader.downloader import download_images

flags.DEFINE_string('config', 'configs/download_config.json', 
    'Path to image download config.json file')

def main(_argv):
	with open(FLAGS.config,'r') as config:
	    arguments=json.load(config)
	download_images(arguments["keywords"],arguments["chromedriver"],arguments["size"],arguments["limit"])

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass