#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def evaluate(x):
    """ Dumb sequential assignmnet tasks.
    """
    proc_time = [0] * x.m
    tpm = math.ceil(x.n / x.m)
    for i, t in enumerate(x.tasks):
        t.pid = int(i / tpm)
        t.start = max(proc_time[t.pid], t.r)
        proc_time[t.pid] = t.start + t.p
    return x.tasks
