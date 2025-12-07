#!/usr/bin/env python3
"""
Update topics in a MongoDB document
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a document in a MongoDB collection based on the name.

    Args:
        mongo_collection: The MongoDB collection object.
        name: The name of the document to update.
        topics: A list of topics to set for the document.

    Returns:
        The updated document.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
