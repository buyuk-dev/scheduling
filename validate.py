#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import instance
import itertools

def read_solution_file(path):
    with open(path) as fsol:
        lines = fsol.read().splitlines()
        value = int(lines[0])
        scheduling = [
            [int(tid) for tid in line.strip().split()]
            for line in lines[1:]
        ]
        return value, scheduling


def compute_scheduling_value(inst, scheduling):
    proc_time = [0] * inst.m
    total_delay = 0
    for pid, processor in enumerate(scheduling):
        for tid in processor:
            tid = tid - 1
            start = max(proc_time[pid], inst.tasks[tid].r)
            end = start + inst.tasks[tid].p
            proc_time[pid] = end
            inst.tasks[tid].start = start
            inst.tasks[tid].pid = pid
            total_delay += inst.tasks[tid].delay()

    return total_delay


def validate_scheduling(inst, scheduling):
    taskset = set(itertools.chain.from_iterable(scheduling))
    if len(taskset) != sum(len(M) for M in scheduling):
        print("Non-unique tasks detected in scheduling.")
        return False

    if len(taskset) != inst.n:
        print("Invalid number of tasks scheduled.")
        return False

    if len(scheduling) != inst.m:
        print("Invalid number of rows (machines) in scheduling file.")
        return False

    return True


def validate(instance_path, solution_path):
    instance_file = open(instance_path, "r")
    inst = instance.Instance.from_file(instance_file)
    instance_file.close()
    value, scheduling = read_solution_file(solution_path)

    if not validate_scheduling(inst, scheduling):
        print("invalid scheduling solution")
        return False

    expected_value = compute_scheduling_value(inst, scheduling)
    if expected_value != value:
        print("invalid schaduling value")
        print(expected_value, value)
        return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", help="scheduling instance file")
    parser.add_argument("--solution", help="scheduling file")
    args = parser.parse_args()

    if validate(args.instance, args.solution):
        print("OK")
    else:
        print("NOT OK")
