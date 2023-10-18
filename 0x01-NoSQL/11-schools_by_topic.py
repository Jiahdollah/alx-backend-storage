#!/usr/bin/env python3
""" where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ returns  list of school having a specific topic """
    return mongo_collection.find({ "topics": topic })
