import uuid
import random


def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:6]
    return code
