import sqlite3
import bcrypt

DB = "data/users.db"


# Hash Password
def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
    return hashed.decode('utf-8')


# Verify Password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )


# Register User
def register_user(name, email, password, branch, year):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        hashed_password = hash_password(password)

        cursor.execute("""
        INSERT INTO users
        (name,email,password,branch,year)
        VALUES(?,?,?,?,?)
        """,
        (
            name,
            email,
            hashed_password,
            branch,
            year
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


# Login User
def login_user(email, password):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE email=?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return None

    # user tuple
    # id, name, email, password, branch, year
    stored_password = user[3]

    if verify_password(password, stored_password):
        return user

    return None