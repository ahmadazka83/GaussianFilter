import numpy as np

def gaussian_filter(matrix):
    rows, cols = matrix.shape
    result = np.zeros_like(matrix, dtype=np.float64)

    # Kernel Gaussian 3x3
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    kernel_sum = np.sum(kernel)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            weighted_sum = (
                matrix[i - 1, j - 1] * kernel[0, 0] + matrix[i - 1, j] * kernel[0, 1] + matrix[i - 1, j + 1] * kernel[0, 2] +
                matrix[i, j - 1] * kernel[1, 0] + matrix[i, j] * kernel[1, 1] + matrix[i, j + 1] * kernel[1, 2] +
                matrix[i + 1, j - 1] * kernel[2, 0] + matrix[i + 1, j] * kernel[2, 1] + matrix[i + 1, j + 1] * kernel[2, 2]
            )

            result[i, j] = round(weighted_sum / kernel_sum)

    return result

# Initial matrix
matrix_10x10 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 90, 90, 5, 5, 5, 5, 5, 5, 0],
    [0, 90, 90, 5, 5, 5, 4, 5, 5, 0],
    [0, 5, 5, 5, 5, 4, 5, 5, 5, 0],
    [0, 5, 5, 90, 85, 90, 5, 5, 5, 0],
    [1, 5, 5, 90, 85, 90, 5, 4, 5, 0],
    [0, 5, 5, 5, 5, 5, 5, 5, 5, 0],
    [0, 5, 4, 5, 5, 5, 5, 90, 90, 0],
    [0, 5, 5, 5, 4, 5, 5, 90, 90, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Apply Gaussian filter
result_matrix_10x10 = gaussian_filter(matrix_10x10)

# Display the result
print(result_matrix_10x10)
