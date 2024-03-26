from datetime import datetime

date_today = datetime.now()
print(str(date_today))


current_time= datetime.today().strftime("%Y-%m-%d %H-%M-%S")
print(current_time)

file_name = f"{current_time}.txt"
print(file_name)

f1 = open(file_name, 'a')
f1.write("sasdasd")
f1.close()