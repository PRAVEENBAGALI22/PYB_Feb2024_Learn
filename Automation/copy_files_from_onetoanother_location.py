import os
import shutil

print("----------------File copying is Started----------------")


def copy_files(file_lst, source_dir, dest_dir):
    try:

        for index, file_to_copy in enumerate(file_lst):
            print(file_lst)
            source_path = os.path.join(source_dir, file_to_copy)
            print(source_path)

            # Check if the source file exists
            if os.path.exists(source_path):
                dest_path = os.path.join(dest_dir, file_to_copy)
                shutil.copy(source_path, dest_path)
                print(f"File '{file_to_copy}' copied to '{dest_dir}'")
            else:
                print(f"File '{file_to_copy}' not found in '{source_dir}'")

    except Exception as e:
        print(f"An error occurred: {e}")


source_directory = r'C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\filetocpy'
destination_file_path = r'C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\scipts\destination_file_path.txt'
files_to_copy = ['Run.py', 'Run_MOR.py', 'Run_VE.py']

# Read destination directories from the text file
with open(destination_file_path, 'r') as dest_file:
    destination_dirs = dest_file.read().splitlines()
    print(destination_dirs)
for index, dest_dir in enumerate(destination_dirs):
    if dest_dir:
        if not dest_dir.startswith("#"):
            copy_files(files_to_copy, source_directory, dest_dir)

print("----------------File copying is Completed----------------")
print("---------------------------------------------------------")
print("----------------File Renaming is Started-----------------")


def rename_files_with_folder_name(destination_file):
    try:
        files_to_check = ['Run.py', 'Run_MOR.py', 'Run_VE.py']

        # Read destination directories from the text file
        with open(destination_file, 'r') as dest_file:
            destination_dirs = dest_file.read().splitlines()

        for dest_dir in destination_dirs:
            study_folder_name = os.path.basename(dest_dir)
            filename_lst = []

            # Iterate through each file in the directory
            for filename in os.listdir(dest_dir):
                file_path = os.path.join(dest_dir, filename)
                file_name = os.path.basename(file_path)
                filename_lst.append(filename)
            print('Files present in current directory', filename_lst)

            if all(f in filename_lst for f in files_to_check):
                for file_to_rename in filename_lst:
                    if file_to_rename == 'Run.py':
                        os.rename(os.path.join(dest_dir, file_to_rename),
                                  (os.path.join(dest_dir, study_folder_name + '.py')))
                        print(f'File', os.path.join(dest_dir, file_to_rename), 'renamed to',
                              os.path.join(dest_dir, study_folder_name + '.py'))
                    elif file_to_rename == 'Run_MOR.py':
                        os.rename(os.path.join(dest_dir, file_to_rename),
                                  (os.path.join(dest_dir, study_folder_name + '_MOR.py')))
                        print(f'File', os.path.join(dest_dir, file_to_rename), 'renamed to',
                              os.path.join(dest_dir, study_folder_name + '_MOR.py'))
                    elif file_to_rename == 'Run_VE.py':
                        os.rename(os.path.join(dest_dir, file_to_rename),
                                  (os.path.join(dest_dir, study_folder_name + '_VE.py')))
                        print(f'File', os.path.join(dest_dir, file_to_rename), 'renamed to',
                              os.path.join(dest_dir, study_folder_name + '_VE.py'))
                        print("Operation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


destination_file_path1 = r'C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\destination_file_path.txt'
rename_files_with_folder_name(destination_file_path)
print("----------------File Renaming is Completed----------------")

print("-----------------Final Filelist Preparing-----------------")


def prepare_final_filelist(destination_file, fileset_path):
    try:
        # Read destination directories from the text file
        with open(destination_file, 'r') as dest_file:
            destination_dirs = dest_file.read().splitlines()

        for dest_dir in destination_dirs:
            study_folder_name = os.path.basename(dest_dir)
            main_file = (os.path.join(dest_dir, study_folder_name + '.py'))
            if os.path.exists(main_file):
                f = open(fileset_path, 'a')
                f.write(main_file)
                f.write('\n')
                print(
                    f"The main file {main_file} ,is found in the directory {dest_dir}. This is written to final-list "
                    f"file")
            else:
                print(f"The main file {main_file} ,is not found in the directory {dest_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")


destination_file_path2 = r'C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\destination_file_path.txt'
final_fileset_path = r"C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\TestCase_List.txt"
prepare_final_filelist(destination_file_path, final_fileset_path)

print("-----------------Final Filelist Completed-----------------")
