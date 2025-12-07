#!/usr/bin/env python3
"""
Module that gets the stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Gets the stats about Nginx logs stored in MongoDB.

    Args:
        mongo_collection: The MongoDB collection object.
    Returns:
        A dictionary containing the log statistics.
    """
    total_logs = mongo_collection.count_documents({})
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = {}
    for method in methods:
        method_counts[method] = mongo_collection.count_documents({'method': method})
    status_count = mongo_collection.count_documents({'status': 200})

    stats = {
        'total_logs': total_logs,
        'method_counts': method_counts,
        'status_count': status_count
    }

    return stats
