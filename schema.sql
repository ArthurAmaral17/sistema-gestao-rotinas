BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO "alembic_version" VALUES('773192d13c92');
CREATE TABLE categorias (
	id INTEGER NOT NULL, 
	nome VARCHAR(64) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (nome)
);
INSERT INTO "categorias" VALUES(1,'Beber');
CREATE TABLE execucoes_diarias (
	id INTEGER NOT NULL, 
	data DATE NOT NULL, 
	concluida BOOLEAN, 
	rotina_id INTEGER NOT NULL, 
	usuario_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(rotina_id) REFERENCES rotinas (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuarios (id)
);
CREATE TABLE rotinas (
	id INTEGER NOT NULL, 
	titulo VARCHAR(100) NOT NULL, 
	descricao TEXT, 
	ativa BOOLEAN NOT NULL, 
	usuario_id INTEGER NOT NULL, 
	categoria_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(categoria_id) REFERENCES categorias (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuarios (id)
);
CREATE TABLE usuarios (
	id INTEGER NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	senha_hash VARCHAR(128), 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO "usuarios" VALUES(1,'sjbhsa','arthuramaralzeus2@gmail.com','scrypt:32768:8:1$vBc8h2KBtOzPgh1q$13444595f7589781e677182947277fa81a6d965a673248f93d4b83bf43610f0503906b877995e8594173ecb7eef553c9e2b02205fea287f70b68c09195db6871');
INSERT INTO "usuarios" VALUES(2,'kjqajhwex','arthuramaralzeus1@gmail.com','scrypt:32768:8:1$9QIpAfxAHwgws7CF$7e4ac81f8a1ac5c71dfb47704c9084b8ee3362b8124490e2801274f68df58d46191b23bed94679f43913443b8d0ccdac35fbdc4a9814fe26549cef8665eac1a2');
INSERT INTO "usuarios" VALUES(3,'Arthur Amaral Dos Santos','arthuramaralzeu@gmail.com','scrypt:32768:8:1$NamXEUjF6lqU5CvZ$c3960d681468cd3840beac0a0e346db4ff2da19059123058b661479d8fb90b1dc2f78a4dd993b70b7b480035d477280fd4f352c577e21450a2245e13b1c40b7b');
COMMIT;
