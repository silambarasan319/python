import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('/tmp'):
        print root
        print dirs
        print files
-------------------------------------------------------------------------------------------
import os
def main():
    # Create directory
    dirName = 'D:\\destination\\google'
    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
             
if __name__ == '__main__':
    main()
    path = os.getcwd()
    print ("The current working directory is %s" % path)
-------------------------------------------------------------------------------------------------
def main():

    # Get the modification time
    t = time.ctime(path.getmtime("disk.py"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("disk.py")))

if __name__ == "__main__":
    main()
 -----------------------------------------------------------------------------------------------------
