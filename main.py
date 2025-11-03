class EyeTracker:
    def eye_position(self) -> tuple[int, int]:
        return (0, 0)


if __name__ == "__main__":
    eye_tracker = EyeTracker()
    print(eye_tracker.eye_position())
