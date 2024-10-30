CREATE DATABASE finale_python;
 
CREATE TABLE runners (runner_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
						runner_name VARCHAR (50) NOT null,
						runner_surname VARCHAR (50) NOT NULL,
						runner_mail VARCHAR (50) UNIQUE NOT null);

INSERT INTO runners (runner_name,runner_surname,runner_mail) VALUES('Paolo', 'Rossi', 'paolorossi@gmail.com');