#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def random_order(n):
    """ Generate random permutation of integers <0..n>.
        Uses sort with random key value method.
    """
    keys = [random.randint(0, n - 1) for _ in range(n)]
    ids = list(range(n))
    ids.sort(key=lambda x: keys[x])
    return ids


def randomized_solution(m, n):
    """ Generate random solution candidate by assigning
        random tasks to random processors.
    """
    return [
        (random.randint(0, m - 1), task_id)
        for task_id in random_order(n)
    ]


def fitness(scheduling, tasks, m):
    """ Compute total delay for given scheduling candidate.
    """
    timers = [0] * m
    total_delay = 0
    for pid, tid in scheduling:
        print(timers)
        timers[pid] += max(timers[pid], tasks[tid].r) + tasks[tid].p
        total_delay += max(0, timers[pid] - tasks[tid].d)
    print("---")
    return total_delay


def apply_scheduling(tasks, scheduling):
    """ Fill tasks scheduling params according to the given scheduling.
    """
    clock = [0, 0, 0, 0]
    for pid, tid in scheduling:
        tasks[tid].pid = pid
        tasks[tid].start = clock[pid]
        clock[pid] += tasks[tid].p
    return tasks


def select_pair(n):
    """ Select pair with linear preference for lower indexes.
    """
    x = int(random.triangular(0, n-1, 0))
    y = int(random.triangular(0, n-1, 0))
    return x, y


def cross(a, b):
    """ Cross by selecting each gene at equal probability from either parent.
    """
    mask = [random.choice("ab") for _ in a]
    child = []
    for x, y in zip(a, b):
        if mask[x[1]] == "b": child.append(x)
        if mask[y[1]] == "a": child.append(y)
    return child


def create_child(sorted_population):
    """ Create child of two random individuals from the population.
        Take social position into account when choosing pairs for crossover.
        -------------------------------------------------------------------
        selection probability linearly decreasing with social position
    """
    a, b = select_pair(len(sorted_population))
    return cross(sorted_population[a], sorted_population[b])


def mutate(individual, m):
    """ Perform random mutation on the individual.
        ------------------------------------------
        How should a mutation look like?
            -- random alternation of PID value
            -- random swap of two genes
    """
    for _ in range(m):

        if random.random() > 0.5:
            # alternate PID
            gid = random.randint(0, len(individual)-1)
            _, tid = individual[gid]
            individual[gid] = random.randint(0, 3), tid

        else:
            # swap two genes
            ida = random.randint(0, len(individual)-1)
            idb = random.randint(0, len(individual)-1)
            individual[ida], individual[idb] = individual[idb], individual[ida]

    return individual


def schedule(x):
    """ Solving an instance of the scheduling problem.
    """
    SIZE = 30
    ITERATIONS = 200
    KEEP_BEST = 5
    MUTATIONS = 0

    # initialize population
    population = [randomized_solution(x.m, x.n) for i in range(SIZE)]
    scores = [fitness(p, x.tasks, x.m) for p in population]

    for iteration in range(ITERATIONS):
        # who goes to new population?
        new_population = []

        # promote top candidates to the next generation
        population = [
            x for x, y in sorted(
                zip(population, scores),
                key=lambda p: p[1]
            )
        ]
        new_population.extend(population[:KEEP_BEST])

        # generate children
        new_population.extend([
            create_child(population)
            for _ in range(x.n - KEEP_BEST)
        ])

        # introduce mutations
        for _ in range(MUTATIONS):
            idx = random.randint(0, len(new_population)-1)
            new_population[idx] = mutate(new_population[idx], x.m)

        # kill old population
        population = new_population

        # evaluate new population
        scores = [fitness(p, x.tasks, x.m) for p in population]
        print(f"{iteration} best has score {max(scores)}")

    best = population[scores.index(max(scores))]
    return apply_scheduling(x.tasks, best)


def _schedule(x):
    """ Test function.
    """
    a = randomized_solution(x.m, x.n)
    b = randomized_solution(x.m, x.n)
    score_a = fitness(a, x.tasks, x.m)
    score_b = fitness(b, x.tasks, x.m)
    print(f"A SCORE: {score_a}")
    print(f"B SCORE: {score_b}")

    child = cross(a, b)
    score_child = fitness(child, x.tasks, x.m)
   
    print(f"CHILD SCORE: {score_child}")
    return apply_scheduling(x.tasks, child)



