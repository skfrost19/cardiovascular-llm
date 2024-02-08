import sys


def error_message_detail(error, error_detail: sys):
    """
    This function is used to get the error message detail
    """
    _, _, exec_tb = error_detail.exc_info()
    error_message = "Error Occured in Python Script: [{0}]\nLine Number: [{1}]\nError Message: [{2}]".format(
        exec_tb.tb_frame.f_code.co_filename, exec_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
