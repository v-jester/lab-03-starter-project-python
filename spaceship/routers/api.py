from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('/greet')
def greeting() -> dict:
    return {'message': 'Hello, World!'}

@router.get('/matrix_product')
def compute_matrix_product() -> dict:

    matrix_x = np.random.randint(0, 10, (10, 10)).tolist()
    matrix_y = np.random.randint(0, 10, (10, 10)).tolist()

    array_x = np.array(matrix_x)
    array_y = np.array(matrix_y)

    result_array = np.dot(array_x, array_y)

    result_matrix = result_array.tolist()

    return {
        'matrix_x': matrix_x,
        'matrix_y': matrix_y,
        'result': result_matrix
    }
