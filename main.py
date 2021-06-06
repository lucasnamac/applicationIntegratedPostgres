import psycopg2
import json

DBHOST = "200.131.206.13"
DATABASE = "lucasnm"
USER = "lucasnm"
PASSWORD = "f1g1a5b4c3d2e1"
PORT = "5432"
SCHEMA = "universidade"


def createConnection():
  mydb = psycopg2.connect(
  host= DBHOST,
  database=DATABASE,
  user=USER,
  password=PASSWORD,
  port = PORT,
  options = f'-c search_path={SCHEMA}'
  )
  return mydb

def menu():
  print("1 - Inclusão")
  print("2 - Deleção")
  print("3 - Consultar")
  print("4 - Alteração")
  print("0 - Sair")

def insertOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Inserir um aluno")
    print("2 - Inserir um professor")
    insertOption = int(input())
    if insertOption == 1:
        insertStudent(mydb)
    else:
        insertProfessor(mydb)

def deleteOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Excluir um aluno")
    print("2 - Excluir um professor")
    insertOption = int(input())
    if insertOption == 1:
        deleteStudent(mydb)
    else:
        deleteProfessor(mydb)

def updateOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Alterar uma disciplina")
    print("2 - Alterar uma faculdade")
    insertOption = int(input())
    if insertOption == 1:
        updateDisciplina(mydb)
    else:
        updateFaculdade(mydb)

def insertStudent(mydb):
    print("Digite os dados do aluno")
    id_aluno = int(input("ID Aluno: "))
    id_faculdade = int(input("ID Faculdade: "))
    nome_aluno = input("Nome Aluno: ")
    cra_aluno = int(input("CRA Aluno: "))
    datanasc_aluno = input("Data Nascimento Aluno: ")
    telefone_aluno = input("Telefone Aluno: ")

    mycursor = mydb.cursor()
    try:
        query = f"insert into Aluno values({id_aluno}, {id_faculdade}, {nome_aluno}, {cra_aluno},{datanasc_aluno}, {telefone_aluno}"

        #res_insert_query ="""insert into Aluno values(%s, %s, %s, %s, %s, %s)"""
        #d_to_insert=(id_aluno, id_faculdade, nome_aluno, cra_aluno, datanasc_aluno, telefone_aluno)
        mycursor.execute(query)
        mydb.commit()
        print("------Aluno inserido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertProfessor(mydb):
    print("Digite os dados do professor")
    id_professor = int(input("ID Professor: "))
    id_faculdade = int(input("ID Faculdade: "))
    nome_prof = input("Nome Professor: ")
    datanasc_prof = input("Data Nascimento Professor: ")
    salario_prof = input("Salario Professor: ")

    mycursor = mydb.cursor()
    try:

        query = f"insert into Professor values ({id_professor}, {id_faculdade}, {nome_prof}, {datanasc_prof}, {salario_prof})"

        #res_insert_query ="""insert into Professor values(%s, %s, %s, %s, %s)"""
        #d_to_insert=(id_professor, id_faculdade, nome_prof, datanasc_prof, salario_prof)
        
        mycursor.execute(query)
        mydb.commit()
        print("------Professor inserido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def deleteStudent(mydb):
    idaluno = int(input("Digite o ID do aluno que deseja excluir: "))
    mycursor = mydb.cursor()
    try:
        query = """Delete from aluno where idaluno = %s"""
        mycursor.execute(query, (idaluno,))
        mydb.commit()
        print("------Aluno removido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def deleteProfessor(mydb):
    idprofessor = int(input("Digite o ID do professor que deseja excluir: "))
    mycursor = mydb.cursor()
    try:
        query = """Delete from professor where idprofessor = %s"""
        mycursor.execute(query, (idprofessor,))
        mydb.commit()
        print("------Professor removido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def consultTable(mydb):
    options = ["Aluno", "Professor", "Disciplinas", "Faculdade"]
    print("Selecione qual tabela deseja consultar:")
    print( "1 - Aluno")
    print( "2 - Professor")
    print( "3 - Disciplinas")
    print( "4 - Faculdade")

    option = int(input())
    table = options[option-1]
    table.format()

    mycursor = mydb.cursor() 
    try:
        query = f"SELECT * FROM {table}"
        mycursor.execute(query)
        for tuple in mycursor.fetchall():
            print(tuple)
        print(f"------Tabela {table} consultada com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateDisciplina(mydb):
    options = ["sigladisciplina", "nome", "creditos", "prerequisito"]
    
    id_update = int(input("Informe o ID da disciplina que deseja alterar:"))

    print("Informe os dados que deseja alterar")
    print("1 - Sigla disciplina")
    print("2 - Nome")
    print("3 - Creditos")
    print("4 - Pre requisito") 
    
    option_update = int(input())

    field_update = options[option_update-1]
    field_update.format()


    new_value = int(input("Informe o novo valor do campo a ser alterado: "))

    mycursor = mydb.cursor()
    try:
        query = f"UPDATE disciplinas SET {field_update} = {new_value} where iddisciplina ={id_update}"

        mycursor.execute(query)
        mydb.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateFaculdade(mydb):
    options = ["idfaculdade", "bloco", "nprofessores", "nalunos", "orcamento"]
    
    id_update = int(input("Informe o ID da faculdade que deseja alterar:"))

    print("Informe os dados que deseja alterar")
    print("1 - idfaculdade")
    print("2 - bloco")
    print("3 - nprofessores")
    print("4 - nalunos")
    print("5 - orcamento") 
    
    option_update = int(input())

    field_update = options[option_update-1]
    field_update.format()


    new_value = int(input("Informe o novo valor do campo a ser alterado: "))

    mycursor = mydb.cursor()
    try:
        query = f"UPDATE faculdade SET {field_update} = {new_value} where idfaculdade ={id_update}"

        mycursor.execute(query)
        mydb.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    
def main():
  mydb = createConnection()
  menu()
  opcao = int(input("Digite a opção: "))

  while(opcao!=0):

      if(opcao ==1):
          insertOption(mydb)         
      if(opcao ==2):
          deleteOption(mydb)
      if(opcao ==3):
          consultTable(mydb)
      if(opcao ==4):
          updateOption(mydb)
      menu()
      opcao = int(input("Digite uma nova opção: "))


  mydb.close()


if __name__ == '__main__':
  main()