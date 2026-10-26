import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.random.seed(42)

# Example: Predicting daily activities (represented as numbers)
# 0=Sleep, 1=Work, 2=Exercise, 3=Social, 4=Leisure
historical_activities = [0, 1, 2, 1, 3, 1, 4, 0, 1, 2, 1, 3, 1, 4, 0]

def calculate_probabilities(sequence):

    counts = Counter(sequence)
    total = len(sequence)
    probabilities = {activity: count/total for activity, count in counts.items()}
    return probabilities




def calculate_conditional_probabilities(sequence):
   
    transitions = {}

    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_activity = sequence[i + 1]

        if current not in transitions:
            transitions[current] = []
        transitions[current].append(next_activity)

    # Convert to probabilities
    conditional_probs = {}
    for current, next_list in transitions.items():
        counts = Counter(next_list)
        total = len(next_list)
        conditional_probs[current] = {activity: count/total for activity, count in counts.items()}

    return conditional_probs



def predict_next_activity(current_activity, conditional_probs):

    if current_activity not in conditional_probs:
        return None

    next_probs = conditional_probs[current_activity]
    max_prob = max(next_probs.values())
    most_likely_next = [activity for activity, prob in next_probs.items() if prob == max_prob][0]

    return most_likely_next



# Calculate  probabilities
probs = calculate_probabilities(historical_activities)

# Display results
activity_names = {0: 'Sleep', 1: 'Work', 2: 'Exercise', 3: 'Social', 4: 'Leisure'}
print("Activity Probabilities:")
for activity, prob in sorted(probs.items()):
    print(f"  {activity_names[activity]}: {prob:.2%}")

# Calculate conditional probabilities
cond_probs = calculate_conditional_probabilities(historical_activities)

# Display
print("Conditional Probabilities: P(Next | Current)\n")
for current, next_probs in cond_probs.items():
    print(f"After {activity_names[current]}:")
    for next_activity, prob in sorted(next_probs.items()):
        print(f"  → {activity_names[next_activity]}: {prob:.2%}")
    print()


#  Predict the next activity after "Work"
current = 1  # Work
predicted = predict_next_activity(current, cond_probs)
print("\n NEXT ACTIVITY PREDICTION \n")
print(f"After {activity_names[current]}, most likely next: {activity_names.get(predicted, 'Unknown')}")

