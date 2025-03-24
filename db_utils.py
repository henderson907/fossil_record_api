import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    print(HOST)
    return cnx


def get_all_fossils_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        query = """SELECT * FROM fossil ORDER BY discovered_on ASC;"""
        cur.execute(query)
        result = cur.fetchall()

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()


def add_new_fossil_db(new_fossil_dictionary):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        query = "INSERT INTO fossil (species, country, discovered_on, discovered_by, fossil_type, complete, period) VALUE (%s, %s, %s, %s, %s, %s, %s)"

        # Execute the query
        cur.execute(query, (
        new_fossil_dictionary['species'], new_fossil_dictionary['country'], new_fossil_dictionary['discovered_on'],
        new_fossil_dictionary['discovered_by'], new_fossil_dictionary['fossil_type'], new_fossil_dictionary['complete'],
        new_fossil_dictionary['period']))

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        query = """SELECT * FROM fossil"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()


def find_fossil_by_country_db(country):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        query = "SELECT * FROM fossil WHERE country = %s ORDER BY discovered_on ASC;"

        cur.execute(query, (country,))

        result = cur.fetchall()
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()


if __name__ == "__main__":
    pass