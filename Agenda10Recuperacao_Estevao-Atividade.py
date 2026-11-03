#Banco de dados

alunos = {
    "João": {
        "Geografia": [5.0, 7.5, 9.0],
        "Matemática": [6.0, 5.5, 7.0]
    },
    "Maria": {
        "Geografia": [9.0, 8.5, 7.0],
        "Matemática": [8.0, 9.5, 10.0]
    },
    "Pedro": {
        "Geografia": [4.0, 6.5, 5.0],
        "Matemática": [7.0, 6.5, 8.0]
    },
    "Ana": {
        "Geografia": [10.0, 9.5, 8.0],
        "Matemática": [9.0, 8.5, 7.0]
}
}

#Calculo das medias

def calcular_media(aluno, disciplina):
    if aluno in alunos and disciplina in alunos[aluno]:
        notas = alunos[aluno][disciplina]
        media = sum(notas) / len(notas)

        if media >= 5.0:
            return "Aprovado"
        else:
            return "Reprovado"

    else:
        return "Aluno ou disciplina não encontrados."


