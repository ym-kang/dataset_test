import os
import re

def readmark_rename(folder):
    # copy marked image
    #folder = '0521_walk1'
    #dir = './data/0521_walk1/'
    dir = './data/'+folder+'/'

    files = os.listdir(dir)
    jpg_pattern = re.compile(".*.jpg")
    txt_pattern = re.compile(".*.txt")

    img_list = [img for img in files if jpg_pattern.match(img)]
    txt_list = [txt for txt in files if txt_pattern.match(txt)]


    img_txt_pair = []
    for txt in txt_list:
        txt_file = os.path.join(dir,txt)
        with open(txt_file) as f_txt:
            lines = f_txt.readlines()
            if(lines!=[]):
                print(txt_file) #found non-empty mark file
                #ser = re.search('([^/]*).txt',txt_file)
                jpg_path = txt_file.replace(".txt",".jpg")
                exist_jpg = os.path.exists(jpg_path)
                if(exist_jpg):
                    img_txt_pair.append((txt_file,jpg_path))
                pass

    from shutil import copy2    
    #target_folder='./data/0518_walk_train/'
    target_folder = dir[:len(dir)-1]+'_train/'
    if( not os.path.exists(target_folder)):
        os.mkdir(target_folder)
    for pair in img_txt_pair:
        copy2(pair[0],target_folder)
        copy2(pair[1],target_folder)
        print("copy:{}, {}".format(pair[0],pair[1]))
        
        
    import rename
    #rename files
    infix = '18'+folder  #180521_walk1
    rename.withText(target_folder,infix)


folders = ['0522_walk3']
for folder in folders:
    print('folder:'+folder)
    readmark_rename(folder)
'''
for img in img_list:
    
    print(img)
    
'''
    
