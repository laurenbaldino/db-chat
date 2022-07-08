from src.swen344_db_utils import *

def build_communities():
    """Build the communities table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS communities CASCADE
    """
    sql = """
        CREATE TABLE communities(
            community_id SERIAL PRIMARY KEY,
            name VARCHAR UNIQUE NOT NULL
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)

def create_new_community(name):
    """
    -create a new community
    -name = name of community
    """
    sql = 'INSERT INTO communities(name) values (%s)'
    result = exec_commit(sql, (name))
    return result
    
def build_users_to_communities():
    """Build the users_to_communities table and create schema """
    drop_sql = """
        DROP TABLE IF EXISTS users_to_communities
    """
    sql = """
        CREATE TABLE users_to_communities(
            user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
            community_id INTEGER REFERENCES communities(community_id) ON DELETE CASCADE
        )
    """
    exec_commit(drop_sql)
    exec_commit(sql)

def join_community(user_id, community_id):
    """
    -add a user to a community
    -user_id= id associated with user
    -community_id= id associated with community
    """
    sql = 'INSERT INTO users_to_communities(user_id, community_id) VALUES (%s, %s)'
    result = exec_commit(sql, (user_id, community_id))
    return result

def leave_community(user_id, community_id):
    """
    -remove a user from a community
    -user_id= id associated with user
    -community_id= id associated with community
    """
    sql = 'DELETE FROM users_to_communities(user_id, community_id) WHERE user_id = (%s) AND community_id = (%s)'
    result = exec_commit(sql, (user_id, community_id))
    return result
