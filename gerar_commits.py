import matplotlib.pyplot as plt
import numpy as np

# Define the ranks and their corresponding percentiles
ranks = ['S', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
percentiles = [1, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100]

# Calculate the global percentile (example value)
global_percentile = 30  # This value should be calculated based on the given statistics

# Calculate the rank based on the global percentile
rank_index = next(i for i, p in enumerate(percentiles) if global_percentile <= p)
rank = ranks[rank_index]

# Create a pie chart to show the rank
fig, ax = plt.subplots(figsize=(10, 5))
size = 0.3

# Create a circle at the center to represent the global percentile
circle = plt.Circle((0, 0), size, color='white')

# Create the pie chart
wedges, texts = ax.pie([global_percentile, 100 - global_percentile], radius=1, colors=['blue', 'lightgray'], startangle=90)

# Add the circle at the center
plt.gca().add_artist(circle)

# Add text to show the rank
plt.text(0, 0, rank, ha='center', va='center', fontsize=24)

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Set title
plt.title('GitHub Usage Statistics Rank')

# Add information to the left side of the image
info_text = (
    "Total Stars Earned: \n"
    "Total Commits (2024): \n"
    "Total PRs: \n"
    "Total Issues: \n"
    "Contributions in (Last year): "
)

plt.text(-2.5, 0.5, info_text, ha='right', va='center', fontsize=12)

# Save the chart as an image file
plt.savefig('usage_statistics_rank_with_info_left.png')

# Show the chart
plt.show()

print("Usage statistics rank image with information generated: usage_statistics_rank_with_info_left.png")

