import json
from pydantic import BaseModel, Field

class Companies(BaseModel):
    Name: str = Field(alias='Name_Ins')
    No: str
    Address: str
    Tax_ID:str = Field(alias= 'tax_ID_number')
    X: str = Field(alias= 'wgs84aX')
    Y:str = Field(alias= 'wgs84aY')
    
class Result(BaseModel):
    records:list[Companies]

class Food_Processing_Company(BaseModel):
    result:Result

with open('新北市食品工廠清冊.json') as file:
    content:str = file.read()
    fpc:Food_Processing_Company = Food_Processing_Company.model_validate_json(content)
    
fpcs = fpc.result.records
for _ in fpcs:
    print(_) 