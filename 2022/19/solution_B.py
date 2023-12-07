#!/usr/bin/env python

import math
import re
import sys

allowed_time = 32
allowed_blueprints = 3
priority = {'geode': 0, 'obsidian': 1, 'clay': 2, 'ore': 3}
blueprint_regex = re.compile(r'Each (\w+) robot costs (\d+) ore(?: and (\d+) (\w+))?')


def read_blueprint(line):
    costs = []

    for sentence in line.split('.'):
        sentence = sentence.strip()
        if not sentence:
            continue

        match = blueprint_regex.search(sentence)
        cost = {'ore': int(match.group(2))}
        if match.group(3) is not None:
            cost[match.group(4)] = int(match.group(3))
        costs.append((match.group(1), cost))

    costs.sort(key=lambda item: priority[item[0]])
    return costs


def find_limits(costs):
    limits = {}

    for robot in [_[0] for _ in costs]:
        limits[robot] = max(_[1].get(robot, 0) for _ in costs)

    return limits


def find_best(costs, limits, time, resources, robots, global_best = 0, depth = 0):
    best = resources.get('geode', 0) + (allowed_time - time) * robots.get('geode', 0)
    prefix = ''.join(['  '] * depth)
    #print(f'{prefix}STATE: T={time}, R={resources}, R={robots} | {best}')

    for robot, cost in costs:
        if not set(cost.keys()) <= set(robots.keys()):
            #print(f'{prefix}- can\'t build {robot} robot')
            continue

        if robot != 'geode' and robots.get(robot, 0) >= limits[robot]:
            #print(f'{prefix}- no more {robot} robots are needed')
            continue

        required_time = max(
            math.ceil(max(0, amount - resources.get(resource, 0)) / robots[resource])
            for resource, amount in cost.items()
        )
        if time + required_time + 1 >= allowed_time:
            #print(f'{prefix}- can build {robot} robot in {required_time + 1} minutes, which is too long')
            continue

        new_resources = {**resources}
        for resource, amount in robots.items():
            if resource not in new_resources:
                new_resources[resource] = 0
            new_resources[resource] += amount * (required_time + 1)
        for resource, amount in cost.items():
            new_resources[resource] -= amount

        new_robots = {**robots}
        if robot not in new_robots:
            new_robots[robot] = 0
        new_robots[robot] += 1

        time_left = allowed_time - time - required_time - 1
        if new_resources.get('geode', 0) + new_robots.get('geode', 0) * time_left + (time_left - 1) * (time_left) / 2 <= max(best, global_best):
            #print(f'{prefix}- building {robot} robot can\'t improve the best known result')
            continue

        #print(f'{prefix}- building {robot} robot in {required_time + 1} minutes -> T={time + required_time + 1}, R={new_resources}, R={new_robots}')
        best = max(best, find_best(costs, limits, time + required_time + 1, new_resources, new_robots, best, depth + 1))
        if robot == 'geode' and required_time == 0:
            #print(f'{prefix}- geode robot built, skipping other options')
            break

    return best


def main():
    result = 1
    for index, line in enumerate(sys.stdin, 1):
        costs = read_blueprint(line)
        limits = find_limits(costs)
        best = find_best(costs, limits, 0, {}, {'ore': 1})
        result *= best
        #print(f'{index}: {best}')
        if index == allowed_blueprints:
            break
    print(result)


if __name__ == '__main__':
    main()
