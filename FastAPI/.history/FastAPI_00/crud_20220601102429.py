
@app.get("/api/data/{id}")  # path parameter
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=400, detail=f"No car with id={id}.")