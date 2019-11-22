#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def random_order(n):
    keys = [random.randin(n) for i in range(n)]
    ids = list(range(n))
    ids.sort(key=lambda x: keys[x])
    return ids


def randomized_solution(m, n):
    return [
        (
            random.randint(m),  # random PID
            task_id             # TID in randomized order
        )
        for task_id in random_order(n)
    ]


def fitness(scheduling, tasks, m):
    """ Compute total delay for given scheduling candidate.
    """
    timers = [0] * m
    total_delay = 0
    for pid, tid in scheduling:
        timers[pid] = max(timers[pid], tasks[tid].r + tasks[tid].p)
        total_delay += max(0, timers[pid] - tasks[tid].d)
    return total_delay


def apply_scheduling(tasks, scheduling):
    """ Fill tasks scheduling params according to the given scheduling.
    """
    raise NotImplemented()


def create_child(sorted_population):
    """ Create child of two random individuals from the population.
        Take social position into account when choosing pairs for crossover.
        -------------------------------------------------------------------
        What probabilities for selection should each individual have depending on
        its social position?
    """
    raise NotImplemented()


def mutate(individual, m):
    """ Perform random mutation on the individual.
        ------------------------------------------
        How should a mutation look like?
            -- random swap of genes,
            -- random alternation of the gene value
    """
    raise NotImplemented()
    

def schedule(x):
    """ Solving an instance of the scheduling problem.
    """
    SIZE = 30
    ITERATIONS = 200
    KEEP_BEST = 5
    MUTATIONS = 2

    # initialize population
    population = [randomized_solution(x.m, x.n] for i in range(SIZE)]
    scores = [fitness(p, x.tasks, x.m) for p in population]    

    for i in range(ITERATIONS):
        # who goes to new population?
        new_population = []

        # promote top candidates to the next generation
        population.sort(key=lambda x: scores[x])
        new_population.extend(population[:KEEP_BEST])

        # generate children
        new_population.extend([
            create_child(population)
            for i in range(x.n - KEEP_BEST)
        ])

        # introduce mutations
        for i in range(MUTATIONS):
            idx = random.randint(0, len(new_population))
            new_population[idx] = mutate(new_population[idx])

        # kill old population
        population = new_population

        # evaluate new population
        scores = [fitness(p, x.tasks, x.m) for p in population]
        
    best = population[scores.index(max(scores))]
    return apply_scheduling(x.tasks, best)

