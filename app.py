import flet as ft
import requests


API_BASE_URL = "http://localhost:8000/api" #se for feito o deploy, só trocar essa constante pelo dominio

def main(page: ft.Page):
    page.title = "Cadastro de Alunos"

    #Criar aluno aba
    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
    create_result = ft.Text()

    def criar_aluno_click(e): #parametro "e" seria evento
        payload = {
            "nome": nome_field.value,
            "email": email_field.value,
            "faixa": faixa_field.value,
            "data_nascimento": data_nascimento_field.value,
        }
        response = requests.post(API_BASE_URL + '/', json=payload)

        if response.status_code == 200: #200 seria o status de sucesso
            aluno = response.json()
            create_result.value = f'Aluno criado: {aluno}'
        else:
            create_result.value = f"Erro: {response.text}"
        page.update()
           

    create_button = ft.ElevatedButton(text="Criar Aluno", on_click=criar_aluno_click)

    criar_aluno_tab = ft.Column(
        [
            nome_field, email_field, faixa_field, data_nascimento_field, create_result, create_button
        ],
        scroll=True
    )

    # Listar aluno aba
    students_table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text('ID')),
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('Email')),
            ft.DataColumn(ft.Text('Faixa')),
            ft.DataColumn(ft.Text('Data Nascimento')),
        ],
        rows=[]
    )
    list_result = ft.Text()

    def listar_alunos_click(e):
        response = requests.get(API_BASE_URL + '/aluno/')
        alunos = response.json()
        students_table.rows.clear()

        for aluno in alunos:
            row = ft.DataRow(
                cells = [
                    ft.DataCell(ft.Text(aluno.get('id'))),
                    ft.DataCell(ft.Text(aluno.get('nome'))),
                    ft.DataCell(ft.Text(aluno.get('email'))),
                    ft.DataCell(ft.Text(aluno.get('faixa'))),
                    ft.DataCell(ft.Text(aluno.get('data_nascimento'))),
                ]
            )
            students_table.rows.append(row)
            list_result.value = f'{len(aluno)} alunos encontrados.'
        page.update()



    list_button = ft.ElevatedButton(text="Listar Alunos", on_click=listar_alunos_click)
    listar_aluno_tab = ft.Column([students_table, list_button], scroll=True)
    
    #Adicionar aulas

    email_aula_field = ft.TextField(label="Email do Aluno")
    qtd_field = ft.TextField(label="Quantidade de aulas", value="1")
    aula_result = ft.Text()
 
    def marcar_aula_click(e):
        payload = {
            "qtd": int(qtd_field.value),
            "email_aluno": email_aula_field,
        }
        response = requests.post(API_BASE_URL + '/aula_realizar/', json=payload)
        if response.status_code == 200:
            aula_result.value = f"Sucesso: {response.json()}"
        else:
            aula_result.value = f"Erro: {response.text}"
        page.update()

    aula_button = ft.ElevatedButton(text="Marcar Aula Realizada", on_click=marcar_aula_click)
    aula_tab = ft.Column([email_aula_field, qtd_field, aula_result, aula_button], scroll=True)

    # Progresso do aluno
    email_progress_field = ft.TextField(label="Email do Aluno")
    progress_result = ft.Text()
    
    def consultar_progresso_click(e):
        email = email_progress_field.value
        response = requests.get(API_BASE_URL + '/progresso_aluno/', params={'email_aluno': email})
        if response.status_code == 200:
            progress = response.json()
            progress_result.value(
                f'Nome: {progress.get('nome')}\n'
                f"Email: {progress.get('email')}\n"
                f"Faixa: {progress.get('faixa')}\n"
                f"Total de aulas: {progress.get('total_aulas')}\n"
                f"Aulas necessárias para a próxima faixa: {progress.get('aulas_necessarias_para_proxima_faixa')}\n"
            )
        else:
            progress_result.value = f"Erro: {response.text}"
        page.update()

    progress_button = ft.ElevatedButton(text="Consultar progresso", on_click=consultar_progresso_click)
    progress_tab = ft.Column([email_progress_field, progress_result ,progress_button], scroll=True)

    # Atualizar aluno
    id_aluno_field = ft.TextField(label="ID do Aluno")
    nome_update_field = ft.TextField(label="Novo Nome")
    email_update_field = ft.TextField(label="Novo Email")
    faixa_update_field = ft.TextField(label="Nova Faixa")
    data_nascimento_update_field = ft.TextField(label="Nova Data de Nascimento (YYYY-MM-DD)")
    update_result = ft.Text()

    def atualizar_aluno_click(e):
        aluno_id = id_aluno_field.value
        if not aluno_id:
            update_result.value = "ID do aluno é obrigatório"
        else:
            payload = {
                "nome": nome_update_field.value, 
                "email": email_update_field.value,
                "faixa": faixa_update_field.value,
                "data_nascimento":data_nascimento_update_field.value
                
            }
            
            response = requests.put(API_BASE_URL + f'/alunos/{aluno_id}', json=payload)
            if response.status_code == 200:
                aluno = response.json()
                update_result.value = f'Aluno atualizado: {aluno}'
            else:
                update_result.value = f"Erro: {response.text}"
        page.update()

    update_button = ft.ElevatedButton(text="Atualizar aluno", on_click=atualizar_aluno_click)
    atualizar_tab = ft.Column(
        [
            id_aluno_field, #TODO virar um campo do tipo select, pegando pelo id de tds cadastrados 
            nome_update_field,
            email_update_field,
            faixa_update_field,
            data_nascimento_update_field,
            update_button,
            update_result,
        ],
        scroll=True,
    )

    tabs = ft.Tabs(
        selected_index=0, 
        tabs= [
            ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
            ft.Tab(text="Listar Alunos", content=listar_aluno_tab),
            ft.Tab(text="Cadastrar Aula", content=aula_tab),
            ft.Tab(text="Progresso do Aluno", content=progress_tab),
            ]
    )

    page.add(tabs)



if __name__ == "__main__":
    ft.app(target=main)