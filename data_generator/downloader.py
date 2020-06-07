from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import urllib.parse
import os
import sys
import time
import base64
import random
import requests

google_base_url="https://www.google.com/search?"

def load_image_from_url(url):
    img_request=requests.get(url)
    return Image.open(BytesIO(img_request.content))

def load_image_from_base64(base64_url):
    im_bytes = base64.b64decode(base64_url)
    return Image.open(BytesIO(im_bytes))

def complete_loading(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except:
        pass

def download_images(keywords,chromedriver,output_path,img_size=(1280,720),limit=50):
    driver = webdriver.Chrome(chromedriver)
    if not os.path.isdir(os.path.join("data","downloads")):
        os.mkdir(os.path.join("data","downloads"))
    for key in keywords:
        if not os.path.isdir(os.path.join(output_path,"downloads",key)):
            os.mkdir(os.path.join(output_path,"downloads",key))
        saved_base_path=os.path.join(output_path,"downloads",key)
        t0=time.time()
        error=0
        google_url_params={"q":key,"tbm":"isch"}
        url=google_base_url+urllib.parse.urlencode(google_url_params)
        driver.get(url)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="islmp"]/div/div/div/div/div[4]')))
        time.sleep(1)
        try:
            box=driver.find_element_by_id("islmp")
            all_images=box.find_elements_by_tag_name("img")[:limit]
            for i,img in enumerate(all_images):
                img_src=img.get_attribute("src")
                if img_src is not None:
                    img=None
                    if img_src.startswith("http"):
                        img=load_image_from_url(img_src)
                    elif img_src.startswith("data:image/jpeg;base64,"):
                        img=load_image_from_base64(img_src.replace("data:image/jpeg;base64,",""))
                    img=img.convert(mode="RGB")
                    img.thumbnail(img_size)
                    save_path=os.path.join(saved_base_path,f"{key}{i:003}.jpg")
                    img.save(save_path)
                    print(f"{save_path} saved ")
                else:
                    error+=1
            t1=time.time()
            print(f"Time Taken: {t1-t0}sec")
            print(f"Total Image Processed: {len(all_images)}")
            print(f"URL with Error: {error}")
            print(f"Total Images Saved: {len(all_images)-error}")
            time.sleep(random.random() * 0.2 + 0.1)
        except Exception as e:
            print(f"Cannot Load Page Correctly {e}")