from pydantic import BaseModel


# Define the model for each item in the list
class EngineStatus(BaseModel):
    engine: str
    value: int
