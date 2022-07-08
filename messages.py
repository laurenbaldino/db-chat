from src.swen344_db_utils import *
import datetime

def build_messages():
    """Buid the messages table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS messages CASCADE
    """
    sql = """
        CREATE TABLE messages(
            message_id SERIAL PRIMARY KEY,
            sender_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
            reciever_id INTEGER REFERENCES users(user_ID) ON DELETE CASCADE,
            message VARCHAR NOT NULL,
            sent_on DATE,
            is_read BOOLEAN
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)

def get_messages(sender_id, reciever_id):
    """
    -Gather all messages between 2 users
    -sender_id = id number associated with message sender
    -reciever_id = id number associated with message reciever
    -Returns an array of all messages

     """
    sql = 'SELECT * FROM messages WHERE sender_id = (%s) AND reciever_id = (%s)'
    result = exec_get_all(sql, (sender_id, reciever_id))
    return result


def get_messages_range(sender_id, reciever_id, sent_on):
    """
    -Gather all messages during a time frame
    -sender_id = id number associated with message sender
    -reciever_id = id number associated with message reciever
    -sent_on = date to determine range
    -Returns an array of all messages
    """
    sql = 'SELECT * FROM messages WHERE sender_id = (%s) AND reciever_id = (%s) and sent_on >= (%s)'
    result = exec_get_all(sql, (sender_id, reciever_id, sent_on))
    return result

def get_unread_count_dm(reciever_id):
    """
    -Gather the number of unread messages of a user
    -reciever_id = id number associated with message reciever
    -Returns a count of the number of messages
    """
    sql = 'SELECT COUNT(message) FROM messages WHERE reciever_id = (%s) AND is_read = FALSE'
    result = exec_get_one(sql, (reciever_id,))
    return result

def get_unread_count_channels(user_id, community_id):
    """
    -Gather the number of unread messages of a user in a channel
    -user_id = id number associated with message reciever
    -community_id= id number associated with community associated with channel
    -Returns a count of the number of messages
    """
    check = 'SELECT EXISTS(SELECT FROM users_to_communities WHERE user_id = (%s) AND community_id = (%s)'
    result = exec_get_one(check, (user_id, community_id))
    if result == True:
        sql = 'SELECT COUNT(message) FROM channel_messages WHERE is_read = FALSE'
        res = exec_get_one(sql)
    return res

def get_message_count(sender_id, reciever_id):
    """
    -Gather number of messages in total between 2 users
    -sender_id= id associated with message sender
    -reciever_id = id assoicatied with message reciever
    -returns a count of the number of messages
    """
    sql= 'SELECT COUNT (message) FROM messages WHERE sender_id = (%s) AND reciever_id = (%s)'
    result = exec_get_one(sql, (sender_id, reciever_id))
    return result

def create_new_message(sender_id, reciever_id, message, sent_on):
    """
    -create a new message between users
    -sender_id = id number associated with sender
    -reciever_id = id number associated with reciever
    -message = new message
    -sent_on = date associated with message
    """
    sql = 'INSERT INTO messages(sender_id, reciever_id, message,sent_on, is_read) VALUES (%s, %s, %s, %s, FALSE)'
    result = exec_commit(sql ,(sender_id, reciever_id, message, sent_on))
    return result

def create_channel_message(sender_id, channel_id, message, sent_on):
    
    """
    -create a new message in a channel
    -sender_id = id number associated with sender
    -channel_id = id number associated with the channel
    -message = new message
    -sent_on = date associated with message
    """
    sql = 'INSERT INTO channel_messages(sender_id, channel_id, message, sent_on, is_read) VALUES (%s, %s, %s, %s, FALSE)'
    result = exec_get_all(sql, (sender_id, channel_id, message, sent_on))
    return result

def mark_read(sender_id, reciever_id, message):
    """
    -change message status to read
    -sender_id = id number associated with sender
    -reciever_id = id number associated with reciever
    -message = message associated with sender and reciever
    """
    sql = 'UPDATE messages SET is_read = TRUE WHERE sender_id = (%s) AND reciever_id = (%s) AND message = (%s)'
    result = exec_commit(sql, (sender_id, reciever_id, message))
    return result

def get_stemmed_words(words):
    """
    -words= string of words input by user
    -return all instances of stemmed words
    """
    words = words.replace(' ', ' & ')
    print(words)
    sql = 'SELECT * FROM messages WHERE to_tsvector(message) @@ to_tsquery(%s)'
    result = exec_get_all(sql, words)
    return result

# def get_average_day_count(community_id, cur_date, past_date):
#     """
#     -community_id= community id associated with community
#     -cur_date= current date inputted by user
#     -past_date= 30 days prior to inputted date
#     -returns average number of messages per day within criteria
#     """
#     past_date = past_date - date.timedelta(30)
#     sql = 'SELECT avg(count) FROM (SELECT COUNT(*), date_trunc('day', sent_on) FROM channels INNER JOIN channel_messages ON channel_messages.channel_id = channels.channel_id WHERE channels.community_id = (%s) AND char_length(message) > 5 AND channel_messages.sent_on > (%s) AND channel_messages.sent_on < (%s) GROUP BY date_trunc('day', sent_on)) AS avg_count'
#     result = exec_get_one(sql, (community_id, cur_date, past_date))
#     return result

