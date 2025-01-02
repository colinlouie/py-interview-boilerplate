from pydantic import BaseModel, Field


# Field() provides the ability to specify an optional default, and example.
class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
