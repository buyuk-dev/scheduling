#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
from matplotlib import pyplot


def random_tasks_generator(n, rmin, dmax, pmax):
    ''' random tasks generator
    '''
    for i in range(n):
        p = random.randint(1, pmax)
        r = random.randint(rmin, dmax - p)

        margin = int((r + p) * 1.25)
        d = random.randint(r + p, min(dmax, margin))

        yield p, r, d


def plot(tasks):
    ''' show tasks on a graph
    '''
    for k, (p, r, d) in enumerate(tasks):
        x = [r, r+p, d]
        y = [k, k, k]
        pyplot.plot(x, y, marker="o")
    pyplot.show()
   

def main(opts):
    ''' generate random tasks for the given parameters
    '''
    gen = random_tasks_generator(opts.n, opts.rmin, opts.dmax, opts.pmax)
    tasks = [t for t in gen]

    print(opts.n)
    for t in tasks:
        print(f"{t.r} {t.p} {t.d}")

    if opts.plot:
        plot(tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="number of tasks")
    parser.add_argument("--rmin", type=int, help="lower ready time limit")
    parser.add_argument("--dmax", type=int, help="upper due time limit")
    parser.add_argument("--pmax", type=int, help="max task length")
    parser.add_argument("--plot", action='store_true', help="plot generated tasks")
    opts = parser.parse_args()

    if opts.pmax is None:
        opts.pmax = opts.dmax

    main(opts)

