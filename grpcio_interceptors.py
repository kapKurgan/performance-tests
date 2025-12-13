import grpc
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserResponse, GetUserRequest
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub


class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request1):
        print(client_call_details, type(client_call_details))
        print(f"Calling method: {client_call_details}")
        response1 = continuation(client_call_details, request1)
        return response1


channel = grpc.insecure_channel("localhost:9003")
intercept_channel = grpc.intercept_channel(channel, SimpleLoggingInterceptor())

stub = UsersGatewayServiceStub(intercept_channel)

request = GetUserRequest(id="05128864-578f-4d48-947c-fad55573e8a9")
response = stub.GetUser(request)
print(response)
