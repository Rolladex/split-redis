# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:52:59 2023

@author: https://github.com/Rolladex
"""

import redis

def move_half_between_dbs():
    # Connect to the Redis server
    redis_client = redis.Redis(host='localhost', port=6379)

    # Prompt the user for source and destination database numbers
    source_db = int(input("Enter the source database number (0-15): "))
    dest_db = int(input("Enter the destination database number (0-15): "))

    # Check if source and destination DBs are within limits
    if not (0 <= source_db <= 15) or not (0 <= dest_db <= 15):
        print("Invalid database numbers. They should be between 0 and 15.")
        return

    # Retrieve keys from the source database
    source_keys = []
    for _, keys in redis_client.scan_iter(match='*', count=1000, db=source_db): # Fetch keys in chunks to prevent blocking the server. Default 1000
        source_keys.extend(keys)

    half_length = len(source_keys) // 2
    keys_to_move = source_keys[:half_length]

    # Move data to the destination database
    for key in keys_to_move:
        value = redis_client.get(key, db=source_db)
        redis_client.set(key, value, db=dest_db)

    # Delete keys from the source database
    for key in keys_to_move:
        redis_client.delete(key, db=source_db)

if __name__ == "__main__":
    move_half_between_dbs()
