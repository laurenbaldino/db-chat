from src.swen344_db_utils import *
import datetime


def build_users():
    """Build the users table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS users CASCADE
    """
    sql = """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            email VARCHAR UNIQUE NOT NULL,
            username VARCHAR UNIQUE NOT NULL,
            created_on DATE,   
            changed_on DATE,
            change_end DATE    
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)


def build_suspended_users():
    """Build the suspended users table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS suspended_users
    """
    sql = """
        CREATE TABLE suspended_users(
            user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
            community_id INTEGER REFERENCES communities(community_id) ON DELETE CASCADE,
            suspension_end DATE
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)


def suspend_users(user_id, community_id, suspension_end):
    """
    -add user to the suspended table
    -user_id= id associated with user
    -community_id= id associated with community
    -suspension_end= date suspension is over
    """
    sql = 'INSERT INTO suspended_users(user_id, community_id, suspension_end) VALUES (%s, %s, %s)'
    result = exec_commit(sql, (user_id, community_id, suspension_end))
    return result


def create_new_user(email, username, created_on):
    """
    -create a new user into users table
    -email: email associated with user
    -username: unique username
    -created_on: current date
    """
    sql = 'INSERT INTO users (email, username, created_on, changed_on, change_end) VALUES (%s, %s, %s, NULL, NULL)'
    result = exec_commit(sql, (email, username, created_on))
    return result


def list_users(reciever_id, user_id):
    """
    -list all users the reciever has gotten messages from and unread count
    -reciever_id = id number associated with reciever
    -user_id = id associated with user in users table
    -returns array of all senders and count of unread messages
    """
    sql = 'SELECT sender_id FROM messages WHERE reciever_id = (%s)'
    result = exec_get_all(sql, reciever_id)
    count = getUnreadCount(user_id)
    return result
    return count


def change_username(username, user_id, change_end):
    """
    -update users username as long as it has been past the 6th month change rule
    -user_id = id associated with username
    -username = current username of choice
    -changed_end = day change suspension is lifted
    """
    sql = 'UPDATE users SET username=(%s) WHERE user_id = (%s) AND change_end > (%s)'
    result = exec_commit(sql, (username, user_id, change_end))
    return result


def get_suspension(user_id, community_id):
    """
    -Check if user is suspended from community
    -User_id = id number associated with user
    -community_id= id number associated with a community
    -Returns boolean value of suspension status
    """
    sql = 'SELECT EXISTS(SELECT FROM suspended_users WHERE user_id = (%s) AND community_id = (%s)'
    result = exec_get_one(sql, (user_id, community_id))
    return result


def change_suspension(user_id, community_id, suspension_end):
    """
    -change suspension end date
    -username = username associated with user
    -suspension_end = date in which suspension is over
    """
    sql = 'UPDATE suspended_users SET suspension_end= (%s) WHERE user_id = (%s) AND community_id = (%s)'
    result = exec_commit(sql, (user_id, community_id, suspension_end))
    return result


def remove_suspension(user_id, community_id, suspension_end):
    """
    -change suspension end date
    -username = username associated with user
    -suspension_end = date in which suspension is over
    """
    sql = 'UPDATE users SET suspension_end=NULL WHERE user_id = (%s) AND community_id = (%s)'
    result = exec_commit(sql, (user_id, community_id, suspension_end))
    return result


def get_user_metrics(cur_date, past_date):
    """
    -cur_date= current date inputted by user
    -past_date= 30 days prior to inputted date
    -returns number of different users within criteria
    """
    past_date = past_date - date.timedelta(30)
    sql = 'select count(distinct sender_id) from channel_messages where char_length(message) > 5 and channel_messages.sent_on > (%s) and channel_messages.sent_on < (%s)'
    result = exec_get_one(sql, (cur_date, past_date))
    return result

def get_suspended_users(cur_date, past_date):
    sql = 'select distinct username from users inner join messages on messages.sender_id = users.user_id inner join suspended_users on suspended_users.user_id = users.user_id where messages.sent_on > (%s) and messages.sent_on < (%s)'
    result = exec_get_one(sql, (cur_date, past_date))
    return result
