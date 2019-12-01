#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task import Task


class Instance:
    """ Instance consists of:
        m - number of processing machines
        n - number of tasks
        tasks - list of tasks to schedule
    """

    def __init__(self, m, tasks):
        """ Instance consists of number of processors m, and list of n tasks.
        """
        self.m = m
        self.n = len(tasks)
        self.tasks = tasks

    @classmethod
    def from_file(cls, file_):
        """ Create new instance from file.
        """
        n = int(file_.readline())
        m = 4
        tasks = [Task.from_string(file_.readline()) for i in range(n)]
        return cls(m, tasks)
