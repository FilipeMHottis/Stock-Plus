from typing import TypedDict, List, TypeVar, Generic, Optional

T = TypeVar("T")


class StatusDetail(Generic[T], TypedDict):
    status: int
    detail: str
    data: Optional[T]


status_html: List[StatusDetail] = [
    {"status": 200, "detail": "OK"},
    {"status": 201, "detail": "Created"},
    {"status": 204, "detail": "No Content"},
    {"status": 400, "detail": "Bad Request"},
    {"status": 401, "detail": "Unauthorized"},
    {"status": 403, "detail": "Forbidden"},
    {"status": 404, "detail": "Not Found"},
    {"status": 500, "detail": "Internal Server Error"},
    {"status": 503, "detail": "Service Unavailable"},
    {"status": 504, "detail": "Gateway Timeout"},
]


def get_status_detail(
    status_code: int,
    data: Optional[T] = None,
) -> StatusDetail[T]:
    for status in status_html:
        if status["status"] == status_code:
            return {**status, "data": data}
    return {"status": status_code, "detail": "Unknown Status", "data": data}
