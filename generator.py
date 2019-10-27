#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
from collections import namedtuple
from matplotlib import pyplot


Task = namedtuple("Task", ["r", "p", "d"])


def random_tasks_generator(opts):
    """ random tasks generator
    """
    for i in range(opts.n):
        p = random.randint(1, opts.pmax)
        r = random.randint(0, opts.dmax - p)

        dmax = min(opts.dmax, int((r + p) * 1.25))
        d = random.randint(r + p, opts.dmax)

        yield Task(r, p, d)


def plot(tasks):
    """ show tasks on a graph
    """
    for k, t in enumerate(tasks):
        x = [t.r, t.r + t.p, t.d]
        y = [k] * len(x)

        pyplot.plot(x, y, marker="o")
    pyplot.show()


def main(opts):
    """ generate random tasks for the given parameters
    """
    tasks = [t for t in random_tasks_generator(opts)]

    print(f"{opts.m}")
    for t in tasks:
        print(f"{t.r} {t.p} {t.d}")

    if opts.plot:
        plot(tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="number of tasks")
    parser.add_argument("--dmax", type=int, help="upper due time limit")
    parser.add_argument("--m", type=int, help="processors number")
    parser.add_argument("--pmax", type=int, help="max task length")
    parser.add_argument("--plot", action="store_true", help="plot generated tasks")
    main(parser.parse_args())
