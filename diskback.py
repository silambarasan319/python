#!/usr/bin/python3

import os, zipfile, shutil, sys
from datetime import datetime

#copy files and folder and compress into a zip file
def     doprocess(source_folder, target_zip):
        zipf = zipfile.ZipFile(target_zip, "w")
        for subdir, dirs, files in os.walk(source_folder):
                for file in files:
                        zipf.write(os.path.join(subdir, file))

        print ("Created ", target_zip)

if __name__ == '__main__':
        print ('Starting execution')

        #compress to zip
        source_folder = '/root/'
        target_zip = '/tmp/myfile-%s.zip'%datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        doprocess(source_folder, target_zip)

        print ('Ending execution')
