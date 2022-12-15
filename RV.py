import os

# Set the directory containing the program files
program_dir = 'C:\\Users\\USER\\Documents\\FileRead'

# Get a list of all files in the directory
files = os.listdir(program_dir)

# Create an empty list to store the text files
text_files = []

# Loop through the files in the directory
for file in files:
  # Check if the file is a text file
  if file.endswith(".txt"):
    # If it is a text file, add it to the list
    text_files.append(file)

# Sort the list of text files in descending order by size
text_files.sort(key=lambda f: os.path.getsize(os.path.join(program_dir, f)), reverse=True)

file_1 = str(os.path.join(program_dir, text_files[0]))
file_2 = str(os.path.join(program_dir, text_files[1]))

  # read the two input files
with open(file_2) as f:
    common_words = [line.strip() for line in f]

with open(file_1) as f:
    file_1 = f.read()

# count the number of times each common word appears in the body text
counts = {}
for word in common_words:
    counts[word] = file_1.count(word)

# sort the words by their counts in descending order
sorted_words = sorted(counts, key=lambda x: counts[x], reverse=True)

# get the number of words to output from the user
n = int(input('How many words do you want to output? '))

# output the most commonly used words
for word in sorted_words[:n]:
    print(f'{word}: {counts[word]}')
