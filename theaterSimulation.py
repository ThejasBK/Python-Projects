import simpy
import random
import statistics
wait_times = []
class Theater(object):
    def __init__(self,env,num_cashiers,num_servers,num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.usher = simpy.Resource(env, num_ushers)
        self.server = simpy.Resource(env, num_servers)
        
    def purchase_ticket(self,moviegoer):
        yield self.env.timeout(random.randint(1,3))
        
    def check_tickets(self,moviegoer):
        yield self.env.timeout(3/60)
    
    def sell_food(self,moviegoer):
        yield self.env.timeout(random.randint(1,5))

def go_to_movies(env, moviegoer, theater):
    arrival_time = env.now
    
    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(moviegoer))
        
    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))
        
    if random.choice([True,False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))
    
    wait_times.append(env.now - arrival_time)

def run_simulation(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)
    
    for moviegoer in range(5):
        env.process(go_to_movies(env, moviegoer, theater))
    
    while True:
        env.timeout(0.2)
        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))

def get_avg_wait_time(wait_times):
    avg_wait_time = statistics.mean(wait_times)

def user_input():
    num_cashiers = input('Cashiers: ')
    num_servers = input('Servers: ')
    num_ushers = input('Ushers: ')
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):
        params = [int(x) for x in params]
    else:
        print('Wrong input! Considering everything as 1')
        params = [1, 1, 1]
    return params

def main():
    random.seed(42)
    num_cashiers, num_servers, num_ushers = user_input()
    env = simpy.Environment()
    env.process(run_simulation(env, num_cashiers, num_servers, num_ushers))
    env.run(until = 10)
    mins, secs = get_avg_wait_time(wait_times)
    print(mins, secs)

if __name__ == '__main__':
    main()
