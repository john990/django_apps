from datetime import datetime, date

__author__ = 'kai.wang'


class ModelToJson:
    def __init__(self):
        pass

    @staticmethod
    def to_json(model):
        """
        将model转换为json
        """
        keys = []
        for field in model._meta.fields:
            keys.append(field.name)

        d = {}
        for key in keys:
            value = getattr(model, key)
            if isinstance(value, datetime):
                print value
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, date):
                print value
                value = value.strftime('%Y-%m-%d')
            d[key] = value
        import json

        return json.dumps(d)