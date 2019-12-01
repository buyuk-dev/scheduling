#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Task:
    """ Task consists of:
        r - ready time
        p - task length
        d - due time
    """

    def __init__(self, p, r, d):
        """ Single task representation.
        """
        self.id = self.next_id()
        self.r = r
        self.p = p
        self.d = d
        self.pid = -1
        self.start = -1

    def delay(self):
        """ Compute delay for the tasks.
            This method assumes that scheduling params have been filled before call.
        """
        assert self.start >= 0, "Cannot compute delay of unscheduled task."
        return max(0, self.start + self.p - self.d)

    def __str__(self):
        """ Task representation used in generator output.
        """
        return f"{self.r} {self.p} {self.d}"

    def __repr__(self):
        """ Task representation used for debug prints.
        """
        return f"<{self.id}>"

    @classmethod
    def from_string(cls, string):
        """ Parse task from text.
        """
        return cls(*[int(x) for x in string.split()])

    @classmethod
    def next_id(cls):
        """ Assign new task id.
        """
        cls._next_id += 1
        return cls._next_id - 1

    _next_id = 0
