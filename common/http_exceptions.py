from fastapi import HTTPException


class UnderMaintenanceException(HTTPException):
    def __init__(self, detail="Service is under maintenance"):
        super().__init__(status_code=503, detail=detail)

    def __str__(self):
        return f"{self.detail}"
