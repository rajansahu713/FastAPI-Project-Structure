from common.http_exceptions import UnderMaintenanceException


def check_maintenance():
    print("Checking maintenance status")
    if 1 == 2:  # Change this condition to actually check maintenance status
        raise UnderMaintenanceException
