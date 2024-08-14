#!/usr/bin/env python3
""" Main file """

import redis
get_page = __import__('web').get_page

redis_store = redis.Redis()


if __name__ == "__main__":
    # Example usage:
    url = "https://redis-py.readthedocs.io/"
    html_content = get_page(url)
    print(f"Content for {url}:\n{html_content}\n")
    
    # You can access the access count from Redis if needed
    count_key = f"count:{url}"
    access_count = int(redis_store.get(count_key).decode())
    print(f"Access count for {url}: {access_count}")

