# python -m grpc_test_server

import grpc  # Библиотека gRPC
from concurrent import futures  # Для создания пула потоков
import grpc_test_greeting_pb2
import grpc_test_greeting_pb2_grpc


# Наследуемся от сгенерированного класса GreeterServicer
class GreeterServicer(grpc_test_greeting_pb2_grpc.GreeterServicer):
    # Реализация метода SayHello
    def SayHello(self, request, context):
        # request — объект HelloRequest
        # context — информация о вызове (метаданные, статус и т.д.)
        name = request.name
        message = f"Привет, {name}!"  # Формируем сообщение
        print("Запрос от клиента:", request)
        # Возвращаем HelloReply с текстом
        return grpc_test_greeting_pb2.HelloReply(message=message)


def serve():
    # Создаём gRPC-сервер с пулом потоков на 10 воркеров
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем наш сервис на сервере
    grpc_test_greeting_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Назначаем порт, на котором будет слушать сервер
    server.add_insecure_port('[::]:50051')  # [::] — для IPv4/IPv6

    print("Запуск сервера на порту 50051...")
    server.start()  # Запуск сервера
    server.wait_for_termination()  # Ожидание завершения (бесконечно)


if __name__ == '__main__':
    serve()


