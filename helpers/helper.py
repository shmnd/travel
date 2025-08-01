import logging, hashlib, json,socket, base64, os, sys


logger = logging.getLogger(__name__)


def get_object_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None
    
    
def get_value_or_empty(value):

    return value if value is not None else ""

    
def get_value_or_dash(value):
    
    return value if value is not None and value !='' else "-"