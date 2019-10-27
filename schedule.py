#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from matplotlib import pyplot as plt


class Task:
    def __init__(self, line):
        p, r, d = [int(x) for x in line.split()]
        self.p = p
        self.r = r
        self.d = d
        self.procid = -1

    def __str__(self):
        return f"{self.p} {self.r} {self.d} {self.procid}"


class Instance:
    pass


def read_instance(path):
    with open(path, "r") as f:
        lines = f.readlines()
        x = Instance()
        x.n = int(lines[0])
        x.tasks = [Task(l) for l in lines[1:]]
        return x


def schedule(x):
    proc_time = [0, 0, 0, 0]
    for t in sorted(x.tasks, key=lambda t: t.r):
        nextproc = proc_time.index(min(proc_time))
        t.procid = nextproc
        t.start = max(proc_time[nextproc], t.r)
        proc_time[nextproc] = t.start + t.p
    return x.tasks


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, help="number of the machines")
    parser.add_argument("input", help="input file path")
    opts = parser.parse_args()

    x = read_instance(opts.input)
    x.M = opts.M

    solution = schedule(x)
    tasks_proc_map = {i: [t for t in solution if t.procid == i] for i in range(x.M)}

    total_delay = 0
    for k, v in tasks_proc_map.items():
        for t in v:
            total_delay += max(0, t.start + t.p - t.d)
    print(total_delay)

    for k, v in tasks_proc_map.items():
        X = [(t.start, t.start + t.p) for t in v]
        Y = [(k, k) for t in v]
        for x, y in zip(X, Y):
            plt.plot(x, y, marker="o")

    plt.title(f"total delay: {total_delay}")
    plt.show()
