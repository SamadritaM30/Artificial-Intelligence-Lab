import random

def generate_initial_state(m, mat):
    initial_state = list()
    for i in range(m):
        initial_state.append(round(random.uniform(mat[i][3], mat[i][4]), 2))
    return initial_state  

def check_constraints(state, m, mat, Pd):
    output = 0
    for i in range(m):
        if (state[i] < mat[i][3] or state[i] > mat[i][4]):
            return False
        output += state[i]
    
    if abs(output - 1.05 * Pd) > 1:
        return False
    return True

def fitness_function(state, m, mat, Pd):
    cost = 0
    for i in range(m):
        cost += (mat[i][0] + mat[i][1]*state[i] + mat[i][2] * pow(state[i], 2))
    
    if (check_constraints(state, m, mat, Pd) == False):
        return 10**6 + cost
    return cost

def Reproduce(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))  

    child = [-1] * (n)
    child[start:end] = parent1[start:end]
    child[:start] = parent2[:start]
    child[end:] = parent2[end:]
    return child


def Mutate(state, m, mat):
    i = random.randint(0, m-1)
    state[i] = round(random.uniform(mat[i][3], mat[i][4]),2)
    return state  

def Random_Selection(population, m, mat, Pd):
    fitness_values = [fitness_function(state, m, mat, Pd) for state in population]
    weights = [1 / (fitness + 1e-6) for fitness in fitness_values]  
    
    return random.choices(population, weights=weights, k=1)[0] 

def genetic_algorithm(population, m, mat, Pd):
    K = 2000  

    for _ in range(K):
        newPopulation = []  
        for _ in range(len(population)):  
            parent1 = Random_Selection(population, m, mat, Pd)  
            parent2 = Random_Selection(population, m, mat, Pd)  
            child = Reproduce(parent1, parent2)  

            if random.random() < 0.1:  
                child = Mutate(child, m, mat)  

            newPopulation.append(child)  

        population = newPopulation  

    best_idx = 0  
    for i in range(len(population)):  
        if fitness_function(population[i], m, mat, Pd) < fitness_function(population[best_idx], m, mat, Pd):  
            best_idx = i  

    return population[best_idx]  

def main():
    m = int(input("Enter the number of generators: "))  
    Pd = float(input("Enter the demand (in MW): "))  

    mat = []  
    for _ in range(m):  
        row = list(map(float, input().split()))  
        mat.append(row)

    population = [generate_initial_state(m, mat) for _ in range(20)]

    final_state_ga = genetic_algorithm(population, m, mat, Pd)  

    print(f"Generator Outputs: {final_state_ga}")  
    print(f"Total cost: {fitness_function(final_state_ga, m, mat, Pd)}")  

main()
