#!/usr/bin/env python3
"""A module with tools for request caching and tracking."""

import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""The module-level Redis instance."""


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data."""
    @wraps(method)
    def invoker(url) -> str:
        """The wrapper function for caching the output."""
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        redis_store.incr(f"count:{url}")
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    return requests.get(url).text
