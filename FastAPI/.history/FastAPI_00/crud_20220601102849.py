



# GET
@app.get("/api/data/{id}")  # path parameter
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=400, detail=f"No car with id={id}.")
    
    
    
    
    
# POST
@app.post("/api/cars/", response_model=CarOutput)
async def add_car(car: CarInput) -> CarOutput:
    new_car = CarOutput(size=car.size, doors=car.doors,
                        fuel=car.fuel,
                        transmission=car.transmission,
                        id=len(db) + 1)
    db.append(new_car)
    save_db(db)
    return new_car