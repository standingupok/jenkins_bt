from fastapi import FastAPI

app = FastAPI()

@app.get("/get_version")
def get_version():
    """
    Endpoint để lấy version của API.
    """
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int):
    """
    Endpoint để kiểm tra số nguyên tố.
    """
    if number <= 1:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}
