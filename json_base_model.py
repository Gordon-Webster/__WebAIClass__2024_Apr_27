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

class FoodProcessingCompany(BaseModel):
    result:Result

with open('新北市食品工廠清冊.json', encoding='utf-8') as file:
    content:str = file.read()
    fpc:FoodProcessingCompany = FoodProcessingCompany.model_validate_json(content)
    
fpcs = fpc.result.records
for _ in fpcs:
    print(_) 