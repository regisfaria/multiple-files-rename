'''
@author: Régis Faria
@email: regisprogramming@gmail.com
'''

import os
import re
from tqdm import tqdm

'''
in my directory i had the following setup
folder/
	samples001/
		img001-0001.png
		img001-0002.png
		img001-0003.png
		img001-0004.png
		.
		.
		.
	samples002/
		img002-0001.png
		img002-0002.png
		img002-0003.png
		.
		.
		.
	.
	.
	.

And my objective was to rename them to paste into another folder which had the same filenames
so i would only change the number string after the '-', and will not be conflicted anymore
'''


def get_current_dir():
	return os.path.dirname(os.path.realpath(__name__))

def print_folder_files(path):
    for f in os.listdir():
        print(f)

def get_all_files(path):
    file_paths = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        # this is because i dont want the first path and filenames
        path = dirpath+'/'
        files = filenames
        a = [path, files]
        #print(a)
        #q = input()
        file_paths.append(a)
    return file_paths

def rename_files(files_path):
    #'os.rename(src, dst)'
    for i in tqdm(range(0, len(files_path))):
	# the reason i skip when i=0 is that because in my first folder there are some archives as well
	# so the rest of the code would breake, bcause there isnt any img files in this folder.         
	if i == 0:
            continue
        # list[x][0] = file directory
        # list[x][1][y] = files in the dir

        # my img files are like this: 'imgxyzw-XYZW.png'
        # so i already have similar files with 'imgxyzw' in another folder
        # i want to change XYZW to a big number
        # so in when i paste theses files into another folder
        # there wont be any similar names
        for j in range(0, len(files_path[i][1])):
            img_name = files_path[i][1][j]
            folder = files_path[i][0]
            img_path = folder + img_name
            
            if len(re.findall('.swp', img_name)) > 0:
                continue
            #print('currently on dir: {}\nfile:{}'.format(folder, img_name))
            # all imgs are separed with a number from which class it is
            # and a number from which sample of that class it is
            # so 'xyzw' = class img / 'XYZW' = sample of the class img
            nlist = re.findall('\d', img_name.split('-')[1])
            new_num = ''
            for num in nlist:
                new_num += num
            new_num = str(int(new_num)+1000)

            # make the new img name and path
            new_img_name = img_name.split('-')[0] + '-' + new_num + '.png' 
            new_img_path = folder + new_img_name

            # now we will rename it
            os.rename(img_path, new_img_path)

if __name__ == "__main__":
    # get current path
    path = get_current_dir()

    # get all files from that path
    files = get_all_files(path)
    '''
    for i in range(0, len(files)):
        for j in range(0, len(files[i][1])):
            print('dir:{}\nfiles:{}'.format(files[i][0], files[i][1]))
    '''
    # rename the files
    rename_files(files)

