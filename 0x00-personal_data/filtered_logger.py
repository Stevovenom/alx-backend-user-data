import re


def filter_datum(fields, redaction, message, separator):
    """
    function that returns the log message obfuscated

    Args:
        field: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log message
        separator: string representing characters seperating fields in message.

    Return:
        log message obfuscated
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  r'\1=' + redaction, message)
