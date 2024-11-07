#!/usr/bin/env python3
"""
Main file
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    This function replaces the values of specified fields in a log message with a redaction string.

    Args:
        fields (list): A list of field names to obfuscate.
        redaction (str): The string used to replace the values.
        message (str): The log message to process.
        separator (str): The separator used in the log message.

    Returns:
        str: The obfuscated log message.
    """
    return re.sub(r'(' + '|'.join([re.escape(field) for field in fields]) + r')=[^' + re.escape(separator) + r']+', lambda m: m.group(0).split('=')[0] + '=' + redaction, message)
