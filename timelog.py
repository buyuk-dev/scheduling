# -*- coding: utf-8 -*-

import time


MICROSECONDS = 1000000000


def with_time_log(task):
    """ Function decorator which prints duration time
        in microseconds to standard output.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = task(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        duration_us = int(duration * MICROSECONDS)
        print(f"task duration: {duration_us}")
        return ret

    return wrapper
