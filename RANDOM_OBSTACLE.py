import time
import random

class ObstacleAvoider:
    def __init__(self, stop_distance=0.5, forward_speed=0.2, turn_speed=0.8):
        self.stop_distance = stop_distance
        self.forward_speed = forward_speed
        self.turn_speed = turn_speed
        self.distance = float("inf")

    def get_sensor_reading(self):
        """Simulate a distance sensor (replace with real hardware code)."""
        # Randomly simulate obstacle detection
        return random.uniform(0.2, 2.0)

    def stop_robot(self):
        print("STOP: Motors off")

    def move_forward(self):
        print(f"FORWARD: Speed {self.forward_speed}")

    def turn_robot(self):
        direction = random.choice(["left", "right"])
        print(f"TURN {direction}: Angular speed {self.turn_speed}")

    def run(self):
        while True:
            self.distance = self.get_sensor_reading()
            print(f"Sensor distance: {self.distance:.2f} m")

            if self.distance <= self.stop_distance:
                self.stop_robot()
                time.sleep(0.2)
                self.turn_robot()
            else:
                self.move_forward()

            time.sleep(1)  # loop delay

if __name__ == "__main__":
    try:
        ObstacleAvoider().run()
    except KeyboardInterrupt:
        print("Program stopped")
