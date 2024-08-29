import grpc
from concurrent import futures
from servicio_pb2_grpc import SistemaServicer, add_SistemaServicer_to_server
from servicio_pb2 import ResultadoReceive, OperacionRequest

class ServicioSistema(SistemaServicer):
    def Listo(self, request, context):
        return request

    def OperacionParcial(self, request, context):
        tipo_operacion = request.tipoOperacion
        dato = request.dato
        resultado = 0

        if tipo_operacion == 1:
            resultado = dato * 2
        elif tipo_operacion == 2:
            resultado = dato + 2
        elif tipo_operacion == 3:
            resultado = dato / 2
        elif tipo_operacion == 4:
            resultado = dato ** 2
        else:
            context.set_details('Operación no válida')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        print(f"Resultado: {resultado}")
        print("Enviando a servidor principal. ")
        return ResultadoReceive(resultado=resultado)

def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SistemaServicer_to_server(ServicioSistema(), server)
    server.add_insecure_port('[::]:5002')
    print("El servidor 2 está ejecutándose. Esperando solicitud de cliente.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()
