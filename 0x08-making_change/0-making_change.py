#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """ returns fewest number of coins needed to meet total """

    if total <= 0:
        return 0
    else:
        from math import trunc

        coins = sorted(coins, reverse=True)
        cn_dict = {}
        while total is not None:
            for cn in coins:
                if total % cn == 0:
                    cn_dict[cn] = total / cn
                    return(int(sum(cn_dict.values())))
                else:
                    cn_dict[cn] = trunc(total / float(cn))
                    total -= (cn * cn_dict[cn])
            return -1
