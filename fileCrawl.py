# Run this python program in the terminal. Change the rootDir to 
# the folder that you want to start traversing
# Chris Sanchez 8/15/18

import os, shutil
import glob

# define the directory you want to crawl
workingDirectory = os.getcwd()

target_file = input('Enter name of file to copy: ')

rootDir = workingDirectory + '/' + target_file

# Makes a copy of the folder in your working directory
destination = workingDirectory + '/' + target_file + '_Copy'

# Clone the entire directory
shutil.copytree(rootDir,destination,symlinks=False,ignore=None);

def removeFiles(destination):
	# for all folders, subfolders etc... walk through
	for dirName, subdirList, fileList in os.walk(destination):
		print('Found directory: %s' % dirName)

    	# If the file ends in .wmv, then delete it
		for file_name in fileList:
			print('\t%s' % file_name)
			if (file_name.endswith(".wmv")):
				os.remove(os.path.join(dirName, file_name))


removeFiles(destination)