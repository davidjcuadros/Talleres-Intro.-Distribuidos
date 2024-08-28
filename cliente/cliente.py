import sys
import grpc

from servicio_pb2 import OperacionRequest, Nulo, ResultadoReceive, _SISTEMA
from servicio_pb2_grpc import SistemaStub

def main():
    # Crear un canal gRPC no seguro
    channel = grpc.insecure_channel('localhost:5000')
    client = SistemaStub(channel)

    try:
        grpc.channel_ready_future(channel).result(timeout=10)
        print("Conexión al servidor gRPC exitosa.")
    except grpc.FutureTimeoutError:
        print("No se pudo conectar al servidor gRPC.")
        return

if __name__ == "__main__":
    main()
