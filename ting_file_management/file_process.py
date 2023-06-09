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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
