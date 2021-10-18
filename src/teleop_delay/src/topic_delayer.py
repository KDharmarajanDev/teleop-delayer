import queue
import rospy

class TopicDelayer:

    def __init__(self, topic_info):
        self.object_queue = queue.Queue()
        self.time_queue = queue.Queue()
        self.topic_info = topic_info
        self.publisher = rospy.Publisher(topic_info.name, topic_info.type)
        self.subscriber = rospy.Subscriber()
