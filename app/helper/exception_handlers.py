import logging

def report_log(message, level="info", error=None, url=""):
    logging.log(getattr(logging, level.upper()), f"{message}: {error} - {url}")
