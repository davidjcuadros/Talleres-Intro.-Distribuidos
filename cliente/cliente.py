import grpc
from servicio_pb2 import OperacionRequest, ResultadoReceive
from servicio_pb2_grpc import SistemaStub

def main():
    # Crear un canal gRPC no seguro
    channel = grpc.insecure_channel('localhost:5000')
    client = SistemaStub(channel)
    print("Esperando conexión al servidor. ")
    
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
        print("Conexión al servidor gRPC exitosa.")
        
        # Enviar solicitud al servidor
        solicitud = OperacionRequest(tipoOperacion=0, dato=10)
        respuesta = client.SolicitudOperacion(solicitud)
        
        print(f"Resultado final recibido del servidor: {respuesta.resultado}")
    
    except grpc.FutureTimeoutError:
        print("No se pudo conectar al servidor gRPC.")
    except grpc.RpcError as e:
        print(f"Error al comunicarse con el servidor: {e}")

if __name__ == "__main__":
    main()