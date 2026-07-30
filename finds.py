import csv

# Read dataset
data = []

with open("enjoysport.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        data.append(row)

print("Training Data:\n")

for row in data:
    print(row)

print("\nTotal number of training instances :", len(data))

# Number of attributes (excluding target class)
num_attributes = len(data[0]) - 1

# Initialize hypothesis
hypothesis = ['0'] * num_attributes

print("\nInitial Hypothesis:")
print(hypothesis)

# Find-S Algorithm
for i in range(len(data)):

    if data[i][num_attributes].lower() == "yes":

        for j in range(num_attributes):

            if hypothesis[j] == '0':
                hypothesis[j] = data[i][j]

            elif hypothesis[j] != data[i][j]:
                hypothesis[j] = '?'

    print("\nHypothesis after Training Instance", i + 1)
    print(hypothesis)

print("\nFinal Maximally Specific Hypothesis:")
print(hypothesis)