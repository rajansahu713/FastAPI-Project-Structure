from typing import Any, Dict, Optional

from fastapi.responses import JSONResponse


def common_response(
    message: str,
    status: bool = True,
    data: Optional[Any] = None,
    status_code: int = 200,
) -> JSONResponse:
    response_content: Dict[str, Any] = {
        "message": message,
        "status": status,
        "data": data,
        "status_code": status_code,
    }
    return response_content
