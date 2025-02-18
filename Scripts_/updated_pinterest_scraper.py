import random

# Function to generate a large random 2D array
def generate_random_posts(rows, max_cols):
    posts = []

    for row in range(rows):
        cols = random.randint(1, max_cols)  # Random number of columns per row
        row_posts = []

        for col in range(cols):
            row_posts.append(f"Post ({row},{col})")

        posts.append(row_posts)

    return posts

random_posts = generate_random_posts(rows=100, max_cols=50)

# Example output
for row in random_posts[:5]:  # Displaying only the first 5 rows for readability
    print(row)