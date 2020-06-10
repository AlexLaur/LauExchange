def get_user(db_connection, user_username):
    req = 'SELECT * FROM user WHERE user_username = "%s"' % user_username
    cursor = db_connection.cursor()
    cursor.execute(req)
    rows = cursor.fetchall()
    if not rows:
        return None
    return rows[0]


def create_user(db_connection, user_username):
    req = 'INSERT INTO user (user_username) VALUES ("%s")' % user_username
    cursor = db_connection.cursor()
    cursor.execute(req)
    db_connection.commit()
    return cursor.lastrowid


def get_messages_from_user(db_connection, user_id):
    req = 'SELECT * FROM message WHERE message_sender = "%s"' % user_id
    cursor = db_connection.cursor()
    cursor.execute(req)
    return cursor.fetchall()


def get_messages_for_user(db_connection, user_id):
    req = 'SELECT * FROM message WHERE message_receiver = "%s"' % user_id
    cursor = db_connection.cursor()
    cursor.execute(req)
    return cursor.fetchall()
