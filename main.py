from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Replace these with your details
FULL_NAME = "john_doe"
DOB = "17091999"   # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class InputData(BaseModel):
    data: List[str]

# Health check (so browser GET works on root "/")
@app.get("/")
async def root():
    return {"message": "API is live! Use GET/POST on /bfhl"}

# /bfhl supports both GET and POST now
@app.get("/bfhl")
async def get_bfhl():
    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER
    }

@app.post("/bfhl")
async def post_bfhl(input_data: InputData):
    try:
        data = input_data.data
        odd_numbers, even_numbers, alphabets, special_characters = [], [], [], []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        # reverse + alternating caps
        concat_str = "".join(alphabets).lower()[::-1]
        alt_caps = "".join(
            ch.upper() if i % 2 == 0 else ch.lower()
            for i, ch in enumerate(concat_str)
        )

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": alt_caps
        }

    except Exception as e:
        return {"is_success": False, "error": str(e)}
