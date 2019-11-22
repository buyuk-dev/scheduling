#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Task:
    """ Task consists of:
        r - ready time
        p - task length
        d - due time
    """
    def __init__(self, r, p, d):
        self.id = self.next_id()
        self.r = r
        self.p = p
        self.d = d
        self.pid = -1
        self.start = -1

    def delay(self):
        assert self.start >= 0, "Cannot compute delay of unscheduled task."
        return max(0, self.start + self.p - self.d)

    def __str__(self):
        return f"{self.r} {self.p} {self.d}"

    def __repr__(self):
        return f"<{self.id}>"

    @classmethod
    def from_string(cls, string):
        return cls(*[int(x) for x in string.split()])

    @classmethod
    def next_id(cls):
        cls._next_id += 1
        return cls._next_id - 1
    
    _next_id = 0

