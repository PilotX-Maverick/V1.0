#device types that can be selected by user has been summarised into these two list: 
#list_of_ac = ["BLDC Motor", "DC Motor EN_A", "DC Motor EN_B", "Servo 180", "Servo 360", "RC_1", "RC_2", "RC_3", "RC_4", "RC_5", "RC_6", "RC_7", "RC_8", "Switch", "Analog Sensor", "None"]
#list_of_sensors = ["HC-SR04", "MPU6050", "MPU6000", "BMP180", "HMCL5883", "APDS9960", "None"]
#this list has been further divided into groups, but is not relevant to this snippet

def node_validation():
    final_list = [menu_new1.get(), menu_new2.get(), menu_new3.get(), menu_new4.get(), menu_new5.get(), menu_new6.get(), menu_new7.get(), menu_new8.get(), menu_new9.get(), menu_new10.get(), menu_new11.get(), menu_new12.get(), menu_new13.get(), menu_new14.get(), menu_new15.get(), menu_new16.get(), menu_new17.get()]
    DC_A = final_list.count("DC Motor EN_A")
    DC_B = final_list.count("DC Motor EN_B")
    BLDC = final_list.count("BLDC Motor")
    servo180 = final_list.count("Servo 180")
    servo360 = final_list.count("Servo 360")
    RC = sum("RC" in item for item in final_list)
    print(DC_A, DC_B, BLDC, servo360, servo180, RC)
    flag = 0
    message = ""

    if (DC_A != DC_B):
        flag = 0
        coloring = "Red"
        message = "Node Validation Failed! \n[ERROR: DC Motors EN_A and EN_B must co-exist]"
    elif (BLDC == 0) and (DC_A == 0):
        flag = 0
        coloring = "Red"
        message = "Node Validation Failed! \n[ERROR: No Motors Found!]"
    elif (BLDC == 1) or (DC_A == 1 and DC_B == 1):
        flag = 1
        coloring = "Orange"
        message = "Node Validation Successful! \n[WARNING: Only One Motor Exists, Axis Turn is not possible!]"
    elif (servo360 == 0) or (servo180 == 0):
        flag = 1
        coloring = "Orange"
        message = "Node Validation Successful! \n[WARNING: Steering Feature Unavailable]"
    elif (RC == 0):
        flag = 1
        coloring = "Orange"
        message = "Node Validation Successful! \n[WARNING: No Input Channel Available, MANUAL mode disabled]"
    else:
        flag = 1
        coloring = "Green"
        message = "Node Validation Successful!"

    validation_window = tkinter.Toplevel(gui)
    validation_window.title("Node Validation")
    validation_window.iconbitmap('PilotX Assets\PilotX Assets\Iterations In Use\onlyfg3.ico')

    validation_window.geometry("470x160+310+240")
    validation_window.resizable(width=False, height=False)

    validation_message = tkinter.Label(validation_window, text= message, font=("Helvetica Bold", 10), foreground=coloring, justify="center")
    validation_message.place(x=75, y=35)

    validation_Button = Button(validation_window, text="Okay", height=2, width=7, command=validation_window.destroy, background=coloring)
    validation_Button.place(x=220, y=90)
