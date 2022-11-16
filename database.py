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

    create player table with 10 columns extra is age which can be derived
'''

def add_team(team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name):
    c.execute('INSERT INTO TEAM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name))
    mydb.commit()



def add_player(player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name):
    c.execute('INSERT INTO PLAYER(player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name))
    c.execute('UPDATE PLAYER SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE player_name="{}"'.format(player_name))
    #Umesh Yadav 9 19 1987-10-25 52 2014-06-13 75 Royal Challengers Bangalore
    mydb.commit()

def view_all_team():
    c.execute('SELECT * FROM TEAM')
    data = c.fetchall()
    return data

def view_all_player():
    c.execute('SELECT * FROM PLAYER')
    data = c.fetchall()
    return data


def view_only_team_names():
    c.execute('SELECT team_name FROM TEAM')
    data = c.fetchall()
    return data

def view_only_player_names():
    c.execute('SELECT player_name FROM PLAYER')
    data = c.fetchall()
    return data


def get_team(team_name):
    c.execute('SELECT * FROM TEAM WHERE team_name="{}"'.format(team_name))
    data = c.fetchall()
    return data

def get_player(player_name):
    c.execute('SELECT * FROM PLAYER WHERE player_name="{}"'.format(player_name))
    data = c.fetchall()
    return data


def edit_team_data(new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name):
    c.execute("UPDATE TEAM SET team_name=%s, city=%s, wins=%s, losses=%s, draws=%s, team_rank=%s, home_stadium_id=%s, rival_team_name=%s WHERE "
              "team_name=%s and city=%s and wins=%s and losses=%s and draws=%s and team_rank=%s and home_stadium_id=%s and rival_team_name=%s", (new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_player_data(new_player_name,new_jersey_no,new_test,new_odi,new_t20,new_dob,new_debut,new_keeper,new_team_name,player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name):
    c.execute("UPDATE PLAYER SET player_name=%s, jersey_no=%s, test=%s, odi=%s, t20=%s, dob=%s, debut=%s, keeper=%s, team_name=%s WHERE "
              "player_name=%s and jersey_no=%s and test=%s and odi=%s and t20=%s and dob=%s and debut=%s and keeper=%s and team_name=%s", (new_player_name,new_jersey_no,new_test,new_odi,new_t20,new_dob,new_debut,new_keeper,new_team_name,player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name))
    c.execute('UPDATE PLAYER SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE player_name="{}"'.format(player_name))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_team(team_name):
    c.execute('DELETE FROM TEAM WHERE team_name="{}"'.format(team_name))
    mydb.commit()

def delete_player(player_name):
    c.execute('DELETE FROM PLAYER WHERE player_name="{}"'.format(player_name))
    mydb.commit()