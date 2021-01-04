# Exercitiul III
# Realizati o agenda telefónica in Python. In fiecare intrare se vor salva date ale contactelor, cum ar fi nume, prenume,
# companie, adresa de email. Agenda trebuie sa contina o functie de cautare, si sa se poata folosi din line de comanda.
import os
import time
import sqlite3


fisier_db = 'agenda.db'
lista_contact = ['nume', 'prenume', 'companie', 'email', 'telefon']
sql_agenda_table = """ CREATE TABLE IF NOT EXISTS agenda (
                                                                contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                nume VARCHAR(30),
                                                                prenume VARCHAR(30),
                                                                companie VARCHAR(30),
                                                                email VARCHAR(30),
                                                                telefon INTEGER); """


# sql_agenda_table = """ CREATE TABLE IF NOT EXISTS agenda (
#                                                                 contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                                                 nume VARCHAR(30),
#                                                                 prenume VARCHAR(30),
#                                                                 companie VARCHAR(30),
#                                                                 email VARCHAR(30),
#                                                                 telefon INTEGER); """


def create_db(db_name, sql_table):
    '''se crează baza de date dacă nu există'''
    my_connection = sqlite3.connect(db_name)
    my_connection.execute(sql_table)
    my_connection.commit()
    my_connection.close()


def write_to_db(db_name, contact):
    '''add values to db'''
    print('Se scrie în baza de date:')
    time.sleep(0.5)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO agenda (nume,prenume,companie,email,telefon) values(?,?,?,?,?)", contact)
    time.sleep(0.5)
    connection.commit()
    connection.close()


def add_to_db(contact, sql_table, db_name=fisier_db):
    '''se adaugă în baza de date'''
    print(db_name)
    if os.path.exists(db_name):
        print('Baza de date există!')
        time.sleep(0.5)
        write_to_db(db_name, contact)
    else:
        print('Se crează baza de date!')
        time.sleep(0.5)
        create_db(db_name,sql_table)
        write_to_db(db_name, contact)


def delete_entry(id, db_name=fisier_db):
    '''se va șterge un contact după ID'''
    print(f'Se va șterge din agendă ID: {id}')
    time.sleep(0.5)
    my_connection = sqlite3.connect(db_name)
    my_cursor = my_connection.cursor()
    my_cursor.execute(f'''DELETE FROM agenda WHERE rowid="{id}";''')
    time.sleep(0.5)
    my_connection.commit()
    my_connection.close()


def query_entry(name, db_name=fisier_db):
    '''cautare contact'''
    print('Se caută în agendă:')
    time.sleep(0.5)
    my_connection = sqlite3.connect(db_name)
    my_cursor = my_connection.cursor()
    my_cursor.execute(f'''SELECT * FROM agenda WHERE nume="{name}";''')
    rows = my_cursor.fetchall()
    for row in rows:
        print(row)
    my_connection.close()


def read_from_db():
    '''se citește din baza de date'''
    pass

def delete_from_db():
    '''se șterge din baza de date'''
    pass

def add_entry():
    '''se va adăga datele unui nou contact: nume, prenume, companie, adresa de mail'''
    pass


def create_contact(lista=lista_contact):
    '''se generează meniul pentru introducerea datelor persoanei de contact'''
    contact = []
    for i in range(len(lista)):
        c = input(lista[i] + ': ')
        if i < 3:
            contact.append(c.capitalize())
        else:
            contact.append(c)
    add_to_db(contact, sql_table=sql_agenda_table)

def meniu():
    '''meniul agendei'''
    print('''
    ^Agenda telefonică^
    
    1. Adaugă un contact nou:
    2. Caută contact existent folosind: Numele
    3. Sterge un contact din agendă folosind: Numele
    
    Pentru a opri programul folosiți litera e
    ''')

    a = input('selectați opțiunea: ')
    if a == 'e':
        exit(0)
    elif a == '1':
        create_contact()
    elif a == '2':
        name = input('Ce nume căutați?:')
        query_entry(name)
    elif a == '3':
        name = input('Ce nume doriți să ștergeți?:')
        query_entry(name)
        id = input('Ce id doriți să ștergeți?:')
        delete_entry(id)

    return a



while True:
    meniu()