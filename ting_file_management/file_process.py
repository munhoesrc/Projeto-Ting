import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    # """Aqui irá sua implementação"""
    processed_files = set([item["nome_do_arquivo"] for item in instance.queue])

    if path_file in processed_files:
        print(
            f"Arquivo {path_file} já foi processado."
            "Ignorando.",
            file=sys.stdout
        )
        return

    lines = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file_data)

    print(file_data)


def remove(instance: Queue):
    # """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    removed_file = instance.dequeue()
    print(
        f"Arquivo {removed_file['nome_do_arquivo']} "
        "removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
