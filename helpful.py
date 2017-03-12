import os.path
import sys
f = open("os_path.txt","w")
sys.stdout = f
help(os.path)
f.close()