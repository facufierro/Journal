import random

# Sample post templates for each category
food_posts = [
    "I love eating {}.",
    "My favorite dish is {}.",
    "I cooked {} for dinner.",
    "I went to a restaurant that serves amazing {}.",
    "I tried cooking {} and it turned out great!"
]

sports_posts = [
    "I watched the {} game last night.",
    "I love playing {}.",
    "The {} team did really well.",
    "I got tickets for the {} match.",
    "I can't believe the {} game last night!"
]

technology_posts = [
    "I just bought a new {}.",
    "I'm learning how to code in {}.",
    "The new software update for {} is great.",
    "I can't wait for the new {} to release.",
    "I'm having trouble with my {}."
]

# Sample keywords for each category
food_keywords = ['pizza', 'pasta', 'sushi', 'steak', 'salad']
sports_keywords = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
technology_keywords = ['laptop', 'Python', 'Android', 'smartphone', 'Linux']


def generate_random_posts(n):
    all_posts = []
    all_labels = []

    for _ in range(n):
        category = random.choice(['food', 'sports', 'technology'])

        if category == 'food':
            template = random.choice(food_posts)
            keyword = random.choice(food_keywords)
            all_labels.append('food')

        elif category == 'sports':
            template = random.choice(sports_posts)
            keyword = random.choice(sports_keywords)
            all_labels.append('sports')

        else:
            template = random.choice(technology_posts)
            keyword = random.choice(technology_keywords)
            all_labels.append('technology')

        post = template.format(keyword)
        all_posts.append(post)

    return all_posts, all_labels


# Generate 20 random posts
random_posts, random_labels = generate_random_posts(20)

# Display generated data
for i, (post, label) in enumerate(zip(random_posts, random_labels)):
    print(f"Post {i + 1} (Category: {label}) - {post}")
