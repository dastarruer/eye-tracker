from eyeGestures.utils import VideoCapture
from eyeGestures import EyeGestures_v2

from time import sleep

class EyeTracker:
    def __init__(self):
        # Initialize gesture engine and video capture
        self._gestures = EyeGestures_v2()
        self._cap = VideoCapture(0)
        self._calibrate = True
        self._screen_width = 1920
        self._screen_height = 1080

    def eye_position(self) -> tuple[int, int]:
        """
        Return the eye position as (x, y) coordinates.
        """

        ret, frame = self._cap.read()
        # TODO: This function keeps throwing an error whenever it cannot detect a face/eyes
        event, cevent = self._gestures.step(
            frame, self._calibrate, self._screen_width, self._screen_height, context="my_context"
        )

        if event:
            return(event.point[0], event.point[1])
        return None


if __name__ == "__main__":
    eye_tracker = EyeTracker()

    while True:
        print(eye_tracker.eye_position())
        sleep(0.1)


