# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="trial1",
    password="manofsteel"
)
c = mydb.cursor()

'''
def create_tables():
    c.execute('CREATE TABLE TEAM(team_name VARCHAR(50) PRIMARY KEY, city VARCHAR(20), wins INT, losses INT, draws INT, team_rank INT, '
    'home_stadium_id INT, rival_team_name VARCHAR(50), FOREIGN KEY(home_stadium_id) REFERENCES STADIUM(stadium_id), '
    'FOREIGN KEY(rival_team_name) REFERENCES TEAM(team_name));')
'''

def add_team(team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name):
    c.execute('INSERT INTO TEAM(team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name))
    mydb.commit()


def view_all_team():
    c.execute('SELECT * FROM TEAM')
    data = c.fetchall()
    return data


def view_only_team_names():
    c.execute('SELECT team_name FROM TEAM')
    data = c.fetchall()
    return data


def get_team(team_name):
    c.execute('SELECT * FROM TEAM WHERE team_name="{}"'.format(team_name))
    data = c.fetchall()
    return data


def edit_team_data(new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name):
    c.execute("UPDATE TEAM SET team_name=%s, city=%s, wins=%s, losses=%s, draws=%s, team_rank=%s, home_stadium_id=%s, rival_team_name=%s WHERE "
              "team_name=%s and city=%s and wins=%s and losses=%s and draws=%s and team_rank=%s and home_stadium_id=%s and rival_team_name=%s", (new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_team(team_name):
    c.execute('DELETE FROM TEAM WHERE team_name="{}"'.format(team_name))
    mydb.commit()
