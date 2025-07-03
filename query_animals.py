# Import the Prolog class from the pyswip library
from pyswip import Prolog

# --- 1. Initialize Prolog Interface ---
prolog = Prolog()

# --- 2. Load Knowledge Base using assertz ---
# Add facts one by one
print("Loading knowledge base ...")
prolog.assertz("bigger(elephant, horse)")
prolog.assertz("bigger(horse, donkey)")
prolog.assertz("bigger(donkey, dog)")
prolog.assertz("bigger(donkey, monkey)")

# Add rules one by one
prolog.assertz("is_bigger(X, Y) :- bigger(X, Y)")
prolog.assertz("is_bigger(X, Y) :- bigger(X, Z), is_bigger(Z, Y)")
print("Knowledge Base Loaded.")

# --- 3. Perform Queries ---
print("\n--- Querying ---")

# Example 1: Check a specific known fact (boolean result)
query_result_direct = list(prolog.query("bigger(elephant, horse)"))
print(f"Is 'bigger(elephant, horse)' true? {'Yes' if query_result_direct else 'No'}")

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
    all_pairs.append(f"{soln['X']} > {soln['Y']}")
# Print unique pairs, sorted
print(sorted(list(set(all_pairs))))

print("\n--- Queries Complete ---")
