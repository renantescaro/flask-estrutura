
CREATE TABLE usuario(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	senha VARCHAR(100) NOT NULL,
	id_grupo INT NOT NULL,
	
	FOREIGN KEY (id_grupo) REFERENCES grupo_usuario(id),
	PRIMARY KEY (id)
);

CREATE TABLE grupo_usuario(
	id INT NOT NULL AUTO_INCREMENT,
	descricao VARCHAR(100),
	PRIMARY KEY(id)
);