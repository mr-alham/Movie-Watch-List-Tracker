#!/bin/env python3
"""This Python script is employed to perform a health check on the Dockerfile."""

from sys import exit as bye  # pylint: disable=import-error

from requests import get  # pylint: disable=import-error


def health(url, timeout=5):
    """This function checks the health by sending an HTTP GET request"""
    try:
        response = get(url, timeout=timeout)
        response.raise_for_status()

        return True

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Health check failed: {e}")

        return False


if __name__ == "__main__":
    URL = "http://127.0.0.1:8000"

    if health(URL):
        print("Server is healthy")
        bye(0)

    else:
        print("WARNING!!! The server is Down!, I am going Down...")
        bye(1)
