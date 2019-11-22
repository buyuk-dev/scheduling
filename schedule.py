#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
from pprint import pprint
from matplotlib import pyplot as plt

from instance import Instance
from greedy import schedule
#from smart import schedule


def plot_schedule(tasks):
    """ Display scheduling Gantt chart.
    """
    X = [(t.start, t.start + t.p) for t in tasks]
    Y = [(t.pid, t.pid) for t in tasks]

    for x, y in zip(X, Y):
        plt.plot(x, y, marker="o")

    plt.show()


def print_schedule(tasks):
    """ Print scheduling.
    """
    delay = sum(t.delay() for t in tasks)
    print(f"Total delay: {delay}")

    proc_to_tasks = {}
    for t in tasks:
        if t.pid not in proc_to_tasks:
            proc_to_tasks[t.pid] = [t]
        else:
            proc_to_tasks[t.pid].append(t)

    for pid in proc_to_tasks:
        proc_to_tasks[pid] = sorted(proc_to_tasks[pid], key=lambda t: t.start)

    pprint(proc_to_tasks)


def main(opts):
    """ Main.
    """
    try:
        scheduled = schedule(Instance.from_file(opts.input))
        opts.input.close()
        print_schedule(scheduled)
        if opts.plot:
            plot_schedule(scheduled)
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
    finally:
        opts.input.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=argparse.FileType("r"),
        nargs="?",
        default=sys.stdin,
        help="input file path. stdin will be used if ommited",
    )
    parser.add_argument("--plot", action="store_true", help="show Gantt chart")
    main(parser.parse_args())
