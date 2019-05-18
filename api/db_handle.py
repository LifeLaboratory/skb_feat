import sqlite3
import hashlib

general_db_file_location = "database_files/general.db"


def db_cmp_passwd(login, passwd):
    _conn = sqlite3.connect(general_db_file_location)
    _c = _conn.cursor()

    hash = _c.execute("select passwd from users where login = " + login + ";").fetchone()
    result = hash[0][0] == hashlib.sha256(passwd.encode()).hexdigest()
    _conn.close()

    return result


def db_check_user(login, passwd):
    _conn = sqlite3.connect(general_db_file_location)
    _c = _conn.cursor()

    hash = _c.execute("select count(*) from users where login = " + login + ";").fetchall()
    result = hash[0][0] == hashlib.sha256(passwd.encode()).hexdigest()
    _conn.close()

    return result


def db_add_user(login, passwd, firstname, secondname, bday, hobby, sex, social_link):
    _conn = sqlite3.connect(general_db_file_location)
    _c = _conn.cursor()

    _c.execute("insert into users values(?, ?, ?, ?, ?, ?, ?, ?  ?)",
               (None, login, hashlib.sha256(passwd.encode()).hexdigest(), firstname, secondname, bday, hobby, sex, social_link))

    _conn.commit()
    _conn.close()


def db_delete_user(login):
    _conn = sqlite3.connect(general_db_file_location)
    _c = _conn.cursor()

    _c.execute("delete from users where login =  '" + login + "'; ")

    _conn.commit()
    _conn.close()

#print(verify("roma_lox", "degenerat"))

#print(hashlib.sha256("degenerat".encode()).hexdigest())