import numpy as np
from fastapi import APIRouter

router = APIRouter()

@router.get("/matrix-sum")
def matrix_sum() -> dict:
    mat1 = np.random.randint(1, 10, size=(10, 10))
    mat2 = np.random.randint(1, 10, size=(10, 10))

    result = np.add(mat1, mat2)
    return {
        "first_matrix": mat1.tolist(),
        "second_matrix": mat2.tolist(),
        "sum_result": result.tolist(),
    }
