#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from matplotlib import pyplot
from instance import Instance


def plot_instance(instance):
    """ show tasks on a graph
    """
    for k, t in enumerate(instance.tasks):
        x = [t.r, t.r + t.p, t.d]
        y = [k] * len(x)
        pyplot.plot(x, y, marker="x")
    pyplot.show()


def plot_scheduling(instance, scheduling_path):
    """ plot scheduling for given instance
    """
    pass


def validate(instance, scheduling):
    """ Compute total delay for the given
        (instance, solution) pair.
    """
    raise NotImplemented()


def main(args):
    instance = None
    with open(args.instance, "r") as instance_file:
        instance = Instance.from_file(instance_file)

    if args.instance:
        plot_instance(instance)

    elif args.scheduling:
        plot_scheduling(instance, args.scheduling)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", help="instance filename")
    parser.add_argument("--scheduling", help="scheduling filename")
    args = parser.parse_args()
    main(args)
