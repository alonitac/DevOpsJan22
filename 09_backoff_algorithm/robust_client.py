from random import random
import requests
from loguru import logger

server_url = 'http://localhost:8080/get-data'


def exponential_backoff_retry(count, max_sec=20):
    """
    Retry in random time within an exponential increasing range of seconds

    :param count: number of failures, starting with 1
    :param max_sec: the maximum seconds to wait independently the retry count
    :return: seconds to sleep before next retry
    """
    return min(max_sec, (2 ** (count - 1) - 1) * random())


def exponential_retry(count, max_sec=20):
    """
    Retry in exponential increasing number of seconds + some small random change

    :param count: number of failures, starting with 1
    :param max_sec: the maximum seconds to wait independently the retry count
    :return: seconds to sleep before next retry

    """
    return min(max_sec, (2 ** (count - 1) - 1) + random())


def linear_retry(count):
    """
    Retry in number of seconds linearly dependent of the retry count

    :param count: number of failures, starting with 1
    :return: seconds to sleep before next retry
    """
    return 2 * count


def constant_retry():
    """
    Retry in constant value of seconds

    :return: seconds to sleep before next retry
    """
    return 5


def get_data_from_server():
    # TODO implement backoff retry
    logger.info('Getting user data from external server')
    data = requests.get(server_url)


def get_data_from_server_recursive():
    pass      # TODO implement backoff retry


if __name__ == '__main__':
    get_data_from_server()
