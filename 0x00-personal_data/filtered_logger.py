import re


def filter_datum(fields, redaction, message, separator):
    """
    function that returns the log message obfuscated

    Arguments:
        field (list): a list of strings representing all fields to obfuscate
        redaction (str): a string representing by what the field will be obfuscated
        message (str): a string representing the log message
        separator (str): string representing characters seperating fields in message.

    Returns:
        str: log message obfuscated
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  r'\1=' + redaction, message)
