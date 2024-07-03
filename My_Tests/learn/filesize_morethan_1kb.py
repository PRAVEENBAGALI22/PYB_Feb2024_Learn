import os

# Directory path containing the .txt files
directory_path = r"C:\Users\pyb\Documents\VE\18_0\Logs"
print(directory_path)

content_file = r"C:\Users\pyb\Documents\VE\content_file.txt"

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.log'):
        file_path = os.path.join(directory_path, filename)
        # Check file size in bytes
        file_size_kb = os.path.getsize(file_path) / 1024
        if file_size_kb > 1:
            print(f"{filename}: {file_size_kb:.2f} KB")
            f1 = open(file_path,'r')
            lines = f1.readlines()
            lines_to_wr = lines[0:3]
            for l in lines_to_wr:
                f3 = open(content_file,'a')
                f3.write(l)
                f3.write('\n')


