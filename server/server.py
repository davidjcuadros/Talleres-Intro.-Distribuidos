from servicio_pb2_grpc import SistemaServicer, add_SistemaServicer_to_server
import grpc 
from concurrent import futures

#Probar que el servidor está vivo
class ServicioSistema(SistemaServicer):
    def Listo (self, request, context):
        return request

    def SolicitudOperacion(self, request, context):
        print("Solicitud de operación recibida.")

def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SistemaServicer_to_server(ServicioSistema(), server)
    server.add_insecure_port('[::]:5000')
    print("El servidor está ejecutándose. Esperando solicitud de cliente.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()
