line1 = ('G:/Temp/MORUnitTests/02_ADMORE_TestBattery/01_Non_Confidential/01_VPS/01_SSL_Demo_Tyre_VPS'
        '/01_SSL_Demo_Tyre_VPS.eprf:	6053980')
line2 = ('U:/MORUnitTests/02_ADMORE_TestBattery/01_Non_Confidential/01_VPS/01_SSL_Demo_Tyre_VPS'
        '/01_SSL_Demo_Tyre_VPS.eprf:	6053984')

check_line1 = line1[20:]
check_line2 = line2[15:]

if check_line1 == check_line2:
    print("match: ", line1)
else:
    print("doesnt match")
    print(line1)
    print(line2)
