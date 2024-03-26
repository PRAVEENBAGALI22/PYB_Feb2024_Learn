import os

file_path = r"C:/Temp/Report.txt"
file_ptr = open(file_path, 'r')
lines = file_ptr.readlines()

for line in lines:
    passed_count = line.split().count("PASSED")
    print(passed_count)
    if passed_count == 2:
        print(line)







'''
status = 1
if status == 1:
    for l in lines:
        l = l.split(" ")
        if "FAILED" in l:
            print("FFFF")
            file_ptr = open(file_path, 'a')
            file_ptr.write(" " + "FAILED")
        elif "PASSED" in l:
            print("PPPP")
            file_ptr = open(file_path, 'a')
            file_ptr.write(" " + "PASSED")


files_to_check = ['Run.py', 'Run_MOR.py', 'Run_VE.py']
for f in files_to_check:
    print(f)

l = r'C:\\G\\Temp\\MORUnitTests\\02_ADMORE_TestBattery\\01_Non_Confidential\\01_VPS\\05_SSL_BoxBeam_VPS_7thDec2020'
print(os.path.dirname(l))
print(os.path.basename(l))
'''