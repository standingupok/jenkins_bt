from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/get_version")
def get_version():
    """
    Trả về phiên bản hiện tại của ứng dụng.
    """
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.
    """
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}
