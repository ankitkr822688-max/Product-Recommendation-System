
# Product Recommendation System
# Using Jaccard Similarity

# Step 1: Store customer purchase data

customers = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


# Step 2: Function to calculate Jaccard Similarity

def jaccard_similarity(products1, products2):

    set1 = set(products1)
    set2 = set(products2)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    if union == 0:
        return 0

    return intersection / union


# Step 3: Find the most popular product

def popular_product():

    product_count = {}

    for products in customers.values():
        for product in products:
            product_count[product] = product_count.get(product, 0) + 1

    max_count = max(product_count.values())

    popular = [
        product for product, count in product_count.items()
        if count == max_count
    ]

    print("Popular product:", ", ".join(popular),
          f"(bought by {max_count} customers)")


# Step 4: Recommend products to a customer

def recommend_product(name):

    # Check empty input
    if not name.strip():
        print("Name cannot be empty.")
        return

    # Check whether customer exists
    if name not in customers:
        print(f"Customer '{name}' not found.")
        return

    similarity_scores = {}

    # Calculate similarity with other customers
    for customer, products in customers.items():

        if customer != name:
            similarity = jaccard_similarity(
                customers[name], products
            )

            similarity_scores[customer] = similarity

    # Display similarity scores
    print("\nSimilarity scores:")

    for customer, score in sorted(
        similarity_scores.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{customer}: {score:.2f}")

    # Find the most similar customer
    max_similarity = max(similarity_scores.values())

    if max_similarity == 0:
        print("No similar customers found.")
        popular_product()
        return

    most_similar = max(
        similarity_scores,
        key=similarity_scores.get
    )

    print("Most similar customer:", most_similar)

    # Recommend products not already purchased
    current_products = set(customers[name])
    similar_products = set(customers[most_similar])

    recommendations = similar_products - current_products

    if recommendations:
        print("Recommended:", ", ".join(sorted(recommendations)))
    else:
        print("No new products to recommend.")


# Step 5: Main program

print("===== PRODUCT RECOMMENDATION SYSTEM =====")

customer_name = input("Recommend for: ").strip().title()

recommend_product(customer_name)
