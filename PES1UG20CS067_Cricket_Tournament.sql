--DDL Commands to create the tables and build the database
CREATE TABLE STADIUM(stadium_name VARCHAR(50), stadium_id INT PRIMARY KEY, capacity INT, city VARCHAR(20), address VARCHAR(50));

CREATE TABLE TEAM(team_name VARCHAR(50) PRIMARY KEY, city VARCHAR(20), wins INT, losses INT, draws INT, team_rank INT, home_stadium_id INT, rival_team_name VARCHAR(50), FOREIGN KEY(home_stadium_id) REFERENCES STADIUM(stadium_id) ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY(rival_team_name) REFERENCES TEAM(team_name) ON UPDATE CASCADE ON DELETE SET NULL);

CREATE TABLE PLAYER(player_name VARCHAR(50), jersey_no INT PRIMARY KEY, test INT, odi INT, t20 INT, dob DATE, debut DATE, keeper VARCHAR(10), team_name VARCHAR(50), FOREIGN KEY(team_name) REFERENCES TEAM(team_name) ON DELETE SET NULL ON UPDATE CASCADE);

CREATE TABLE MATCHES(match_no INT PRIMARY KEY, toss VARCHAR(10), result VARCHAR(50), match_date DATE, man_of_match VARCHAR(50), stadium_id INT, FOREIGN KEY(stadium_id) REFERENCES STADIUM(stadium_id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE COLORS(team_name VARCHAR(50) NOT NULL, color VARCHAR(20), FOREIGN KEY(team_name) REFERENCES TEAM(team_name) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE UMPIRE(umpire_name VARCHAR(50), umpire_id INT PRIMARY KEY, no_of_matches INT, dob DATE, country_origin VARCHAR(20));

CREATE TABLE COACH(coach_name VARCHAR(50), coach_id INT PRIMARY KEY, dob DATE, country_origin VARCHAR(20), team_name VARCHAR(50), FOREIGN KEY(team_name) REFERENCES TEAM(team_name) ON DELETE SET NULL ON UPDATE CASCADE);

CREATE TABLE BOWLER(jersey_no INT PRIMARY KEY, economy FLOAT, wickets INT, average FLOAT, runs INT, balls_bowled INT, FOREIGN KEY(jersey_no) REFERENCES PLAYER(jersey_no) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE BATSMAN(jersey_no INT PRIMARY KEY, sixes INT, runs INT, average FLOAT, fifties INT, fours INT, hundreds INT, FOREIGN KEY(jersey_no) REFERENCES PLAYER(jersey_no) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE TEAM_CAPTAIN(jersey_no INT PRIMARY KEY, team_name VARCHAR(50) UNIQUE, FOREIGN KEY(jersey_no) REFERENCES PLAYER(jersey_no) ON UPDATE CASCADE, FOREIGN KEY(team_name) REFERENCES TEAM(team_name) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE TEAM_MATCH(team_name VARCHAR(50), match_no INT NOT NULL, FOREIGN KEY(team_name) REFERENCES TEAM(team_name) ON UPDATE CASCADE, FOREIGN KEY(match_no) REFERENCES MATCHES(match_no) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE MATCH_UMPIRE(match_no INT NOT NULL, umpire_id INT NOT NULL, FOREIGN KEY(match_no) REFERENCES MATCHES(match_no) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN key(umpire_id) REFERENCES UMPIRE(umpire_id) ON DELETE CASCADE ON UPDATE CASCADE);


--Populating the tables
INSERT INTO STADIUM VALUES
("M. Chinnaswamy Stadium",1,40000,"Bengaluru","Mahatma Gandhi Rd, near Cubbon Road"),
("Arun Jaitley Ground",2,41842,"Delhi","Jawaharlal Nehru Marg, Feroze Shah Kotla"),
("Eden Gardens",3,66000,"Kolkata","Maidan, B.B.D. Bagh"),
("Wankhede Stadium",4,33500,"Mumbai","Vinoo Mankad Rd, Churchgate"),
("Rajiv Gandhi International Cricket Stadium",5,55000,"Hyderabad","RGI Stadium Rd, Uppal"),
("M. A. Chidambaram Stadium",6,50000,"Chennai","Wallajah Road, Chepauk"),
("Sawai Mansingh Stadium",7,30000,"Jaipur","Janpath, Jaipur Nagar Nigam"),
("PCA Stadium",8,27000,"Mohali"," I.S. Bindra Stadium, Sukhna Path");


INSERT INTO TEAM(team_name,city,wins,losses,draws,team_rank,home_stadium_id) VALUES
("Royal Challengers Bangalore","Bengaluru",7,7,0,4,1),
("Sunrisers Hyderabad","Hyderabad",7,7,0,3,5),
("Mumbai Indians","Mumbai",9,5,0,1,4),
("Chennai Super Kings","Chennai",6,8,0,7,6),
("Kolkata Knight Riders","Kolkata",7,7,0,5,3),
("Rajasthan Royals","Jaipur",6,8,0,8,7),
("Punjab Kings","Mohali",6,8,0,6,8),
("Delhi Capitals","Delhi",8,6,0,2,2);

UPDATE TEAM SET rival_team_name="Sunrisers Hyderabad" WHERE team_name="Royal Challengers Bangalore";
UPDATE TEAM SET rival_team_name="Royal Challengers Bangalore" WHERE team_name="Sunrisers Hyderabad";
UPDATE TEAM SET rival_team_name="Mumbai Indians" WHERE team_name="Chennai Super Kings";
UPDATE TEAM SET rival_team_name="Chennai Super Kings" WHERE team_name="Mumbai Indians";


INSERT INTO COLORS VALUES
("Royal Challengers Bangalore","red"),
("Royal Challengers Bangalore","black"),
("Sunrisers Hyderabad","orange"),
("Sunrisers Hyderabad","black"),
("Mumbai Indians","light Blue"),
("Chennai Super Kings","yellow"),
("Kolkata Knight Riders","purple"),
("Kolkata Knight Riders","gold"),
("Rajasthan Royals","pink"),
("Rajasthan Royals","dark blue"),
("Punjab Kings","red"),
("Punjab Kings","gold"),
("Delhi Capitals","red"),
("Delhi Capitals","blue");


INSERT INTO UMPIRE VALUES
("Sundaram Ravi",1,131,"1966-04-22","India"),
("Anil Chaudhary",2,109,"1965-03-12","India"),
("Kumar Dharmasena",3,94,"1971-04-24","Sri Lanka"),
("Chettithody Shamshuddin",4,89,"1970-03-22","India"),
("Nitin Menon",5,78,"1983-11-02","India"),
("Marais Erasmus",6,69,"1964-02-27","South Africa"),
("Chris Gaffaney",7,64,"1975-11-30","New Zealand"),
("C. K. Nandan",8,59,"1963-10-14","India"),
("Bruce Oxenford",9,55,"1960-03-05","Australia"),
("Asad Rauf",10,51,"1956-05-12","Pakistan");


INSERT INTO PLAYER VALUES
("Virat Kohli",18,102,262,115,"1988-11-05","2008-12-18",0,"Royal Challengers Bangalore"),
("AB De Villiers",17,114,228,78,"1984-02-17","2005-02-02",1,"Royal Challengers Bangalore"),
("Mohammed Siraj",73,13,13,6,"1994-03-13","2019-01-15",0,"Royal Challengers Bangalore"),
("Glenn Maxwell",34,7,127,98,"1988-10-14","2008-12-18",0,"Royal Challengers Bangalore"),
("Wanindu Hasaranga",41,4,31,32,"1997-06-29","2019-09-01",0,"Royal Challengers Bangalore"),
("MS Dhoni",7,90,350,98,"1981-07-07","2005-12-02",1,"Chennai Super Kings"),
("Robin Uthappa",8,60,171,64,"1985-11-11","2006-04-09",1,"Chennai Super Kings"),
("Ravindra Jadeja",88,102,262,115,"1988-12-06","2008-04-19",0,"Chennai Super Kings"),
("Deepak Chahar",90,9,24,63,"1992-08-07","2018-07-08",0,"Chennai Super Kings"),
("Ambati rayudu",5,0,55,6,"1985-09-23","2013-07-24",0,"Chennai Super Kings"),
("Rohit Sharma",45,45,223,128,"1987-04-30","2013-11-06",0,"Mumbai Indians"),
("Suryakumar Yadav",63,13,40,123,"1990-09-14","2021-07-18",0,"Mumbai Indians"),
("Ishan Kishan",32,0,9,19,"1998-07-18","2021-07-18",1,"Mumbai Indians"),
("Jasprit Bumrah",93,30,72,60,"1993-12-06","2018-01-05",0,"Mumbai Indians"),
("Kieron Pollard",55,0,123,101,"1987-05-12","2007-04-10",0,"Mumbai Indians"),
("Kane Williamson",78,102,262,115,"1988-11-05","2010-11-04",0,"Sunrisers Hyderabad"),
("Bhuvneshwar Kumar",15,21,121,85,"1990-02-05","2013-02-22",0,"Sunrisers Hyderabad"),
("Glenn Phillips",23,1,6,54,"1996-12-06","2020-01-02",1,"Sunrisers Hyderabad"),
("Abdul Samad",28,0,0,0,"2001-10-28","2020-12-29",0,"Sunrisers Hyderabad"),
("Umran Malik",24,0,0,3,"1999-11-22","2022-07-26",0,"Sunrisers Hyderabad"),
("Shreyas Iyer",43,5,33,47,"1994-12-06","2017-11-01",0,"Kolkata Knight Riders"),
("Sam Billings",97,3,25,37,"1991-07-15","2015-07-09",1,"Kolkata Knight Riders"),
("Alex Hales",2,11,70,75,"1989-01-03","2015-12-26",0,"Kolkata Knight Riders"),
("Andre Russell",12,1,56,67,"1988-04-29","2010-11-15",0,"Kolkata Knight Riders"),
("Pat Cummins",30,43,73,50,"1993-05-08","2011-11-17",0,"Kolkata Knight Riders"),
("Sanju Samson",9,0,10,16,"1994-11-11","2015-07-19",0,"Rajasthan Royals"),
("Jos Buttler",64,57,157,103,"1990-07-08","2014-07-27",1,"Rajasthan Royals"),
("Ravichandran Ashwin",99,96,103,65,"1986-07-17","2011-11-06",0,"Rajasthan Royals"),
("Riyan Parag",56,0,0,0,"2001-11-10","2019-04-11",0,"Rajasthan Royals"),
("Trent Boult",58,78,99,55,"1989-07-22","2011-12-06",0,"Rajasthan Royals"),
("KL Rahul",1,43,45,72,"1992-04-18","2014-12-26",0,"Punjab Kings"),
("Mayank Agarwal",48,102,262,115,"1991-02-16","2018-12-26",1,"Punjab Kings"),
("Arshdeep Singh",26,0,0,19,"1999-02-05","2022-07-07",0,"Punjab Kings"),
("Shikhar Dhawan",42,34,161,68,"1985-12-05","2013-03-14",0,"Punjab Kings"),
("Jonny Bairstow",51,89,95,66,"1989-11-26","2011-11-16",0,"Punjab Kings"),
("Rishabh Pant",87,31,27,64,"1997-10-04","2018-08-08",1,"Delhi Capitals"),
("David Warner",31,96,138,99,"1986-10-27","2011-12-01",0,"Delhi Capitals"),
("Prithvi Shaw",100,5,6,1,"1999-11-09","2020-12-17",0,"Delhi Capitals"),
("Axar Patel",20,6,44,37,"1994-01-20","2014-07-15",0,"Delhi Capitals"),
("Shardul Thakur",54,8,27,25,"1991-10-16","2017-08-31",0,"Delhi Capitals");


INSERT INTO BATSMAN VALUES
(18,218,6624,36.2,44,578,5),
(7,229,4978,39.2,24,346,0),
(45,240,5879,30.3,40,419,1),
(63,84,2644,30.05,16,284,0),
(42,136,6243,34.88,47,701,2),
(87,129,2838,34.61,15,260,1),
(88,90,2502,26.6,2,182,0);
--jersey_no,sixes,runs,avg, fifties,fours,hundreds


INSERT INTO BOWLER VALUES
(73,8.78,59,33.07,1951,1334),
(88,7.61,132,30.79,4064,3205),
(90,7.8,59,29.19,1772,1324),
(93,7.4,145,23.31,3380,2742),
(30,8.54,45,30.16,1357,953),
(24,8.83,24,22.5,540,367);
--jersey_no,economy,wickets,avg,runs,balls_bowled


INSERT INTO MATCHES VALUES
(1,"head","Mumbai Indians","2020-10-01","Kieron Pollard",4),
(2,"tails","Royal Challengers Bangalore","2020-10-02","Virat Kohli",7),
(3,"tails","Delhi Capitals","2020-10-03","Shreyas Iyer",2),
(4,"head","Chennai Super Kings","2020-10-04","Shane Watson",6),
(5,"head","Delhi Capitals","2020-10-05","Axar Patel",1),
(6,"tails","Mumbai Indians","2020-10-06","Suryakumar Yadav",8),
(7,"tails","Kolkata Knight Riders","2020-10-07","Rahul Tripathi",3),
(8,"head","Rajasthan Royals","2020-10-08","Jos Buttler",5);




INSERT INTO TEAM_MATCH VALUES
("Mumbai Indians",1),
("Punjab Kings",1),
("Royal Challengers Bangalore",2),
("Rajasthan Royals",2),
("Delhi Capitals",3),
("Kolkata Knight Riders",3),
("Chennai Super Kings",4),
("Sunrisers Hyderabad",4),
("Royal Challengers Bangalore",5),
("Delhi Capitals",5),
("Mumbai Indians",6),
("Punjab Kings",6),
("Kolkata Knight Riders",7),
("Chennai Super Kings",7),
("Rajasthan Royals",8),
("Sunrisers Hyderabad",8);


INSERT INTO COACH VALUES
("Stephen Fleming",1,"1973-04-01","Australia","Chennai Super Kings"),
("Mahela Jayawardene",2,"1977-03-27","Sri Lanka","Mumbai Indians"),
("Sanjay Bangar",3,"1972-10-11","India","Royal Challengers Bangalore"),
("Ricky Ponting",4,"1974-12-19","Australia","Delhi Capitals"),
("Brian Lara",5,"1969-03-02","West Indies","Sunrisers Hyderabad"),
("Anil Kumble",6,"1970-10-17","India","Punjab Kings"),
("Brendon McCullum",7,"1971-10-21","New Zealand","Kolkata Knight Riders"),
("Kumar Sangakkara",8,"1977-10-27","Sri Lanka","Rajasthan Royals");


INSERT INTO TEAM_CAPTAIN VALUES
(18,"Royal Challengers Bangalore"),
(7,"Chennai Super Kings"),
(45,"Mumbai Indians"),
(9,"Rajasthan Royals"),
(87,"Delhi Capitals"),
(1,"Punjab Kings"),
(43,"Kolkata Knight Riders"),
(78,"Sunrisers Hyderabad");


INSERT INTO MATCH_UMPIRE VALUES
(1,1),
(1,2),
(1,3),
(2,4),
(2,5),
(2,6),
(3,7),
(3,8),
(3,9),
(4,10),
(4,1),
(4,2),
(5,3),
(5,4),
(5,5),
(6,6),
(6,7),
(6,8),
(7,9),
(7,10),
(7,1),
(8,2),
(8,3),
(8,4);



--Stored Procedure to get the age of any table if the dob is mentioned in the schema
DELIMITER $$
CREATE procedure dob_to_age(IN date_of_birth DATE, OUT age int)
BEGIN
SELECT TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) into age;
END $$
DELIMITER ;

DELIMITER $$
CREATE procedure update_age()
BEGIN
ALTER TABLE PLAYER
ADD age INT;
UPDATE PLAYER
SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE());
END $$
DELIMITER ;

CALL update_age()


DELIMITER $$
CREATE procedure update_age_umpire()
BEGIN
ALTER TABLE UMPIRE
ADD age INT;
UPDATE UMPIRE
SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE());
END $$
DELIMITER ;

CALL update_age_umpire()


DELIMITER $$
CREATE procedure update_age_coach()
BEGIN
ALTER TABLE COACH
ADD age INT;
UPDATE COACH
SET age=TIMESTAMPDIFF(YEAR, dob, CURDATE());
END $$
DELIMITER ;

CALL update_age_coach();



--Function to return "Money well spent" if home team wins
DELIMITER $$
CREATE FUNCTION home_team_wins(result VARCHAR(50), this_stadium INT)
RETURNS varchar(50)
DETERMINISTIC 
BEGIN
DECLARE usr_msg VARCHAR(50);
IF result=(select team_name from TEAM WHERE home_stadium_id=this_stadium) THEN
SET usr_msg="Money well spent";
ELSE SET usr_msg="Money wasted";
END IF;
RETURN usr_msg;
END $$
DELIMITER ;



--Trigger activated when number of colors for a team > 3
DELIMITER $$
CREATE TRIGGER color_limit
AFTER INSERT
ON COLORS FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
SET error_msg = ('Total number of colors should not exceed 3');
IF (select COUNT(color)
FROM colors
where team_name=new.team_name) >3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$
DELIMITER ;


--Function to get the colors of the team altogether within the team column
DELIMITER $$
CREATE FUNCTION team_colors(teamName VARCHAR(50))
RETURNS varchar(50)
DETERMINISTIC 
BEGIN
DECLARE result VARCHAR(50);
SET result=(SELECT t.colors FROM
(SELECT team_name,GROUP_CONCAT(color) as "colors"
FROM colors 
GROUP BY team_name) as t
WHERE team_name=teamName);
RETURN result;
END $$
DELIMITER ;


--Stored Procedure to delete batsman based on the player name
DELIMITER $$
CREATE procedure delete_batsman(IN playerName varchar(50))
BEGIN
DECLARE jn int;
set jn= (SELECT jersey_no from PLAYER where player_name=playerName);
DELETE FROM batsman WHERE jersey_no=jn;
END $$
DELIMITER ;


--Stored Procedure to delete bowler based on the player name
DELIMITER $$
CREATE procedure delete_bowler(IN playerName varchar(50))
BEGIN
DECLARE jn int;
set jn= (SELECT jersey_no from PLAYER where player_name=playerName);
DELETE FROM bowler WHERE jersey_no=jn;
END $$
DELIMITER ;

--Function to get the captain of a team
DELIMITER $$
CREATE FUNCTION get_captain(teamName VARCHAR(50))
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN
DECLARE result VARCHAR(50);
DECLARE jn INT;
SET jn=(SELECT jersey_no FROM TEAM_CAPTAIN WHERE team_name=teamName);
SET result=(SELECT player_name FROM PLAYER WHERE jersey_no=jn);
RETURN result;
END $$
DELIMITER ;


--Function to get the teams playing in a certain match
DELIMITER $$
CREATE FUNCTION get_first_team_for_match(matchNo INT)
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN
DECLARE result VARCHAR(50);
SET result=(SELECT team_name FROM
(SELECT* FROM team_match
GROUP BY match_no) as m
WHERE match_no=matchNo);
RETURN result;
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION get_second_team_for_match(matchNo INT)
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN
DECLARE result VARCHAR(50);
SET result=(SELECT team_name FROM team_match
WHERE match_no=matchNo
AND team_name<>get_first_team_for_match(matchNo));
RETURN result;
END $$
DELIMITER ;


--Function to get the umpires in certain match
DELIMITER $$
CREATE FUNCTION get_first_umpire(matchNo INT)
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN
DECLARE result VARCHAR(50);
DECLARE umpid INT;
SET umpid=(SELECT umpire_id FROM
(SELECT* FROM MATCH_UMPIRE
GROUP BY match_no) as m
WHERE match_no=matchNo);
SET result=(SELECT umpire_name
FROM UMPIRE
WHERE umpire_id=umpid);
RETURN result;
END $$
DELIMITER ;


--Procedure to get the umpire ID from the Umpire Name
DELIMITER $$
CREATE procedure get_umpid_from_name(IN umpireName varchar(50), OUT umpid INT)
BEGIN
set umpid= (SELECT umpire_id from UMPIRE where umpire_name=umpireName);
END $$
DELIMITER ;


--Function to get the number of wins for the team
DELIMITER $$
CREATE FUNCTION get_cummulative_team(teamName VARCHAR(50))
RETURNS INT
DETERMINISTIC 
BEGIN
DECLARE res INT;
SET res=(SELECT COUNT(match_no)
FROM matches
WHERE result=teamName);
RETURN res;
END $$
DELIMITER ;
