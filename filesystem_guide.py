import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('/tmp'):
        print root
        print dirs
        print files
        print '--------------------------------'
