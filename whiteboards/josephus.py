import itertools


def remainder(lst, k):
    return len(lst) % k


def culling(lst, k):
    for i, x in enumerate(lst):
        num = i + 1
        if num % k == 0:
            print(f'Death of {x}')
        else:
            yield x


def step_through_list(lst, k):
    values = list(culling(lst, k))
    r = remainder(lst, k)
    end = values[-r:]
    return end + values[:-r]


def josephus(lst, k):
    while len(lst) > 1:
        print(f'The people to be judged are: {lst}')
        if len(lst) >= k:
            lst = step_through_list(lst, k)

        else:
            r = remainder(lst, k)
            lst = lst[:r] + lst[r:]

    return lst

person = josephus(list(range(1, 6)), 2)
print(person)