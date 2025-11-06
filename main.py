from eyeGestures.utils import VideoCapture
from eyeGestures import EyeGestures_v2

from time import sleep


class EyeTracker:
    def __init__(self):
        # Initialize gesture engine and video capture
        self.gestures = EyeGestures_v2()
        self.cap = VideoCapture(0)
        self.calibrate = True
        self.screen_width = 1920
        self.screen_height = 1080

    def eye_position(self) -> tuple[int, int]:
        """
        Return the eye position as (x, y) coordinates.
        """

        while True:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to capture frame, retrying...")
                    sleep(0.1)
                    continue

                event, cevent = self.gestures.step(
                    frame,
                    self.calibrate,
                    self.screen_width,
                    self.screen_height,
                    context="my_context",
                )
                break
            except TypeError:
                print("Cannot detect eyes, retrying...")
                sleep(0.1)

        if event:
            return (event.point[0], event.point[1])
        return None


if __name__ == "__main__":
    eye_tracker = EyeTracker()

    while True:
        print(eye_tracker.eye_position())
