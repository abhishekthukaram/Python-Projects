"""
def next_validip(input_ip):
    convert = input_ip.split(".")
    print(convert)
    if int(convert[3]) < 255:
        convert[3] = int(convert[3])+1
    elif (int(convert[3]) >= 255) and (int(convert[2]) < 255):
        convert[3] = 0
        convert[2] = int(convert[2]) +1
    elif ((int(convert[3]) and int(convert[2])) >=255) and int(convert[1])<255:
        convert[3], convert[2] = 0,0
        convert[1] = int(convert[1])+1
    elif (int(convert[3] and int(convert[2] and int(convert[1]))) >= 255) and int(convert[0]) < 255:
        print("Reached here")
        convert[3], convert[2], convert[1] = 0,0, 0
        print(convert[0])
        convert[0] = int(convert[0])+1

    print(convert)
    #elif int(convert[2])
"""


import re

"""
def check_validip(string_ip):
    reg = r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]| 2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|2[0-4][0-9]|25[0-5])$'
    matching = re.match(reg, string_ip)
    if matching:
        print("OncE")
        return True
    else:
        print("TWICE")
        return  False

def next_valid_ip(input_string):
    convert = input_string.split(".")
    ip_temp = ""
    for i in range(len(convert)- 1, -1, -1):
        temp_value = int(convert[i]) + 1
        convert[i] = str(temp_value)
        print(convert)
        ip_temp = ".".join(convert)
        if check_validip(ip_temp):
            print("reached here")
            break
        else:
            convert[i] = str(0)
    final_ip = ".".join(convert)
    print("IP",final_ip)
    return ip_temp

"""
#print(next_valid_ip("255.255.255.255"))

def next_valid_ip(input_string):
    convert = input_string.split(".")
    if int(convert[3]) == 255:
        if int(convert[2]) == 255:
            if int(convert[1]) == 255:
                if int(convert[0]) == 255:
                    return "INvalid IP address"
                else:
                    convert[3], convert[2], convert[1] = str(0),str(0),str(0)
                    convert[1] = str(int(convert[1])+1)
            else:
                convert[3], convert[2] = str(0), str(0)
                convert[1] = str(int(convert[1])+1)
        else:
            convert[3] = str(0)
            convert[2]= str(int(convert[2])+1)
    else:
        convert[3] = str(int(convert[3])+1)
    result = ".".join(convert)
    print(result)
    print(convert)


print(next_valid_ip("10.251.251.254"))


"""

               ip_temp = ""
    for i in range(len(convert)- 1, -1, -1):
        temp_value = int(convert[i]) + 1
        convert[i] = str(temp_value)
        print(convert)
        ip_temp = ".".join(convert)
        if check_validip(ip_temp):
            print("reached here")
            break
        else:
            convert[i] = str(0)
    final_ip = ".".join(convert)
    print("IP",final_ip)
    return ip_temp

"""


"""
    for i in range(len(convert) - 1, -1, -1):
        print(convert[i])
        if int(convert[i]) < 255:
            convert[i] = 
        elif int(convert[i]) == 255:
            convert[i] = 0
            convert[i - 1] = int(convert[i - 1]) + 1
            break
    print(convert)
    # print(convert[i-1])
    """

#print(next_validip("2.254.254.255"))

#print(next_validip("2.2.255.25"))

"""

current, previous = len(convert)-1, len(convert)-1
    n = len(convert)
    while n>=0:
        if int(convert[n-1]) < 255:
            convert[n-1] = str(int(convert[n-1])+1)
            n-=1
            break
        elif int(convert[n-1]) == 255:
            convert[n-1] = 0
            convert[n-2] = str(int(convert[n-2]) +1)
            n-=2
            break
    return convert

    
    

next_validip("2.2.255.255")


#last = len(input_ip)-1
"""
