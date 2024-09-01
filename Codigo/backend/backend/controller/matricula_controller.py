from model import Matricula
from view import matricula_view
from model import Aluno
from util import (
    CAMINHO_CURSOS,
    CAMINHO_DISCIPLINAS,
    CAMINHO_USUARIOS,
    divider,
    ler_arquivo,
    menu,
    pedir_dados_usuario,
)
import json

# def create_matricula(self, idMatricula: int, data: str, aluno: Aluno):
#     pass

def load_json_file(filename):
    """Helper function to load JSON data from a file."""
    with open(filename, 'r') as file:
        return json.load(file)
    

def save_json_file(filename, data):
    """Helper function to save JSON data to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_matricula():
    # Carregar dados dos arquivos JSON
    cursos = load_json_file(CAMINHO_CURSOS)
    disciplinas = load_json_file(CAMINHO_DISCIPLINAS)
    usuarios = load_json_file(CAMINHO_USUARIOS)
    
    # Solicitar e-mail do aluno
    aluno_email = input("Digite o e-mail do aluno: ")
    
    # Encontrar os dados do aluno no arquivo usuarios.json
    aluno_info = usuarios.get(aluno_email)
    
    if aluno_info is None or aluno_info['tipo'] != 'aluno':
        print("Aluno não encontrado ou e-mail inválido.")
        return
    
    # Mostrar cursos disponíveis
    print("Cursos disponíveis:")
    for i, curso in enumerate(cursos.keys(), start=1):
        print(f"{i}. {curso}")
    
    # Solicitar curso ao usuário
    curso_index = int(input("Escolha o número do curso para matrícula: ")) - 1
    curso_nome = list(cursos.keys())[curso_index]
    
    if curso_nome not in cursos:
        print("Curso inválido.")
        return
    
    curso_selecionado = cursos[curso_nome]
    print(f"Você escolheu o curso: {curso_selecionado['nome']}")
    
    # Mostrar semestres disponíveis
    print("Semestres disponíveis:")
    for i, semestre in enumerate(curso_selecionado['semestres'], start=1):
        print(f"{i}. Período {semestre['periodo']}")
    
    # Solicitar semestre ao usuário
    semestre_index = int(input("Escolha o número do semestre para matrícula: ")) - 1
    if semestre_index < 0 or semestre_index >= len(curso_selecionado['semestres']):
        print("Semestre inválido.")
        return
    
    semestre_selecionado = curso_selecionado['semestres'][semestre_index]
    print(f"Você escolheu o período: {semestre_selecionado['periodo']}")
    
    # Mostrar disciplinas disponíveis no semestre selecionado
    print("Disciplinas disponíveis:")
    disciplinas_disponiveis = {}
    for i, disciplina in enumerate(semestre_selecionado['disciplinas'], start=1):
        disciplinas_disponiveis[i] = disciplina['nome']
        print(f"{i}. {disciplina['nome']}")
    
    # Solicitar disciplinas ao usuário
    disciplinas_escolhidas = []
    while True:
        disciplina_index = int(input("Escolha o número da disciplina para adicionar (0 para terminar): "))
        if disciplina_index == 0:
            break
        if disciplina_index not in disciplinas_disponiveis:
            print("Disciplina inválida.")
            continue
        disciplina_nome = disciplinas_disponiveis[disciplina_index]
        disciplinas_escolhidas.append(disciplina_nome)
    
    if not disciplinas_escolhidas:
        print("Nenhuma disciplina escolhida.")
        return
    
    # Calcular e registrar o valor total
    valor_total = 0
    
    # Atualizar as disciplinas com o novo aluno
    for semestre in curso_selecionado['semestres']:
        for disciplina in semestre['disciplinas']:
            if disciplina['nome'] in disciplinas_escolhidas:
                if 'alunos' not in disciplina:
                    disciplina['alunos'] = []  # Inicializa a lista se não existir
                # Adiciona o aluno apenas se não estiver já na lista
                aluno_existente = any(aluno['email'] == aluno_info['email'] for aluno in disciplina['alunos'])
                if not aluno_existente:
                    disciplina['alunos'].append(aluno_info)
                # Calcular o valor da disciplina
                carga_horaria = disciplina.get('carga_horaria', 0)
                preco_por_hora = disciplina.get('preco_por_hora', 0)
                valor_total += carga_horaria * preco_por_hora
    
    # Salvar os dados atualizados
    save_json_file(CAMINHO_CURSOS, cursos)
    save_json_file(CAMINHO_DISCIPLINAS, disciplinas)
    
    # Criar matrícula
    matricula = {
        'curso': curso_selecionado['nome'],
        'disciplinas': disciplinas_escolhidas,
        'valor_total': valor_total
    }
    
    # Exibir informações da matrícula
    print("Matrícula criada com sucesso!")
    print("Curso:", matricula['curso'])
    print("Disciplinas:", ", ".join(matricula['disciplinas']))
    print(f"Valor total a ser pago: R${valor_total:.2f}")


def editar_matricula():
    # Carregar dados dos arquivos JSON
    cursos = load_json_file(CAMINHO_CURSOS)
    disciplinas = load_json_file(CAMINHO_DISCIPLINAS)
    usuarios = load_json_file(CAMINHO_USUARIOS)

    # Solicitar e-mail do aluno
    aluno_email = input("Digite o e-mail do aluno para editar a matrícula: ")

    # Encontrar os dados do aluno no arquivo usuarios.json
    aluno_info = usuarios.get(aluno_email)

    if aluno_info is None or aluno_info['tipo'] != 'aluno':
        print("Aluno não encontrado ou e-mail inválido.")
        return

    # Encontrar as matrículas atuais do aluno
    aluno_matriculas = []
    for curso_nome, curso in cursos.items():
        for semestre in curso['semestres']:
            for disciplina in semestre['disciplinas']:
                if any(aluno['email'] == aluno_email for aluno in disciplina.get('alunos', [])):
                    aluno_matriculas.append({
                        'curso': curso_nome,
                        'semestre': semestre['periodo'],
                        'disciplina': disciplina['nome']
                    })

    if not aluno_matriculas:
        print("O aluno não está matriculado em nenhum curso.")
        return

    # Mostrar matrículas atuais
    print("Matrículas atuais do aluno:")
    for i, matricula in enumerate(aluno_matriculas, start=1):
        print(f"{i}. Curso: {matricula['curso']}, Semestre: {matricula['semestre']}, Disciplina: {matricula['disciplina']}")

    # Solicitar matrícula a ser editada
    matricula_index = int(input("Escolha o número da matrícula para editar (0 para cancelar): ")) - 1
    if matricula_index < 0 or matricula_index >= len(aluno_matriculas):
        print("Matrícula inválida.")
        return
    
    matricula_selecionada = aluno_matriculas[matricula_index]
    curso_nome = matricula_selecionada['curso']
    semestre_periodo = matricula_selecionada['semestre']
    disciplina_nome = matricula_selecionada['disciplina']

    # Remover a matrícula antiga
    for semestre in cursos[curso_nome]['semestres']:
        if semestre['periodo'] == semestre_periodo:
            for disciplina in semestre['disciplinas']:
                if disciplina['nome'] == disciplina_nome:
                    disciplina['alunos'] = [aluno for aluno in disciplina.get('alunos', []) if aluno['email'] != aluno_email]
                    break

    # Solicitar novas opções de matrícula
    print("Escolha um novo curso:")
    for i, curso in enumerate(cursos.keys(), start=1):
        print(f"{i}. {curso}")
    
    novo_curso_index = int(input("Escolha o número do novo curso: ")) - 1
    novo_curso_nome = list(cursos.keys())[novo_curso_index]
    
    if novo_curso_nome not in cursos:
        print("Curso inválido.")
        return
    
    # Mostrar semestres disponíveis do novo curso
    print("Semestres disponíveis:")
    for i, semestre in enumerate(cursos[novo_curso_nome]['semestres'], start=1):
        print(f"{i}. Semestre {semestre['periodo']}")
    
    novo_semestre_index = int(input("Escolha o número do novo semestre: ")) - 1
    if novo_semestre_index < 0 or novo_semestre_index >= len(cursos[novo_curso_nome]['semestres']):
        print("Semestre inválido.")
        return
    
    novo_semestre = cursos[novo_curso_nome]['semestres'][novo_semestre_index]

    # Mostrar disciplinas disponíveis no novo semestre
    print("Disciplinas disponíveis:")
    for i, disciplina in enumerate(novo_semestre['disciplinas'], start=1):
        print(f"{i}. {disciplina['nome']}")
    
    nova_disciplina_index = int(input("Escolha o número da nova disciplina: ")) - 1
    if nova_disciplina_index < 0 or nova_disciplina_index >= len(novo_semestre['disciplinas']):
        print("Disciplina inválida.")
        return
    
    nova_disciplina_nome = novo_semestre['disciplinas'][nova_disciplina_index]['nome']

    # Adicionar aluno na nova disciplina
    for semestre in cursos[novo_curso_nome]['semestres']:
        if semestre['periodo'] == novo_semestre['periodo']:
            for disciplina in semestre['disciplinas']:
                if disciplina['nome'] == nova_disciplina_nome:
                    if 'alunos' not in disciplina:
                        disciplina['alunos'] = []
                    if aluno_info not in disciplina['alunos']:
                        disciplina['alunos'].append(aluno_info)
                    break
                
    # Salvar os dados atualizados
    save_json_file(CAMINHO_CURSOS, cursos)
    save_json_file(CAMINHO_DISCIPLINAS, disciplinas)
    
    # Confirmar alteração
    print("Matrícula atualizada com sucesso!")
    print(f"Novo curso: {novo_curso_nome}")
    print(f"Novo semestre: {novo_semestre['periodo']}")
    print(f"Nova disciplina: {nova_disciplina_nome}")
    
    
def excluir_matricula():
    # Carregar dados dos arquivos JSON
    cursos = load_json_file(CAMINHO_CURSOS)
    disciplinas = load_json_file(CAMINHO_DISCIPLINAS)
    usuarios = load_json_file(CAMINHO_USUARIOS)

    # Solicitar e-mail do aluno
    aluno_email = input("Digite o e-mail do aluno para excluir a matrícula: ")

    # Encontrar os dados do aluno no arquivo usuarios.json
    aluno_info = usuarios.get(aluno_email)

    if aluno_info is None or aluno_info['tipo'] != 'aluno':
        print("Aluno não encontrado ou e-mail inválido.")
        return

    # Encontrar as matrículas atuais do aluno
    aluno_matriculas = []
    for curso_nome, curso in cursos.items():
        for semestre in curso['semestres']:
            for disciplina in semestre['disciplinas']:
                if any(aluno['email'] == aluno_email for aluno in disciplina.get('alunos', [])):
                    aluno_matriculas.append({
                        'curso': curso_nome,
                        'semestre': semestre['periodo'],
                        'disciplina': disciplina['nome']
                    })

    if not aluno_matriculas:
        print("O aluno não está matriculado em nenhum curso.")
        return

    # Mostrar matrículas atuais
    print("Matrículas atuais do aluno:")
    for i, matricula in enumerate(aluno_matriculas, start=1):
        print(f"{i}. Curso: {matricula['curso']}, Semestre: {matricula['semestre']}, Disciplina: {matricula['disciplina']}")

    # Solicitar matrícula a ser excluída
    matricula_index = int(input("Escolha o número da matrícula para excluir (0 para cancelar): ")) - 1
    if matricula_index < 0 or matricula_index >= len(aluno_matriculas):
        print("Matrícula inválida.")
        return
    
    matricula_selecionada = aluno_matriculas[matricula_index]
    curso_nome = matricula_selecionada['curso']
    semestre_periodo = matricula_selecionada['semestre']
    disciplina_nome = matricula_selecionada['disciplina']

    # Remover a matrícula
    for semestre in cursos[curso_nome]['semestres']:
        if semestre['periodo'] == semestre_periodo:
            for disciplina in semestre['disciplinas']:
                if disciplina['nome'] == disciplina_nome:
                    disciplina['alunos'] = [aluno for aluno in disciplina.get('alunos', []) if aluno['email'] != aluno_email]
                    break

    # Se o aluno não estiver matriculado em nenhuma disciplina, também remover do curso
    aluno_matriculado_em_outro = any(
        aluno_email in [a['email'] for semestre in curso['semestres'] for disciplina in semestre['disciplinas'] for a in disciplina.get('alunos', [])]
        for curso in cursos.values()
    )
    
    if not aluno_matriculado_em_outro:
        cursos[curso_nome]['alunos'] = [aluno for aluno in cursos[curso_nome].get('alunos', []) if aluno['email'] != aluno_email]

    # Salvar os dados atualizados
    save_json_file(CAMINHO_CURSOS, cursos)
    save_json_file(CAMINHO_DISCIPLINAS, disciplinas)
    
    # Confirmar exclusão
    print("Matrícula excluída com sucesso!")
    print(f"Curso: {curso_nome}")
    print(f"Semestre: {semestre_periodo}")
    print(f"Disciplina: {disciplina_nome}")

