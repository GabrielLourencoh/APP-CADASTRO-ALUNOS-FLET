import flet as ft

# Listas para armazenar dados
alunos = []
aulas = []

def main(page: ft.Page):
    page.title = "Cadastro de Alunos"

    # Criar aluno aba
    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
    aulas_faixa_field = ft.TextField(label="Aulas necessárias para a faixa", value="10")  # Aulas para a faixa
    create_result = ft.Text()

    def criar_aluno_click(e):
        aluno = {
            "id": len(alunos) + 1,  # Gerando um ID único
            "nome": nome_field.value,
            "email": email_field.value,
            "faixa": faixa_field.value,
            "data_nascimento": data_nascimento_field.value,
            "aulas_necessarias_para_faixa": int(aulas_faixa_field.value),  # Aulas para a faixa
        }
        alunos.append(aluno)
        create_result.value = f'Aluno criado: {aluno["nome"]}'
        page.update()

    create_button = ft.ElevatedButton(text="Criar Aluno", on_click=criar_aluno_click)

    criar_aluno_tab = ft.Column(
        [
            nome_field, email_field, faixa_field, data_nascimento_field, aulas_faixa_field, create_result, create_button
        ],
        scroll=True
    )

    # Listar aluno aba
    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('ID')),
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('Email')),
            ft.DataColumn(ft.Text('Faixa')),
            ft.DataColumn(ft.Text('Data Nascimento')),
            ft.DataColumn(ft.Text('Aulas para Faixa')),
        ],
        rows=[]
    )
    list_result = ft.Text()

    def listar_alunos_click(e):
        students_table.rows.clear()
        for aluno in alunos:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(aluno['id']))),  # Usando o ID para listar
                    ft.DataCell(ft.Text(aluno["nome"])),
                    ft.DataCell(ft.Text(aluno["email"])),
                    ft.DataCell(ft.Text(aluno["faixa"])),
                    ft.DataCell(ft.Text(aluno["data_nascimento"])),
                    ft.DataCell(ft.Text(str(aluno["aulas_necessarias_para_faixa"]))),  # Aulas para faixa
                ]
            )
            students_table.rows.append(row)
        list_result.value = f'{len(alunos)} alunos encontrados.'
        page.update()

    list_button = ft.ElevatedButton(text="Listar Alunos", on_click=listar_alunos_click)
    listar_aluno_tab = ft.Column([students_table, list_button], scroll=True)

    # Adicionar aulas
    email_aula_field = ft.TextField(label="Email do Aluno")
    qtd_field = ft.TextField(label="Quantidade de aulas", value="1")
    aula_result = ft.Text()

    def marcar_aula_click(e):
        aluno_encontrado = None
        for aluno in alunos:
            if aluno['email'] == email_aula_field.value:
                aluno_encontrado = aluno
                break
        
        if aluno_encontrado:
            aula = {
                "email_aluno": email_aula_field.value,
                "qtd": int(qtd_field.value),
            }
            aulas.append(aula)
            aula_result.value = f"Aula(s) marcada(s) para o aluno {aluno_encontrado['nome']}: {aula['qtd']} aula(s)"
        else:
            aula_result.value = "Aluno não encontrado."
        page.update()

    aula_button = ft.ElevatedButton(text="Marcar Aula Realizada", on_click=marcar_aula_click)
    aula_tab = ft.Column([email_aula_field, qtd_field, aula_result, aula_button], scroll=True)

    # Progresso do aluno
    email_progress_field = ft.TextField(label="Email do Aluno")
    progress_result = ft.Text()

    def consultar_progresso_click(e):
        aluno_encontrado = None
        for aluno in alunos:
            if aluno['email'] == email_progress_field.value:
                aluno_encontrado = aluno
                break
        
        if aluno_encontrado:
            total_aulas = 0
            for aula in aulas:
                if aula["email_aluno"] == aluno_encontrado["email"]:
                    total_aulas += aula["qtd"]
            aulas_necessarias = aluno_encontrado["aulas_necessarias_para_faixa"]
            progress_result.value = (
                f'Nome: {aluno_encontrado["nome"]}\n'
                f"Email: {aluno_encontrado['email']}\n"
                f"Faixa: {aluno_encontrado['faixa']}\n"
                f"Total de aulas: {total_aulas}\n"
                f"Aulas necessárias para a próxima faixa: {aulas_necessarias - total_aulas}\n"
            )
        else:
            progress_result.value = "Aluno não encontrado."
        page.update()

    progress_button = ft.ElevatedButton(text="Consultar progresso", on_click=consultar_progresso_click)
    progress_tab = ft.Column([email_progress_field, progress_result, progress_button], scroll=True)


    # Atualizar aluno
    id_aluno_field = ft.TextField(label="ID do Aluno")
    nome_update_field = ft.TextField(label="Novo Nome")
    email_update_field = ft.TextField(label="Novo Email")
    faixa_update_field = ft.TextField(label="Nova Faixa")
    data_nascimento_update_field = ft.TextField(label="Nova Data de Nascimento (YYYY-MM-DD)")
    update_result = ft.Text()

    def atualizar_aluno_click(e):
        aluno_id = int(id_aluno_field.value)
        aluno = None
        for a in alunos:
            if a['id'] == aluno_id:  # Usando 'id' para localizar o aluno
                aluno = a
                break

        if aluno:
            aluno["nome"] = nome_update_field.value or aluno["nome"]
            aluno["email"] = email_update_field.value or aluno["email"]
            aluno["faixa"] = faixa_update_field.value or aluno["faixa"]
            aluno["data_nascimento"] = data_nascimento_update_field.value or aluno["data_nascimento"]
            update_result.value = f'Aluno atualizado: {aluno["nome"]}'
        else:
            update_result.value = "Aluno não encontrado."
        page.update()

    update_button = ft.ElevatedButton(text="Atualizar aluno", on_click=atualizar_aluno_click)
    atualizar_tab = ft.Column(
        [
            id_aluno_field, nome_update_field, email_update_field,
            faixa_update_field, data_nascimento_update_field, update_button, update_result
        ],
        scroll=True,
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
            ft.Tab(text="Listar Alunos", content=listar_aluno_tab),
            ft.Tab(text="Cadastrar Aula", content=aula_tab),
            ft.Tab(text="Progresso do Aluno", content=progress_tab),
            ft.Tab(text="Atualizar Aluno", content=atualizar_tab),
        ]
    )

    page.add(tabs)


if __name__ == "__main__":
    ft.app(target=main)
