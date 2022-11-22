create database semanadejogos;
use semanadejogos;


CREATE TABLE Alunos(
id_Alunos INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
Nome VARCHAR(30),
Sexo CHAR(1)
);

CREATE TABLE Eventos(
id_Eventos INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_Alunos_fk INTEGER NOT NULL,
Esporte VARCHAR(30),
FOREIGN KEY(id_Alunos_fk) REFERENCES Alunos (id_Alunos) on update cascade on delete cascade
);

CREATE TABLE Turmas(
id_Turma INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_eventos_fk INTEGER NOT NULL,
id_Alunos_fk INTEGER NOT NULL,
Serie CHAR(1),
Turma CHAR(1),
FOREIGN KEY(id_eventos_fk) REFERENCES Eventos (id_Eventos) on update cascade on delete cascade,
FOREIGN KEY(id_Alunos_fk) REFERENCES Alunos (id_Alunos) on update cascade on delete cascade
);

SELECT Nome, Esporte FROM Alunos, Eventos
where id_Alunos = id_Alunos_fk;

