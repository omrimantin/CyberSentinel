import json

class Protocol:
    @staticmethod
    def pack(alert_type, details_dict):
        return json.dumps({
            "type": alert_type,
            "payload": details_dict
        }).encode('utf-8')

    @staticmethod
    def unpack(data):
        json_string = data.decode('utf-8')
        return json.loads(json_string)
        

