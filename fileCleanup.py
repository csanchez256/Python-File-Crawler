# Run this python program in the terminal. 
# Type in the terminal the folder that you want to start traversing
# Chris Sanchez 8/15/18

import os, shutil

# define the directory you want to traverse
def getWorkingDirectory():
        workingDirectory = os.getcwd()
        return workingDirectory

def targetFile():        
        target_file = input('Enter name of directory to copy: ')
        return target_file

def fileInput():
        file_input = input('Enter the type of file don\'t want copied: ')
        return file_input

target_file = targetFile()
file_input = fileInput()

print("\nThank you and please wait... \n\n")

file_extension = '.' + file_input

rootDir = getWorkingDirectory() + '/' + target_file

# Makes a copy of the folder in your working directory
destination = getWorkingDirectory() + '/' + target_file + '_Copy'

# Clone the entire directory
shutil.copytree(rootDir,destination,symlinks=False,ignore=None);



def removeFiles(destination, file_input):
	# for all folders, subfolders etc... walk through
	for dirName, subdirList, fileList in os.walk(destination):
		print('Found directory: %s' % dirName)

    	# delete specified file type
		for file_name in fileList:
			print('\t%s' % file_name)
			if (file_name.endswith('.' + file_input)):
				os.remove(os.path.join(dirName, file_name))


removeFiles(destination, file_input)

input("Press Enter to quit")

