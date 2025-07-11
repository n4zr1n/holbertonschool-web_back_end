#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
def log_stats(mongo_collection):
    """ Returns and prints"""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = mongo_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{status_count} status check")
                                                     

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)