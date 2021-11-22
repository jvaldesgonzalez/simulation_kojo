from consts import first_lambda, infinity, second_lambda
from utils import generate_exp, omg_time, generate_new_client


def simulation(with_three=False):
    close_t = 11 * 60 * 60

    store_is_open = True
    global_t = 0
    clients_n = 0

    worker_status = [False, False]  # False is bussy, True is free
    worker_spend_t = [infinity, infinity, infinity]
    worker_clients_n = [0, 0, 0]

    arrival_t_q = []

    waiting_t_q = []

    arrival_time = generate_exp(first_lambda)

    while store_is_open or any(worker_status):
        next_out_time = min(worker_spend_t)

        if arrival_time <= next_out_time and arrival_time < close_t:
            global_t = arrival_time
            clients_n += 1
            arrival_t_q.append(global_t)

            if not all(worker_status):
                i = worker_status.index(False)
                worker_status[i] = True
                worker_clients_n[i] += 1

                generate_new_client(
                    i, waiting_t_q, global_t, arrival_t_q, worker_spend_t)

            if omg_time(global_t):
                arrival_time = global_t + generate_exp(second_lambda)

                if with_three and len(worker_status) == 2:
                    worker_status.append(False)
            else:

                if len(worker_status) == 3 and not worker_status[2]:
                    worker_status.pop()

                arrival_time = global_t + generate_exp(first_lambda)

        elif (arrival_time > next_out_time) or (any(worker_status) and not store_is_open):
            i = worker_spend_t.index(next_out_time)
            global_t = next_out_time

            if len(arrival_t_q) > 0:
                generate_new_client(
                    i, waiting_t_q, global_t, arrival_t_q, worker_spend_t)
            else:
                worker_status[i] = False
                worker_spend_t[i] = infinity

        if global_t >= close_t or arrival_time >= close_t:
            store_is_open = False

    return waiting_t_q, clients_n
