#!/usr/bin/env python3
"""List schools by topic in a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """Lists all schools that have a specific topic.

    Args:
        mongo_collection: The MongoDB collection object.
        topic: The topic to filter schools by.

    Returns:
        A list of schools that have the specified topic.
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
