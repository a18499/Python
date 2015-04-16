import os
import subprocess

list1 = {}
out = subprocess.check_output(["ls",],shell=True)

(word,last) = str(out) .split("\n",1)
print(word)

	


