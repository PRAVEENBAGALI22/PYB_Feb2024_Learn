import os
import shutil

dir = os.path.join(os.path.expanduser("~"), "Downloads")

print(dir)
extensions = {
    '.doc': "Documents",
    '.pdf': "Documents",
    '.txt': "Documents",
    '.xlx': "Documents",
    '.ppt': "Documents",
    '.pptx': "Documents",
    '.xls': "Documents",
    '.xlsx': "Documents",
    '.docx': "Documents",
    '.jpg': "Images",
    '.png': "Images",
    '.gif': "Images",
    '.mp4': "Videos",
    '.avi': "Videos",
    '.py': "WorkRelated",
    '.csv': "WorkRelated",
    '.lic': "WorkRelated",
    '.pc': "WorkRelated",
    '.xml': "WorkRelated",
    '.inc': "WorkRelated",
}

for filename in os.listdir(dir):
    filepath = os.path.join(dir, filename)
    print(filename)
    print(filepath)

    if os.path.isfile(filepath):
        extension = os.path.splitext(filepath)[1].lower()
        print(extension)

        if extension in extensions:
            folder_name = extensions[extension]
            print(folder_name)

            folder_path = os.path.join(dir, folder_name)
            os.makedirs(folder_path,exist_ok=True)
            print(folder_path)

            destination_path = os.path.join(folder_path, filename)
            print(destination_path)
            shutil.move(filepath,destination_path)

            print(f"Moved {filename} to {folder_name} folder")

        else:
            print(f"Skipped {filename} , unknown file extension ")
    else:
        print(f"Skipped {filename} , Is it a directory ")