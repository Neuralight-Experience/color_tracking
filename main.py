import cv2
import color_tracker
from neura_tracker import NeuraTracker

def tracker_callback(tracker: NeuraTracker, static_data : list) -> None:
    '''
    Callback to handle tracker data
    '''
    cv2.imshow("debug", tracker.debug_frame)
    static_data = tracker.get_tracked_points()
    print(static_data)
    cv2.waitKey(1)

'''
Data about color motion to be accessed
'''
static_data = []

'''
Create tracker and set callback
'''
tracker = NeuraTracker(max_nb_of_objects=1, max_nb_of_points=20, debug=True)
# tracker passes only itself as argument to the callback so a lambda is used
# for handling other arguments
tracker.set_tracking_callback(lambda tracker: tracker_callback(tracker, static_data))

'''
Track webcam, press ctrl+c to exit

Run hsv_detector.py to understand HSV values of the object you want to track
'''
with color_tracker.WebCamera() as cam:
    # Define your custom Lower and Upper HSV values
    tracker.track(cam, [8, 255, 126], [18, 255, 158], max_skipped_frames=24)