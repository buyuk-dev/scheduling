#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from matplotlib import pyplot as plt


class Task:
    """ Task consists of:
        r - ready time
        p - task length
        d - due time
    """

    def __init__(self, r, p, d):
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

    @classmethod
    def from_string(cls, string):
        return cls(*[int(x) for x in string.split()])


class Instance:
    """ Instance consists of:
        m - number of processing machines
        n - number of tasks
        tasks - list of tasks to schedule
    """

    def __init__(self, m, tasks):
        self.m = m
        self.n = len(tasks)
        self.tasks = tasks

    @classmethod
    def from_file(cls, path):
        with open(path, "r") as f:
            lines = f.readlines()
            tasks = [Task.from_string(l) for l in lines[1:]]
            return cls(int(lines[0]), tasks)


def schedule(x):
    """ Greedy scheduling in ready time order.
    """
    proc_time = [0, 0, 0, 0]
    for t in sorted(x.tasks, key=lambda t: t.r):
        t.pid = proc_time.index(min(proc_time))
        t.start = max(proc_time[t.pid], t.r)
        proc_time[t.pid] = t.start + t.p
    return x.tasks


def plot_schedule(tasks):
    """ Display scheduling Gantt chart.
    """
    X = [(t.start, t.start + t.p) for t in tasks]
    Y = [(t.pid, t.pid) for t in tasks]

    for x, y in zip(X, Y):
        plt.plot(x, y, marker="o")

    plt.show()


def main(opts):
    scheduled = schedule(Instance.from_file(opts.input))

    delay = sum(t.delay() for t in scheduled)
    print(f"Total delay: {delay}")

    if opts.plot:
        plot_schedule(scheduled)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file path")
    parser.add_argument("--plot", action="store_true", help="show Gantt chart")
    main(parser.parse_args())
