from fastapi import FastAPI, status, HTTPException
from math import sqrt as sqrt

app = FastAPI()

@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    
    try: 
        a = float(a)
        b = float(b)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtract two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try: 
        a = float(a)
        b = float(b)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try: 
        a = float(a)
        b = float(b)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divide two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result or an error if dividing by zero.
    """
    try: 
        a = float(a)
        b = float(b)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    
    try:
        if (b == 0):
            raise ZeroDivisionError
    except ZeroDivisionError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Division by zero is not allowed. Please provide a non-zero value for b.")
    return {"result": a / b}

@app.get("/pow/{a}/{b}", status_code=200)
def pow(a: str, b: str):
    """
    a to the power of b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try: 
        a = float(a)
        b = float(b)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": a ** b}

@app.get("/sqrt/{a}", status_code=200)
def square_root(a: str):
    """
    Square root of a.
    
    Parameter:
    - a: First number
    
    Returns:
    - JSON object with the result
    """
    try: 
        a = float(a)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": sqrt(a)}

@app.get("/avg/{a}/{b}/{c}", status_code=200)
def average(a: str, b: str, c: str):
    """
    Average the three numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    - c: Third number
    
    Returns:
    - JSON object with the result
    """

    try: 
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All arguments must be valid numbers.")
    return {"result": (sum([a, b, c]) / 3)}
