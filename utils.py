import numpy as np
from consts import sandwish_sushi_dist


def generate_exp(l: float) -> float:
    return -(1/l)*np.log(1-np.random.random())


def generate_uniform(lo: int, hi: int) -> float:
    return lo+(hi-lo)*np.random.random()


# !!!! hora pico senyores 😂
def omg_time(t: float) -> bool:
    first_interval = (90*60, 90*60 + 150*60)
    second_interval = (7*60*60, 7*60*60 + 120*60)
    return (t > first_interval[0] and t < first_interval[1]) or (t > second_interval[0] and t < second_interval[1])


def generate_new_client(i, waiting_t_q, global_t, arrival_t_q, worker_spend_t):
    waiting_t_q.append(global_t - arrival_t_q.pop(0))
    is_sandwish = False if generate_uniform(
        0, 1) < sandwish_sushi_dist else True
    if not is_sandwish:
        worker_spend_t[i] = global_t + generate_uniform(5, 8) * 60
    else:
        worker_spend_t[i] = global_t + generate_uniform(3, 5) * 60
