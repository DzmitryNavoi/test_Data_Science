import math

def cos_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Error: Vectors must have the same length for calculating cosine distance.")
        return

    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude_vector1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude_vector2 = math.sqrt(sum(y ** 2 for y in vector2))

    
    if magnitude_vector1 == 0 or magnitude_vector2 == 0:
        print("Error: One or both vectors have zero magnitude, making it impossible to calculate the cosine distance.")
        return

    cosine_distance = dot_product / (magnitude_vector1 * magnitude_vector2)

    return cosine_distance


vector1 = [-0.5, 2, 3, 4]
vector2 = [0, 0, 1, -100]
result = cos_distance(vector1, vector2)

if result is not None:
    print("Cosine Distance between vector1 and vector2:", result)