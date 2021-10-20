#!/usr/bin/env python
import rospy
from list_of_topics_to_delay import get_topics
from topic_delayer import TopicDelayer

if __name__ == "__main__":
    # Creates all the TopicDelayer objects from the list of topics
    rospy.init_node("teleop_delayer")
    delayers = [] #this is a delayer for each topic
    for topic_info in get_topics():
        delayers.append(TopicDelayer(topic_info))

    # Main Loop
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        for i in range(len(delayers)):
            delayers[i].dequeue()
            rate.sleep()