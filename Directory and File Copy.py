import pysftp
import os
import shutil


from stat import S_IMODE, S_ISDIR, S_ISREG
from datetime import datetime

# find the hosts key, but for now

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

redo_list = []


save_dir= '////'
save_dir2 = '////'

localpath = os.path.join(save_dir2, '')


if not os.path.exists(localpath):
    try:
        os.mkdir(localpath,mode=777)
        print('MAKE_DIR: ' + localpath)
    except OSError:
        print("directory error occurred")

for folder_name in os.listdir(save_dir):
    keeppath = os.path.join(save_dir, folder_name)
    subf = os.path.join(save_dir, folder_name)

    print(subf)
            # skip repository folder
    if subf == localpath: continue
            # skip eventually files
    if os.path.isfile(subf): continue

    for subfolder_name in os.listdir(keeppath):
        oldsubf= os.path.join(keeppath, subfolder_name)
        newsubf = os.path.join(localpath, subfolder_name)

       
        if os.path.isfile(newsubf): continue
        if os.path.isfile(oldsubf): continue

        # if os.path.exists(newsubf):continue
        if os.path.exists(newsubf):
            x = 0
            while os.path.exists(newsubf):
                x=x+1
                newsubf = os.path.join(localpath, subfolder_name+'_'+str(x))



        shutil.copytree(oldsubf, newsubf)

        
#optional: remove files from old directory when finished        
dir = '////'
for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
             shutil.rmtree(path)
        except OSError:
            os.remove(path)


