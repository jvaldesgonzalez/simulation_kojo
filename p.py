from consts import first_lambda, infinity, second_lambda, close_t
from utils import generate_exp, omg_time, generate_new_client
import numpy as np


def can_keep_working(store_status, workers):
    return store_status or any(workers)


def is_time_to_close(global_t, arrival_t):
    return global_t >= close_t or arrival_t >= close_t


def simulation(with_three=False):
    store_is_open = True
    global_t = 0
    clients_n = 0
    attendant_status = [False, False]  # False is bussy, True is free
    attendant_spend_t = [infinity, infinity, infinity]
    arrival_t_q = []
    waiting_t_q = []
    arrival_t = generate_exp(first_lambda)

    while True:
        if not can_keep_working(store_is_open, attendant_status):
            break

        client_who_finish_t = np.min(attendant_spend_t)

        if arrival_t > client_who_finish_t or arrival_t >= close_t:
            if (arrival_t > client_who_finish_t) or (any(attendant_status) and not store_is_open):
                i = attendant_spend_t.index(client_who_finish_t)
                global_t = client_who_finish_t

                if len(arrival_t_q) > 0:
                    generate_new_client(
                        i, waiting_t_q, global_t, arrival_t_q, attendant_spend_t)
                else:
                    attendant_spend_t[i] = infinity
                    attendant_status[i] = False

        else:
            global_t = arrival_t
            arrival_t_q.append(global_t)
            clients_n += 1

            if not all(attendant_status):
                i = attendant_status.index(False)
                attendant_status[i] = True

                generate_new_client(
                    i, waiting_t_q, global_t, arrival_t_q, attendant_spend_t)

            if omg_time(global_t):
                arrival_t = global_t + generate_exp(second_lambda)

                if with_three and len(attendant_status) == 2:
                    attendant_status.append(False)
            else:
                arrival_t = global_t + generate_exp(first_lambda)

        if is_time_to_close(global_t, arrival_t):
            store_is_open = False

    return (waiting_t_q, clients_n)
