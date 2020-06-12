#!/usr/bin/python3

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():

    # Get the modification time
    t = time.ctime(path.getmtime("disk.py"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("disk.py")))


if __name__ == "__main__":
    main()
