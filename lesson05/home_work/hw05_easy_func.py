import os

def change_dir(curr_dir):
    os.chdir(curr_dir)
def create_folder_func(curr_dir, number):
    os.mkdir(str(number), mode=511, dir_fd=None)
def remove_folder_func(curr_dir, number_1):
    os.removedirs(str(number_1))
def look_func(curr_dir):
    print(list(os.listdir(curr_dir)))
