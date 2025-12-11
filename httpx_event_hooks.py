from httpx import Client, Request, Response
from datetime import datetime


def log_request(request: Request):
    request.extensions['start_time'] = datetime.now()
    print(f"REQUEST: {request.method}")

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f"RESPONSE: {response.status_code}, {duration}")



client = Client(
    base_url="http://localhost:8003",
    event_hooks={"request": [log_request], "response": [log_response]})
response = client.get("/api/v1/users/da361afc-6cd6-4ae8-806b-bd8bd8d437bc")

print(f"\n{response}")
print(response.request.extensions)

