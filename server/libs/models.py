def get_user(db_connection, user_username):
    req = """SELECT * FROM user WHERE user_username=?"""
    cursor = db_connection.cursor()
    cursor.execute(req, (user_username, ))
    rows = cursor.fetchall()
    if not rows:
        return None
    return rows[0]


def create_user(db_connection, user_username):
    req = """INSERT INTO user (user_username) VALUES (?)"""
    cursor = db_connection.cursor()
    cursor.execute(req, (user_username, ))
    db_connection.commit()
    return cursor.lastrowid


def get_messages_from_user(db_connection, user_id):
    req = """SELECT * FROM message WHERE message_sender=?"""
    cursor = db_connection.cursor()
    cursor.execute(req, (user_id, ))
    return cursor.fetchall()


def get_messages_for_user(db_connection, user_id, software):
    req = """SELECT * FROM message
    INNER JOIN user ON message.message_sender=user.user_id
    WHERE message_receiver=? AND message_software=?
    ORDER BY message_timestamp DESC, message_readed ASC LIMIT 10"""
    cursor = db_connection.cursor()
    cursor.execute(req, (user_id, software))
    return cursor.fetchall()


def get_all_users(db_connection):
    req = """SELECT * FROM user"""
    cursor = db_connection.cursor()
    cursor.execute(req)
    return cursor.fetchall()


def create_message(db_connection, sender, receiver,
                   content, attachment, software, timestamp):
    req =  """INSERT INTO message (message_sender, message_receiver,
    message_content, message_attachment, message_software, message_timestamp)
    VALUES (?, ?, ?, ?, ?, ?)"""
    params = (sender, receiver, content, attachment, software, timestamp)
    cursor = db_connection.cursor()
    cursor.execute(req, params)
    db_connection.commit()
    return cursor.lastrowid


def update_message_read(db_connection, message_id):
    req = """UPDATE message SET message_readed=1 WHERE message_id=?"""
    cursor = db_connection.cursor()
    cursor.execute(req, (message_id, ))
    db_connection.commit()


def delete_message(db_connection, message_id):
    req = """DELETE FROM message WHERE message_id IS ?"""
    cursor = db_connection.cursor()
    cursor.execute(req, (message_id, ))
    db_connection.commit()