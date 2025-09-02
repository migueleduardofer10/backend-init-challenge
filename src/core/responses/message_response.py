from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

@dataclass
class Response(Generic[T]):
    status_code: int
    message: str
    data: Optional[T] = None

    @staticmethod
    def success(data: T, message: str = "OK") -> "Response[T]":
        return Response(status_code=200, message=message, data=data)

    @staticmethod
    def error(message: str, status_code: int = 400) -> "Response[None]":
        return Response(status_code=status_code, message=message, data=None)
