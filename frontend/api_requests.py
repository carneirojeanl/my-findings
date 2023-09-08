import requests


class Request:

    @staticmethod
    def post_new_finding(payload):
        endpoint = "http://localhost:8000/api/products/products/"
        r = requests.post(endpoint, data=payload)
        return r.status_code

    @staticmethod
    def get_findings():
        endpoint = "http://localhost:8000/api/products/products/"
        r = requests.get(endpoint)
        return r.json()

    @staticmethod
    def update_finding(payload, finding_id):
        endpoint = f"http://localhost:8000/api/products/products/{finding_id}/"
        r = requests.put(endpoint, data=payload)
        return r.status_code

    @staticmethod
    def delete_finding(finding_id):
        endpoint = f"http://localhost:8000/api/products/products/{finding_id}/"
        r = requests.delete(endpoint)
        return r.status_code


