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
    server1 = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SistemaServicer_to_server(ServicioSistema(), server1)
    server1.add_insecure_port('[::]:5000')
    print("El servidor principal se está ejecutando. Esperando solicitud de cliente.")
    server1.start()
    
    server1.wait_for_termination()

    # -------------------------------------------

def enviar_solicitud(servidor, tipo_operacion, dato):
    with grpc.insecure_channel(servidor) as channel:
        stub = SistemaStub(channel)
        solicitud = OperacionRequest(tipoOperacion=tipo_operacion, dato=dato)
        respuesta = stub.OperacionParcial(solicitud)
        return respuesta.resultado

if __name__ == "__main__":
    start()

    servidores = [
        'localhost:5001',
        'localhost:5002',
        'localhost:5003',
        'localhost:5004'
    ]
    dato = 10
    resultados = []

    for i, servidor in enumerate(servidores):
        tipo_operacion = i + 1  # El tipo de operación varía entre 1 y 4
        resultado = enviar_solicitud(servidor, tipo_operacion, dato)
        print(f"Resultado de la operación en el servidor {servidor}: {resultado}")
        resultados.append(resultado)

    print(f"Resultado Total {sum(resultados)}")
