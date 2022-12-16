from collections import defaultdict
from sensor_msgs.msg import CompressedImage

subscribers = defaultdict(list)



def subscribe(event_type, fn):
    subscribers[event_type].append(fn)
    print(subscribers)

def post_event(event_type, data=None): 
    print(subscribers)
    if event_type in subscribers:

        for fn in subscribers[event_type]:
            fn(data)