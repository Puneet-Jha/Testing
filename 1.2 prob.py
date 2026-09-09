# Distance threshold 
SAFE_DISTANCE = 20 

while True:
    distance = get_distance()
    #get_distance = input quantity from sensors
  
    if distance > OBSTACLE_DISTANCE:

        # Following functions are to move the motor forward
        left_motor_forward()
        right_motor_forward()

    else:

        # Following functions are to move the motor in the desired manner
        left_motor_stop()
        right_motor_stop()

        left_motor_forward()
        right_motor_backward()
