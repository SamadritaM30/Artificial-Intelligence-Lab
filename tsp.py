import random
import numpy as np

def generate_initial_state(n):
    initial_state = list(range(1, n))  
    random.shuffle(initial_state)  
    initial_state.append(0)  
    initial_state.insert(0, 0)  
    return initial_state  

def fitness_function(state, cost, n):
    state_cost = 0
    for i in range(n):
        state_cost += cost[state[i]][state[i + 1]]  
    return state_cost  

def Reproduce(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(1, n-1), 2))  

    child = [-1] * (n)  
    child[0] = 0
    child[n-1] = 0
    child[start:end] = parent1[start:end]

    pos = end  
    for gene in parent2:
        if gene not in child:
            while child[pos] != -1:  
                pos = (pos + 1) % n  
            child[pos] = gene  

    return child


def Mutate(state, n):
    x = random.randint(1, n-1)
    y = random.randint(1, n-1)
    state[x], state[y] = state[y], state[x]  
    return state  

def Random_Selection(population, cost, n):
    fitness_values = [fitness_function(ind, cost, n) for ind in population]
    weights = [1 / (fitness + 1e-6) for fitness in fitness_values]  
    
    return random.choices(population, weights=weights, k=1)[0] 

def genetic_algorithm(population, cost, n):
    K = 1000  

    for _ in range(K):
        newPopulation = []  
        for _ in range(len(population)):  
            parent1 = Random_Selection(population, cost, n)  
            parent2 = Random_Selection(population, cost, n)  
            child = Reproduce(parent1, parent2)  

            if random.random() < 0.1:  
                child = Mutate(child, n)  

            newPopulation.append(child)  

        population = newPopulation  

    best_idx = 0  
    for i in range(len(population)):  
        if fitness_function(population[i], cost, n) < fitness_function(population[best_idx], cost, n):  
            best_idx = i  

    return population[best_idx]  

def main():
    n = int(input("Enter the number of cities: "))  

    cost = []  
    for _ in range(n):  
        row = list(map(int, input().split()))  
        cost.append(row)  

    population = [generate_initial_state(n) for _ in range(10)]  
    # print(population)

    final_state_ga = genetic_algorithm(population, cost, n)  

    print(f"Final State by Genetic Algorithm: {final_state_ga}")  
    print(f"Distance: {fitness_function(final_state_ga, cost, n)}")  

main()
