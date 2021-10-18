import rospy

class TopicInfo:

    def __init__(self, name, message_type):
        self.name = name
        self.type = message_type