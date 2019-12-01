#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
from collections import namedtuple
from matplotlib import pyplot

from task import Task


def random_tasks_generator(opts):
    """ random tasks generator
    """
    for i in range(opts.n):
        p = random.randint(int(0.25 * opts.pmax), opts.pmax)
        r = random.randint(0, int(0.5 * opts.pmax))
        d = random.randint(r + p, r + int(1.5 * p))
        yield Task(p, r, d)


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

    print(f"{len(tasks)}")
    for t in tasks:
        print(t)

    if opts.plot:
        plot(tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="number of tasks")
    parser.add_argument("--m", type=int, help="processors number")
    parser.add_argument("--pmax", type=int, help="max task length")
    parser.add_argument("--plot", action="store_true", help="plot generated tasks")
    main(parser.parse_args())
