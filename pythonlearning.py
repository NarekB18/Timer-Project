import time
def timer():
    hour, minute, second = map(int, input("Insert time to count down (h:m:s)").split(":"))
    minutes = list(range(0,60))
    seconds = list(range(0,60))
    if minute in minutes and second in seconds:
        for hou in range(hour, -1, -1):
            for minu in range(minute, -1, -1):
                for sec in range(second, -1, -1):
                    print(f"{hou:02}:{minu:02}:{sec:02}", end='\r')
                    if hour == 0 and minu == 0 and sec == 0:
                        break
                    elif minu == 0 and sec == 0:
                        minute = 59
                        second = 59
                    elif sec == 0:
                        second = 59
                    time.sleep(1)
        print('Timer completed!')
    else:
        print("ERROR")
timer()