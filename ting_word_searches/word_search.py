def exists_word(word, instance):
    # """Aqui irá sua implementação"""
    results = []

    for content in instance.queue:
        line_list = content["linhas_do_arquivo"]
        file_occurrences = []

        for sub_index, line in enumerate(line_list, start=1):
            if word in line.lower():
                file_occurrences.append({"linha": sub_index})

        if file_occurrences:
            result = {
                "palavra": word,
                "arquivo": content["nome_do_arquivo"],
                "ocorrencias": file_occurrences
            }
            results.append(result)

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
