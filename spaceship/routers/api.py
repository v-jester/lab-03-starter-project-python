import numpy as np
from fastapi import APIRouter

router = APIRouter()



def hello_world() -> dict:
    return {'msg': 'Hello, World!'}
@router.get("/matrix-multiply")
def matrix_multiplication() -> dict:
    mat1 = np.random.rand(10, 10)
    mat2 = np.random.rand(10, 10)

    result = np.dot(mat1, mat2)
    return {
        "first_matrix": mat1.tolist(),
        "second_matrix": mat2.tolist(),
        "multiplication_result": result.tolist(),
    }

