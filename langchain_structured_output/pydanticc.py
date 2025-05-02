# Pydantic is a Python library that helps you define and validate data structures easily using Python classes.
# If we want the model to return a Pydantic object, we just need to pass in the desired Pydantic class. The key advantage of using Pydantic is that the model-generated output will be validated. Pydantic will raise an error if any required fields are missing or if any fields are of the wrong type.


from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10)
    
student = Student(name="santosh",age="20",email="santosh@gmail.com",cgpa=9.5)

# this pydantic class object can be converted to the python dict object and vice versa
python_dict = student.model_dump()
print(type(python_dict))
print(student)

#similary we can convert it into the json object
json_object = student.model_dump_json()
print(type(json_object))
print(json_object)