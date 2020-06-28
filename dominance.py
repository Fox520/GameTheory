import copy

p1_strats = [[5, 4], [3, 3], [2, 4], [4, 5]]

p2_strats = [[2, 1, 1, 3], [2, 2, 1, 4]]


def is_a_strictly_dominant(a, b):
    for i in range(len(a)):
        if a[i] < b[i] or a[i] in b:
            return False
    return True


def is_a_weakly_dominant(a, b):
    counts = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            counts += 1
    if counts == len(a):
        # Totally dominates
        return False
    if counts > 0:
        # Weakly dominates
        return True


def is_a_fully_dominated(a, b):
    counts = 0
    for i in range(len(a)):
        if b[i] > a[i]:
            counts += 1
    if counts == len(a):
        # Totally dominated
        return True
    return False


# For each player
# 1. Find the strictly dominant strategy
def strongly_dominate_strategy(strategies):
    strong_index = -1
    for i in range(len(strategies)):
        row = strategies[i]
        # Compare with other strategies excluding self
        temp_strategies = copy.deepcopy(strategies)
        temp_strategies.pop(i)
        for j in range(len(temp_strategies)):
            temp_row = temp_strategies[j]
            # Check if we are still dominant
            if is_a_strictly_dominant(row, temp_row):
                if strong_index == -1:
                    strong_index = i
                elif is_a_strictly_dominant(row, strategies[strong_index]):
                    strong_index = i
                else:
                    strong_index = -1

    return strong_index


# 2. Find the weakly dominant strategy
def weakly_dominate_strategy(strategies):
    weak_index = -1
    for i in range(len(strategies)):
        row = strategies[i]
        # Compare with other strategies excluding self
        temp_strategies = copy.deepcopy(strategies)
        temp_strategies.pop(i)
        for j in range(len(temp_strategies)):
            temp_row = temp_strategies[j]
            # Check if we are still dominant
            if is_a_weakly_dominant(row, temp_row):
                if weak_index == -1:
                    weak_index = i
                elif is_a_strictly_dominant(row, strategies[weak_index]):
                    weak_index = i
                else:
                    weak_index = -1

    return weak_index


# 3. Find the dominated strategy
def get_dominated_strategies(strategies):
    dominated_strategies = []
    for i in range(len(strategies)):
        row = strategies[i]
        # Compare with other strategies excluding self
        temp_strategies = copy.deepcopy(strategies)
        temp_strategies.pop(i)
        for j in range(len(temp_strategies)):
            temp_row = temp_strategies[j]
            # Check if row is dominated
            if is_a_fully_dominated(row, temp_row):
                dominated_strategies.append(i)
                break

    return dominated_strategies


wp1_strats = [[8, 6], [3, 3], [2, 4], [1, 5]]

# print(strongly_dominate_strategy(wp1_strats))
# print(weakly_dominate_strategy(p2_strats))
print(get_dominated_strategies(p1_strats))
