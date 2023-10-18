#!/usr/bin/env python3
""" List all the documents in Python """
import pymongo


def list_all(mongo_collection):
    """ lists all documents in collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
