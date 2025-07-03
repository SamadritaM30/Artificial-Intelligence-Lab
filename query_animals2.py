# Import the Prolog class from the pyswip library
from pyswip import Prolog
# --- 1. Initialize Prolog Interface ---
prolog = Prolog ()
# --- 2. Load Knowledge Base using consult ---
print (" Consulting animals .pl ...")
prolog . consult ("animals.pl") # Assumes animals .pl is in the same directory
print (" Knowledge Base Consulted .")
# --- 3. Perform Queries ---
# ( Query code remains the same as in Listing 2)

# ... rest of the query code ...

# --- 3. Perform Queries ---
print("\n--- Querying ---")

# Example 1: Check a specific known fact (boolean result)
query_result_direct = list(prolog.query("bigger(elephant, horse)"))
#print(f"Is 'bigger(elephant, horse)' true? {'Yes' if query_result_direct else 'No'}")
print("Is 'bigger(elephant, horse)' true?" )
if(query_result_direct):
    print("Yes")
else :
    print("No")

# Example 2: Check an inferred fact using 'is_bigger'
query_result_inferred = list(prolog.query("is_bigger(elephant, dog)"))
print(f"Is 'is_bigger(elephant, dog)' true? {'Yes' if query_result_inferred else 'No'}")

# Example 3: Find all animals smaller than a donkey using 'is_bigger'
print("\nAnimals smaller than a donkey (using is_bigger):")
smaller_than_donkey = []
query_gen_donkey = prolog.query("is_bigger(donkey, Animal)")
for solution in query_gen_donkey:
    # Each solution is a dictionary: {'Animal': value}
    smaller_than_donkey.append(solution['Animal'])
# Print unique results
print(sorted(list(set(smaller_than_donkey))))

# Example 4: Find all 'is_bigger' pairs
print("\nAll (X, Y) pairs where X is_bigger than Y:")
all_pairs = []
query_gen_all = prolog.query("is_bigger(X, Y)")
for soln in query_gen_all:
    X, Y = soln['X'], soln['Y']
    all_pairs.append(X + ' > ' + Y)

# Print unique pairs, sorted
print(sorted(list(set(all_pairs))))

print("\n--- Queries Complete ---")
