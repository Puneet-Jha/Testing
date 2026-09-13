import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

def obstacle_avoidance():
    rospy.init_node('obstacle_avoidance')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    safe_distance = 0.5  # meters
    rate = rospy.Rate(10)  # 10 Hz loop

    while not rospy.is_shutdown():
        # Sense: get distance from sensor 
        distance = get_sensor_reading()  # Replace with actual sensor callback

        move_cmd = Twist()

        if distance > safe_distance:
            # Move forward
            move_cmd.linear.x = 0.2
            move_cmd.angular.z = 0.0
        else:
            # Stop first
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)
            rospy.sleep(1)

            # Then turn
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.5  # rotate in place
            rospy.sleep(1)

        pub.publish(move_cmd)
        rate.sleep()

def get_sensor_reading():
    # Placeholder function: in real ROS, you'd subscribe to /sensor_topic
    # and update distance from sensor_msgs/Range
    return 1.0  # mock value (no obstacle)

if __name__ == '__main__':
    try:
        obstacle_avoidance()
    except rospy.ROSInterruptException:
        pass
