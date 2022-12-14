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

    create table for stadium
'''
#def get_info(tablename)
def custom_query(query):
    c.execute(query)
    data = c.fetchall()
    return data

def left_outer_join(left,right,common):
    c.execute('SELECT * FROM {} LEFT JOIN {} ON {}.{}={}.{}'.format(left,right,left,common,right,common))
    data = c.fetchall()
    return data

def right_outer_join(left,right,common):
    c.execute('SELECT * FROM {} RIGHT JOIN {} ON {}.{}={}.{}'.format(left,right,left,common,right,common))
    data = c.fetchall()
    return data

def full_outer_join(left,right,common):
    c.execute('SELECT * FROM {} FULL OUTER JOIN {} ON {}.{}={}.{}'.format(left,right,left,common,right,common))
    data = c.fetchall()
    return data

def inner_join(left,right,common):
    c.execute('SELECT * FROM {} INNER JOIN {} ON {}.{}={}.{}'.format(left,right,left,common,right,common))
    data = c.fetchall()
    return data


def add_team(team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name):
    c.execute('INSERT INTO TEAM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name))
    mydb.commit()

def add_color(team_name,color):
    c.execute('INSERT INTO COLORS VALUES (%s,%s)',
              (team_name,color))
    mydb.commit()

def remove_color(team_name,color):
    c.execute('DELETE FROM COLORS WHERE team_name=%s and color=%s',(team_name,color))
    mydb.commit()

def add_player(player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name):
    c.execute('INSERT INTO PLAYER(player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name))
    c.execute('UPDATE PLAYER SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE player_name="{}"'.format(player_name))
    #Umesh Yadav 9 19 1987-10-25 52 2014-06-13 75 Royal Challengers Bangalore
    mydb.commit()

def add_batsman(jersey_no,sixes,runs,average,fifties,fours,hundreds):
    c.execute('INSERT INTO BATSMAN VALUES (%s,%s,%s,%s,%s,%s,%s)',
              (jersey_no,sixes,runs,average,fifties,fours,hundreds))
    mydb.commit()

def add_bowler(jersey_no,economy,wickets,average,runs,balls_bowled):
    c.execute('INSERT INTO BOWLER VALUES (%s,%s,%s,%s,%s,%s)',
              (jersey_no,economy,wickets,average,runs,balls_bowled))
    mydb.commit()

def add_stadium(stadium_name,stadium_id,capacity,city,address):
    c.execute('INSERT INTO STADIUM VALUES (%s,%s,%s,%s,%s)',
              (stadium_name,stadium_id,capacity,city,address))
    mydb.commit()

def add_match(match_no,toss,result,match_date,man_of_match,stadium_id):
    c.execute('INSERT INTO MATCHES VALUES (%s,%s,%s,%s,%s,%s)',
              (match_no,toss,result,match_date,man_of_match,stadium_id))
    mydb.commit()

def add_team_match(match_no,team_name):
    c.execute('INSERT INTO TEAM_MATCH VALUES (%s,%s)',
              (team_name,match_no))
    mydb.commit()

def add_coach(coach_name,coach_id,dob,country_origin,team_name):
    c.execute('INSERT INTO COACH(coach_name,coach_id,dob,country_origin,team_name) VALUES (%s,%s,%s,%s,%s)',
              (coach_name,coach_id,dob,country_origin,team_name))
    c.execute('UPDATE COACH SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE coach_name="{}"'.format(coach_name))
    mydb.commit()

def add_umpire(umpire_name,umpire_id,no_of_matches,dob,country_origin):
    c.execute('INSERT INTO UMPIRE(umpire_name,umpire_id,no_of_matches,dob,country_origin) VALUES (%s,%s,%s,%s,%s)',
              (umpire_name,umpire_id,no_of_matches,dob,country_origin))
    c.execute('UPDATE UMPIRE SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE umpire_name="{}"'.format(umpire_name))
    mydb.commit()

def add_match_umpire(match_no,umpire_id):
    c.execute('INSERT INTO MATCH_UMPIRE(match_no,umpire_id) VALUES (%s,%s)',
              (match_no,umpire_id))
    mydb.commit()



def view_all_team():
    c.execute('SELECT *,team_colors(team_name),get_captain(team_name),2*get_cummulative_team(team_name) as points FROM TEAM order by points desc;')
    data = c.fetchall()
    return data

def view_all_player():
    c.execute('SELECT * FROM PLAYER')
    data = c.fetchall()
    return data

def view_all_stadium():
    c.execute('SELECT * FROM STADIUM')
    data = c.fetchall()
    return data

def view_all_match():
    c.execute('SELECT match_no,get_first_team_for_match(match_no),get_second_team_for_match(match_no),toss,result,match_date,man_of_match,get_first_umpire(match_no),stadium_id FROM MATCHES')
    data = c.fetchall()
    return data

def view_all_coach():
    c.execute('SELECT * FROM COACH')
    data = c.fetchall()
    return data

def view_all_umpire():
    c.execute('SELECT * FROM UMPIRE')
    data = c.fetchall()
    return data

def view_all_batsman():
    c.execute('SELECT jersey_no,player_name,sixes,runs,average,fifties,fours,hundreds FROM PLAYER NATURAL JOIN BATSMAN')
    data = c.fetchall()
    return data

def view_all_bowler():
    c.execute('SELECT jersey_no,player_name,economy,wickets,average,runs,balls_bowled FROM PLAYER NATURAL JOIN BOWLER')
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

def view_only_batsman_names():
    c.execute('SELECT player_name FROM BATSMAN NATURAL JOIN PLAYER')
    data = c.fetchall()
    return data

def view_only_bowler_names():
    c.execute('SELECT player_name FROM BOWLER NATURAL JOIN PLAYER')
    data = c.fetchall()
    return data

def view_only_stadium_names():
    c.execute('SELECT stadium_name FROM STADIUM')
    data = c.fetchall()
    return data

def view_only_match_number():
    c.execute('SELECT match_no FROM MATCHES')
    data = c.fetchall()
    return data

def view_only_coach_names():
    c.execute('SELECT coach_name FROM COACH')
    data = c.fetchall()
    return data

def view_only_umpire_names():
    c.execute('SELECT umpire_name FROM UMPIRE')
    data = c.fetchall()
    return data




def get_team(team_name):
    c.execute('SELECT *,team_colors(team_name),get_captain(team_name) FROM TEAM WHERE team_name="{}"'.format(team_name))
    data = c.fetchall()
    return data

def get_player(player_name):
    c.execute('SELECT * FROM PLAYER WHERE player_name="{}"'.format(player_name))
    data = c.fetchall()
    return data

def get_batsman(player_name):
    c.execute('SELECT jersey_no,player_name,sixes,runs,average,fifties,fours,hundreds FROM PLAYER NATURAL JOIN BATSMAN WHERE player_name="{}"'.format(player_name))
    data = c.fetchall()
    return data

def get_bowler(player_name):
    c.execute('SELECT jersey_no,player_name,economy,wickets,average,runs,balls_bowled FROM PLAYER NATURAL JOIN BOWLER WHERE player_name="{}"'.format(player_name))
    data = c.fetchall()
    return data

def get_stadium(stadium_name):
    c.execute('SELECT * FROM STADIUM WHERE stadium_name="{}"'.format(stadium_name))
    data = c.fetchall()
    return data

def get_match(match_no):
    c.execute('SELECT match_no,get_first_team_for_match(match_no),get_second_team_for_match(match_no),toss,result,match_date,man_of_match,stadium_id FROM MATCHES WHERE match_no={}'.format(match_no))
    data = c.fetchall()
    return data

def get_coach(coach_name):
    c.execute('SELECT * FROM COACH WHERE coach_name="{}"'.format(coach_name))
    data = c.fetchall()
    return data

def get_umpire(umpire_name):
    c.execute('SELECT * FROM UMPIRE WHERE umpire_name="{}"'.format(umpire_name))
    data = c.fetchall()
    return data


def edit_team_data(new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name):
    c.execute("UPDATE TEAM SET team_name=%s, city=%s, wins=%s, losses=%s, draws=%s, team_rank=%s, home_stadium_id=%s, rival_team_name=%s WHERE "
              "team_name=%s", (new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_player_data(new_player_name,new_jersey_no,new_test,new_odi,new_t20,new_dob,new_debut,new_keeper,new_team_name,player_name):
    c.execute("UPDATE PLAYER SET player_name=%s, jersey_no=%s, test=%s, odi=%s, t20=%s, dob=%s, debut=%s, keeper=%s, team_name=%s WHERE "
              "player_name=%s", (new_player_name,new_jersey_no,new_test,new_odi,new_t20,new_dob,new_debut,new_keeper,new_team_name,player_name))
    c.execute('UPDATE PLAYER SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE player_name="{}"'.format(player_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_stadium_data(new_stadium_name,new_stadium_id,new_capacity,new_city,new_address,stadium_name):
    c.execute("UPDATE STADIUM SET stadium_name=%s, stadium_id=%s, capacity=%s, city=%s, address=%s WHERE "
              "stadium_name=%s", (new_stadium_name,new_stadium_id,new_capacity,new_city,new_address,stadium_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_match_data(new_match_no,new_toss,new_result,new_match_date,new_man_of_match,new_stadium_id,match_no):
    c.execute("UPDATE MATCHES SET match_no=%s, toss=%s, result=%s, match_date=%s, man_of_match=%s, stadium_id=%s WHERE "
              "match_no=%s", (new_match_no,new_toss,new_result,new_match_date,new_man_of_match,new_stadium_id,match_no))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_team_match_data(new_team_name,new_match_no,team_name,match_no):
    c.execute("UPDATE TEAM_MATCH SET team_name=%s, match_no=%s WHERE team_name=%s AND match_no=%s"
              ,(new_team_name,new_match_no,team_name,match_no))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_match_umpire_data(new_match_no,new_umpire_id,match_no,umpire_id):
    c.execute("UPDATE MATCH_UMPIRE SET match_no=%s, umpire_id=%s WHERE match_no=%s AND umpire_id=%s"
              ,(new_match_no,new_umpire_id,match_no,umpire_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_coach_data(new_coach_name,new_coach_id,new_dob,new_country_origin,new_team_name,coach_name):
    c.execute("UPDATE COACH SET coach_name=%s, coach_id=%s, dob=%s, country_origin=%s, team_name=%s WHERE "
              "coach_name=%s", (new_coach_name,new_coach_id,new_dob,new_country_origin,new_team_name,coach_name))
    c.execute('UPDATE COACH SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE coach_name="{}"'.format(coach_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_umpire_data(new_umpire_name,new_umpire_id,new_no_of_matches,new_dob,new_country_origin,umpire_name):
    c.execute("UPDATE UMPIRE SET umpire_name=%s, umpire_id=%s, no_of_matches=%s, dob=%s, country_origin=%s WHERE "
              "umpire_name=%s", (new_umpire_name,new_umpire_id,new_no_of_matches,new_dob,new_country_origin,umpire_name))
    c.execute('UPDATE UMPIRE SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE()) WHERE umpire_name="{}"'.format(umpire_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_batsman_data(new_jersey_no,new_sixes,new_runs,new_average,new_fifties,new_fours,new_hundreds,jersey_no):
    c.execute("UPDATE BATSMAN SET jersey_no=%s, sixes=%s, runs=%s, average=%s, fifties=%s, fours=%s, hundreds=%s WHERE "
              "jersey_no=%s", (new_jersey_no,new_sixes,new_runs,new_average,new_fifties,new_fours,new_hundreds,jersey_no))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_bowler_data(new_jersey_no,new_economy,new_wickets,new_average,new_runs,new_balls_bowled,jersey_no):
    c.execute("UPDATE BOWLER SET jersey_no=%s, economy=%s, wickets=%s, average=%s, runs=%s, balls_bowled=%s WHERE "
              "jersey_no=%s", (new_jersey_no,new_economy,new_wickets,new_average,new_runs,new_balls_bowled,jersey_no))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_team(team_name):
    c.execute('DELETE FROM TEAM WHERE team_name="{}"'.format(team_name))
    mydb.commit()

def delete_player(player_name):
    c.execute('DELETE FROM PLAYER WHERE player_name="{}"'.format(player_name))
    mydb.commit()

def delete_stadium(stadium_name):
    c.execute('DELETE FROM STADIUM WHERE stadium_name="{}"'.format(stadium_name))
    mydb.commit()

def delete_match(match_no):
    c.execute('DELETE FROM MATCHES WHERE match_no={}'.format(match_no))
    mydb.commit()

def delete_team_match(match_no):
    c.execute('DELETE FROM TEAM_MATCH WHERE match_no={}'.format(match_no))
    mydb.commit()

def delete_coach(coach_name):
    c.execute('DELETE FROM COACH WHERE coach_name="{}"'.format(coach_name))
    mydb.commit()

def delete_umpire(umpire_name):
    c.execute('DELETE FROM UMPIRE WHERE umpire_name="{}"'.format(umpire_name))
    mydb.commit()

def delete_batsman(player_name):
    c.execute('CALL delete_batsman("{}")'.format(player_name))
    mydb.commit()

def delete_bowler(player_name):
    c.execute('CALL delete_bowler("{}")'.format(player_name))
    mydb.commit()
    