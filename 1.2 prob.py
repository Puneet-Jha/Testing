# Distance threshold 
OBSTACLE_DISTANCE = 20 

while True:
    distance = get_distance()
  
    if distance > OBSTACLE_DISTANCE:

        left_motor_forward()
        right_motor_forward()

    else:

        left_motor_stop()
        right_motor_stop()


        left_motor_forward()
        right_motor_backward()
