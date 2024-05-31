# car
print("Command :- start,stop,help,quit")
command=""
started=False
while True:
    command=input(">").lower()
    if command =="start":
        if started:
            print("Car_is_already_started!")
        else:
             started=True
             print("Car_started..")
    elif command=="stop":
        if not started:
            print("Car_is_already_started")
        else:
            started=False
            print("Car_stopped...")
    elif command=="help":
        print('''
        start-to_start_the_car
        stop-to_stop_the_car
        quit-to_quit
        ''')
    elif command=="quit":
        break
    else:
        print("Sorry,I_don't_understand_that!")