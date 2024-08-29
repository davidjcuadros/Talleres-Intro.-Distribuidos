from servicio_pb2 import OperacionRequest, ResultadoReceive
from servicio_pb2_grpc import SistemaStub, SistemaServicer, add_SistemaServicer_to_server

import grpc 
from concurrent import futures

# Implementación del servicio
class ServicioSistema(SistemaServicer):
    def Listo(self, request, context):
        return request

    def SolicitudOperacion(self, request, context):
        print("Solicitud de operación recibida.")
        resultado_total = procesar_solicitudes_a_servidores(request.dato)
        return ResultadoReceive(resultado=resultado_total)

#---------------------------------------------------------------------------
def procesar_solicitudes_a_servidores(dato):
    servidores = [
        '[::]:5001',
        '[::]:5002',
        '[::]:5003',
        '[::]:5004'
    ]
    resultados = []
    for i, servidor in enumerate(servidores):
        tipo_operacion = i + 1  # El tipo de operación varía entre 1 y 4
        print("Aqui")
        resultado = enviar_solicitud(servidor, tipo_operacion, dato)
        """
        if resultado == -1:
            resultado = enviar_solicitud(servidor+1, tipo_operacion, dato)
        """
        print(f"Resultado de la operación en el servidor {servidor}: {resultado}")
        resultados.append(resultado)
    return sum(resultados)
#---------------------------------------------------------------------------
def enviar_solicitud(servidor, tipo_operacion, dato):
    try:
        with grpc.insecure_channel(servidor) as channel:
            stub = SistemaStub(channel)
            solicitud = OperacionRequest(tipoOperacion=tipo_operacion, dato=dato)
            respuesta = stub.OperacionParcial(solicitud)
            return respuesta.resultado
    except grpc.RpcError as e:
        print(f"Error al conectar con el servidor {servidor}: {e}")
        return -1
#---------------------------------------------------------------------------
def start():
    # Configurar y arrancar el servidor principal
    server1 = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SistemaServicer_to_server(ServicioSistema(), server1)
    server1.add_insecure_port('[::]:5000')
    print("El servidor principal se está ejecutando. Esperando solicitud de cliente.")
    server1.start()
    
    # Enviar solicitudes a otros servidores (si es necesario)
    resultado_total = procesar_solicitudes_a_servidores(10)
    print(f"Resultado Total: {resultado_total}")
    
    # Esperar la terminación del servidor
    server1.wait_for_termination()
#---------------------------------------------------------------------------
if __name__ == "__main__":
    start()