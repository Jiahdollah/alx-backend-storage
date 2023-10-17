#!/usr/bin/env python3
""" Inserts  document in Python """


def insert_school(mongo_collection, **kwargs):
    """ inserts  new document in a collection based on kwargs,
    Returns  new _id """
    return mongo_collection.insert_one(kwargs).inserted_id
