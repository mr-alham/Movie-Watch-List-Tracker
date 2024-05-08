#!/bin/env python3
"""This Python script is employed to perform a health check on the Dockerfile."""

from requests import get


def health(url, timeout=5):
    """This function checks the health by sending an HTTP GET request"""
    try:
        response = get(url, timeout=timeout)
        response.raise_for_status()

        return True

    except Exception as e:
        print(f"Health check failed: {e}")

        return False


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000'

    if health(url):
        print("Server is healthy")
        exit(0)

    else:
        print("WARNING!!! The server is Down!, I am going Down...")
        exit(1)