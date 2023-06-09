from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        # """Inicialize sua estrutura aqui"""
        self.queue = []

    def __len__(self):
        # """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        # """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        # """Aqui irá sua implementação"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            raise IndexError("Fila Vazia")

    def search(self, index):
        # """Aqui irá sua implementação"""
        if 0 <= index < len(self.queue):
            return self.queue[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
