from p import simulation

clients_wait_time, n = simulation(with_three=True)
total_wait = sum(clients_wait_time)
left5_sum = 0
for i in clients_wait_time:
    if (i >= 5*60):
        left5_sum += i
print("con 3", total_wait, n, (left5_sum/total_wait)*100)

clients_wait_time, n = simulation(with_three=False)
total_wait = sum(clients_wait_time)
left5_sum = 0
for i in clients_wait_time:
    if (i >= 5*60):
        left5_sum += i
print("con 2", total_wait, n, (left5_sum/total_wait)*100)
