import random
import math

# Function to calculate the total conflict score for a seating arrangement
def calculate_conflict_score(arrangement, conflict_matrix):
    score = 0
    n = len(arrangement)
    for i in range(n):
        # Add the conflict score between adjacent guests (circular arrangement)
        score += conflict_matrix[arrangement[i]][arrangement[(i + 1) % n]]
    return score

# Simulated Annealing Algorithm
def simulated_annealing(conflict_matrix, initial_arrangement, initial_temp, cooling_rate, max_iter):
    current_arrangement = initial_arrangement[:]
    current_score = calculate_conflict_score(current_arrangement, conflict_matrix)
    
    # Store the best arrangement and its score
    best_arrangement = current_arrangement[:]
    best_score = current_score
    
    # Set the initial temperature
    temperature = initial_temp

    for iteration in range(max_iter):
        # Generate a neighbor by swapping two random indices
        new_arrangement = current_arrangement[:]
        i, j = random.sample(range(len(new_arrangement)), 2)
        new_arrangement[i], new_arrangement[j] = new_arrangement[j], new_arrangement[i]
        
        # Calculate the conflict score for the new arrangement
        new_score = calculate_conflict_score(new_arrangement, conflict_matrix)
        
        # Decide whether to accept the new arrangement
        if new_score < current_score:
            # Always accept if the score is better
            current_arrangement = new_arrangement
            current_score = new_score
        else:
            # Accept worse arrangements with a probability based on temperature
            delta_score = new_score - current_score
            probability = math.exp(-delta_score / temperature)
            if random.random() < probability:
                current_arrangement = new_arrangement
                current_score = new_score
        
        # Update the best arrangement if found
        if current_score < best_score:
            best_arrangement = current_arrangement[:]
            best_score = current_score
        
        # Decrease the temperature
        temperature *= cooling_rate
        
        # Print progress every 100 iterations (optional for debugging)
        if (iteration + 1) % 100 == 0:
            print(f"Iteration {iteration + 1}: Current Score = {current_score}, Best Score = {best_score}")
    
    return best_arrangement, best_score


if __name__ == "__main__":
    
    conflict_matrix = [
        [0, 3, 8, 2],  
        [3, 0, 6, 4],  
        [8, 6, 0, 5],  
        [2, 4, 5, 0]   
    ]
    
    
    initial_arrangement = [0, 3, 8, 2]  
   
    initial_temp = 100        
    cooling_rate = 0.95      
    max_iter = 1000           
  
    initial_score = calculate_conflict_score(initial_arrangement, conflict_matrix)
    
    
    
    print("Initial Seating Arrangement:", initial_arrangement)
    print("Initial Conflict Score:", initial_score)
    
    
    print("\nRunning Simulated Annealing...")
    best_arrangement, best_score = simulated_annealing(conflict_matrix, initial_arrangement, initial_temp, cooling_rate, max_iter)
    
    
    print("\nOptimal Seating Arrangement:", best_arrangement)
    print("Minimum Conflict Score:", best_score)
