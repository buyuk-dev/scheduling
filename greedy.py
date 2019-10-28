# -*- coding: utf-8 -*-


def schedule(x):
    """ Greedy scheduling in ready time order.
    """
    proc_time = [0] * x.m
    for t in sorted(x.tasks, key=lambda t: t.r):
        t.pid = proc_time.index(min(proc_time))
        t.start = max(proc_time[t.pid], t.r)
        proc_time[t.pid] = t.start + t.p
    return x.tasks

