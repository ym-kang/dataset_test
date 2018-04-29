import os
import re

# copy marked image

files = os.listdir('./output/')
jpg_pattern = re.compile(".*.jpg")
txt_pattern = re.compile(".*.txt")

img_list = [img for img in files if jpg_pattern.match(img)]
txt_list = [txt for txt in files if txt_pattern.match(txt)]


img_txt_pair = []
for txt in txt_list:
    txt_file = os.path.join('output',txt)
    with open(txt_file) as f_txt:
        lines = f_txt.readlines()
        if(lines!=[]):
            print(txt_file)
            #ser = re.search('([^/]*).txt',txt_file)
            jpg_path = txt_file.replace(".txt",".jpg")
            exist_jpg = os.path.exists(jpg_path)
            if(exist_jpg):
                img_txt_pair.append((txt_file,jpg_path))
            pass

from shutil import copy2    
target_folder='copy/'
for pair in img_txt_pair:
    copy2(pair[0],target_folder)
    copy2(pair[1],target_folder)
    print("copy:{}, {}".format(pair[0],pair[1]))
    
    



    

'''
for img in img_list:
    
    print(img)
    
'''
    
