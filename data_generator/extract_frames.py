import time
import cv2
import os

def get_fps(vid):
	return vid.get(cv2.CAP_PROP_FPS)

def get_frames(input_paths,size,output_path):
	if not os.path.isdir(os.path.join(output_path,"frames")):
		os.mkdir(os.path.join(output_path,"frames"))
	num=0
	for input_path in input_paths:
		vid = cv2.VideoCapture(input_path)
		count=0
		num_frames=0
		fps=int(get_fps(vid))
		while True:
			_,img=vid.read()

			if img is None:
				print("Empty Frame")
				time.sleep(0.1)
				break

			if count>=num_frames:
				img_=cv2.resize(img,tuple(size))
				path=os.path.join(output_path,"frames",f'{num:0003}.jpg')
				cv2.imwrite(path,img_)
				print("Image Saved to: ",path)
				num_frames+=fps
				num+=1
			count+=1
