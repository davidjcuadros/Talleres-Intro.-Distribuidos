from servicio_pb2 import OperacionRequest, ResultadoReceive
from servicio_pb2_grpc import SistemaStub, SistemaServicer, add_SistemaServicer_to_server
import grpc
from concurrent import futures

class ServicioSistema(SistemaServicer):
    def Listo(self, request, context):
        return request
    
    def SolicitudOperacion(self, request, context):
        print("Solicitud de operación recibida.")
        resultado_total = procesar_solicitudes_a_servidores(request.dato)
        return ResultadoReceive(resultado=resultado_total)

def procesar_solicitudes_a_servidores(dato):
    servidores = [
        'localhost:5001',
        'localhost:5002',
        'localhost:5003',
        'localhost:5004'
    ]
    resultados = []
    for i in range(4):  # Asumimos que necesitamos 4 operaciones
        tipo_operacion = i + 1
        resultado = enviar_solicitud_con_tolerancia(servidores, tipo_operacion, dato)
        if resultado != -1:
            resultados.append(resultado)
        else:
            print(f"No se pudo completar la operación {tipo_operacion}")
    print(f"Resultado total: {sum(resultados)}")
    return sum(resultados) if resultados else -1

def enviar_solicitud_con_tolerancia(servidores, tipo_operacion, dato):
    for servidor in servidores:
        try:
            resultado = enviar_solicitud(servidor, tipo_operacion, dato)
            if resultado != -1:
                return resultado
        except Exception as e:
            print(f"Error al conectar con el servidor {servidor}: {e}")
    
    print("Todos los servidores fallaron. No se pudo completar la operación.")
    return -1

def enviar_solicitud(servidor, tipo_operacion, dato):
    try:
        with grpc.insecure_channel(servidor) as channel:
            stub = SistemaStub(channel)
            solicitud = OperacionRequest(tipoOperacion=tipo_operacion, dato=dato)
            respuesta = stub.OperacionParcial(solicitud)
            return respuesta.resultado
    except grpc.RpcError as e:
        print(f"Error al conectar con el servidor {servidor}: {e}")
        raise  # Re-lanzamos la excepción para que sea manejada por enviar_solicitud_con_tolerancia




def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SistemaServicer_to_server(ServicioSistema(), server)
    server.add_insecure_port('[::]:5000')
    print("El servidor principal se está ejecutando. Esperando solicitud de cliente.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()