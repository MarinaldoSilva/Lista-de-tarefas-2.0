from rest_framework import status
from .services import msg_error

def get_status_error(error):
    if 'Errors' in error:
        if error['Errors'] == msg_error:
            return status.HTTP_404_NOT_FOUND
    return status.HTTP_400_BAD_REQUEST


