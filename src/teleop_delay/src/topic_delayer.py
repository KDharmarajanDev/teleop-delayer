import queue
import rospy
import delay_time_function

class TopicDelayer:

    def __init__(self, topic_info):
        self.object_queue = queue.Queue()
        self.topic_info = topic_info

        self.publisher = rospy.Publisher(topic_info.name + "_delayed", topic_info.type)
        self.subscriber = rospy.Subscriber(topic_info.name, topic_info.type, self.enqueue)

    def enqueue(self, message):
        try:
            self.object_queue.put_nowait((message, rospy.get_time()))
        except queue.Full:
            pass
        return

    def dequeue(self):
        if not self.object_queue.empty():
            data = self.object_queue.queue[0]
            if rospy.get_time() >= data[1] + delay_time_function.get_delay():
                data = self.object_queue.get_nowait()[0]
                self.publisher.publish(data)