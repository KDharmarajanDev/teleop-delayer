from topic_info import TopicInfo
from std_msgs.msg import Header

topics = [TopicInfo("/test", Header)]

def get_topics():
    return topics