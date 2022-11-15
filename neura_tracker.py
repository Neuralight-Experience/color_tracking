from color_tracker import ColorTracker

class NeuraTracker(ColorTracker):
    def __init__(self, max_nb_of_objects: int = 1, max_nb_of_points: int = None, debug: bool = True):
        super().__init__(max_nb_of_objects, max_nb_of_points, debug)

    def get_tracked_points(self) -> list:
        return self._tracked_objects[0]._tracked_points