input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

for key, value in input_dict.items():
    # print(key," : ",value)
    if value is not None:
        print(str(key)+" : "+str(value))