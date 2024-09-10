from math import floor


def generate_response_dict(name: str, p: float):
    return {"name": name, "p": round(p, 1)}
