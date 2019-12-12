#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timelog
import math


@timelog.with_time_log
def urgent_scheduler(x):
    """ Greedy scheduling in ready time order.
    """
    proc_time = [0] * x.m
    sort_key = iter(range(x.n))
    for t in sorted(x.tasks, key=lambda t: t.d):
        t.pid = proc_time.index(min(proc_time))
        t.start = max(proc_time[t.pid], t.r)
        t.sort_key = next(sort_key)
        proc_time[t.pid] = t.start + t.p
    return x.tasks


@timelog.with_time_log
def fifo_scheduler(x):
    """ Greedy scheduling in ready time order.
    """
    proc_time = [0] * x.m
    sort_key = iter(range(x.n))
    for t in sorted(x.tasks, key=lambda a: a.r):
        t.pid = proc_time.index(min(proc_time))
        t.start = max(proc_time[t.pid], t.r)
        t.sort_key = next(sort_key)
        proc_time[t.pid] = t.start + t.p
    return x.tasks


@timelog.with_time_log
def reference_scheduler(x):
    """ Split tasks sequence into four equal-size parts and assign
        each subset to different machine.
    """
    proc_time = [0] * x.m
    tpm = math.ceil(x.n / x.m)
    sort_key = iter(range(x.n))
    for i, t in enumerate(x.tasks):
        t.pid = int(i / tpm)
        t.start = max(proc_time[t.pid], t.r)
        t.sort_key = next(sort_key)
        proc_time[t.pid] = t.start + t.p
    return x.tasks
