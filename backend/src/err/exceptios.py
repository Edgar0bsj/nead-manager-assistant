class EntityNotFoundException(Exception):

    def __init__(self):
        mensagem = f"Entidade não encontrado no banco de dados."
        super().__init__(mensagem)
