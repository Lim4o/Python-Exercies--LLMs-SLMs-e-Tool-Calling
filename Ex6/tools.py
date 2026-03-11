eventos = []


def criar_evento(titulo: str, data: str):
    evento = {
        "titulo": titulo,
        "data": data,
    }
    eventos.append(evento)
    return f"Evento '{titulo}' criado para {data}."


def listar_eventos():
    if not eventos:
        return "Você ainda não tem eventos cadastrados."

    linhas = []
    for indice, evento in enumerate(eventos, start=1):
        linhas.append(f"{indice}. {evento['titulo']} - {evento['data']}")

    return "Seus eventos:\n" + "\n".join(linhas)
         