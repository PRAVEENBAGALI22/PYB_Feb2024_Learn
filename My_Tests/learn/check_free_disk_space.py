import shutil


def get_free_space_gb(dirname):
        try:
            # Get disk usage statistics
            disk_usage = shutil.disk_usage(dirname)

            # Calculate free space in GB
            free_space_gb = disk_usage.free / (1024 ** 3)

            print(f"Free disk space: {free_space_gb:.2f} GB")
            return free_space_gb
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


free_space_gb =get_free_space_gb("C:")
print(free_space_gb)

if free_space_gb > 200 :
    print('space available')
else:
    print('space unavailable')


