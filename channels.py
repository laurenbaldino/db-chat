from src.swen344_db_utils import *


def build_channels():
    """Build the channels table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS channels CASCADE
    """
    sql = """
        CREATE TABLE channels(
            channel_id SERIAL PRIMARY KEY,
            name VARCHAR UNIQUE NOT NULL,
            community_id INTEGER REFERENCES communities(community_ID) ON DELETE CASCADE
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)


def build_channel_messages():
    """Buid the channel messages table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS channel_messages
    """
    sql = """
        CREATE TABLE channel_messages(
            message_id SERIAL PRIMARY KEY,
            sender_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
            channel_id INTEGER REFERENCES channels(channel_ID) ON DELETE CASCADE,
            message VARCHAR NOT NULL,
            sent_on DATE,
            is_read BOOLEAN
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)


def create_new_channel(name, community_id):
    """
    -create a new channel within a community
    -name = name of channel
    -community_id = id of community the channel is within
    """
    sql = 'INSERT INTO channels(name, community_id) VALUES (%s, %s)'
    result = exec_commit(sql, (name, communnity_id))
    return result


def insert_channel_message(sender_id, channel_id, message, sent_on, is_read):
    """
    -add a message into a channel
    -sender_id= id associated with message sender
    -channel_id= id associated with recieving channel
    -sent_on= date message is sent on
    -is_read = boolean if message has been read by user of choice
    """
    sql = 'INSERT INTO channel_messages(sender_id, channel_id, message, sent_on, is_read) VALUES (%s, %s, %s, %s, NULL)'
    result = exec_commit(sql, (sender_id, channel_id, message, sent_on))
    return result


def get_mentions(username):
    """
    -get all mentions from all communities
    -username= username of mentioned user
    """
    sql = 'SELECT * FROM users_to_communities INNER JOIN channels ON channels.community_id = users_to_communities.community_id INNER JOIN channel_messages ON channel_messages.channel_id = channels.channel_id INNER JOIN users ON users.user_id = users_to_communities.user_id WHERE message LIKE '%' || users.username || '%' AND username = (%s)'
    result = exec_get_all(sql, (username))
    return result