-- Etapa 1
/*
a) Criar um banco de dados vazio chamado escola.
*/
CREATE DATABASE escola;
USE escola;


/*
b) Criar todas as tabelas que fazem parte do banco, a partir do modelo relacional.
c) Definir as restrições de integridade referencial (chaves estrangeiras) nas tabelas necessárias.
d) Definir as chaves primárias das tabelas.
e) Definir as restrições de domínio de atributo.
*/
CREATE TABLE departamentos (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(20) NOT NULL,
    PRIMARY KEY (codigo)
);

CREATE TABLE cursos (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    descricao TEXT,
    codigo_depto INTEGER NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codigo_depto)
        REFERENCES departamentos (codigo)
);

CREATE TABLE professores (
    registro SERIAL AUTO_INCREMENT,
    data_contratacao DATE NOT NULL,
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    nome_social VARCHAR(50),
    endereco VARCHAR(50),
    bairro VARCHAR(20),
    cep CHAR(8),
    cidade VARCHAR(50),
    uf CHAR(2),
    telefone CHAR(12),
    email VARCHAR(50),
    data_nascimento DATE,
    naturalidade VARCHAR(30),
    nacionalidade VARCHAR(30),
    escolaridade VARCHAR(30),
    estado_civil CHAR(20),
    sexo CHAR(1),
    pcd BOOLEAN DEFAULT 0,
    codigo_depto INTEGER NOT NULL,
    PRIMARY KEY (cpf),
    FOREIGN KEY (codigo_depto)
        REFERENCES departamentos (codigo)
);

CREATE TABLE disciplinas (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    qtde_creditos BIGINT NOT NULL,
    cpf_prof CHAR(11) NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (cpf_prof)
        REFERENCES professores (cpf)
);

CREATE TABLE compoe (
    codigo_curso INTEGER NOT NULL,
    codigo_disciplina INTEGER NOT NULL,
    CONSTRAINT PK_compoe PRIMARY KEY (codigo_curso , codigo_disciplina),
    FOREIGN KEY (codigo_curso)
        REFERENCES cursos (codigo),
    FOREIGN KEY (codigo_disciplina)
        REFERENCES disciplinas (codigo)
);

CREATE TABLE pre_requisitos (
    cod_disc INTEGER NOT NULL,
    cod_disc_depend INTEGER NOT NULL,
    CONSTRAINT PK_pre_requisitos PRIMARY KEY (cod_disc, cod_disc_depend),
    FOREIGN KEY (cod_disc)
        REFERENCES disciplinas (codigo),
    FOREIGN KEY (cod_disc_depend)
        REFERENCES disciplinas (codigo)
);

CREATE TABLE alunos (
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    nome_social VARCHAR(50),
    endereco VARCHAR(50),
    bairro VARCHAR(20),
    cep CHAR(8),
    cidade VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL,
    telefone CHAR(12),
    email VARCHAR(50),
    naturalidade VARCHAR(50),
    nacionalidade VARCHAR(50),
    escolaridade VARCHAR(50),
    estado_civil CHAR(20),
    sexo CHAR(20),
    data_nascimento DATE,
    pcd BOOLEAN DEFAULT 0,
    PRIMARY KEY (cpf)
);

CREATE TABLE matriculas (
    codigo_curso INTEGER NOT NULL,
    cpf_aluno CHAR(11) NOT NULL,
    data_matricula DATE NOT NULL,
    CONSTRAINT PK_matriculas PRIMARY KEY (codigo_curso , cpf_aluno),
    FOREIGN KEY (codigo_curso)
        REFERENCES cursos (codigo),
    FOREIGN KEY (cpf_aluno)
        REFERENCES alunos (cpf)
);

CREATE TABLE cursa (
    cpf_aluno CHAR(11) NOT NULL,
    cod_disc INTEGER NOT NULL,
    CONSTRAINT PK_cursa PRIMARY KEY (cpf_aluno , cod_disc),
    FOREIGN KEY (cpf_aluno)
        REFERENCES alunos (cpf),
    FOREIGN KEY (cod_disc)
        REFERENCES disciplinas (codigo)
);


/*
f) Conter comandos de inserção de dados em todas as tabelas. 
Os dados inseridos serão utilizados na etapa 2 do projeto.
*/

INSERT INTO departamentos(nome) VALUES ('Exatas');
INSERT INTO departamentos(nome) VALUES ('Humanas');

INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Matemática', '', 1);
INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Física', '', 1);
INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Química', '', 1);
INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Comunicação', '', 2);
INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Direito', '', 2);
INSERT INTO cursos(nome, descricao, codigo_depto) VALUES ('Pedagogia', '', 2);

INSERT INTO professores(data_contratacao, cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, codigo_depto) 
VALUES ('2022-03-05', '12345678900', 'Ana', '', '', '', '', '', '', '', '', '', '', '', '', 'F', 2);
INSERT INTO professores(data_contratacao, cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, codigo_depto) 
VALUES ('2022-03-12', '98765432199', 'João', '', '', '', '', '', '', '', '', '', '', '', '', 'M', 1);
INSERT INTO professores(data_contratacao, cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, codigo_depto) 
VALUES ('2022-03-18', '45612378952', 'Maria', '', '', '', '', '', '', '', '', '', '', '', '', 'F', 1);
INSERT INTO professores(data_contratacao, cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, codigo_depto) 
VALUES ('2022-03-24', '65432198765', 'Pedro', '', '', '', '', '', '', '', '', '', '', '', '', 'M', 2);
INSERT INTO professores(data_contratacao, cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, codigo_depto) 
VALUES ('2022-03-24', '05432198765', 'Daniel', '', '', '', '', '', '', '', '', '', '', '', '', 'M', 2);

INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Comunicação e Sociedade', 6, '12345678900');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Ética da Comunicação', 6, '12345678900');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Comunicação e Atualidade', 6, '12345678900');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Cálculo diferencial e integral', 6, '98765432199');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Geometria analítica e álgebra linear', 7, '98765432199');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Estatística e probabilidades', 8, '98765432199');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Mecânica', 6, '05432198765');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Teoria da Relatividade', 7, '05432198765');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Termodinâmica', 8, '05432198765');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Segurança e Técnicas de Laboratório', 6, '45612378952');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Química Orgânica', 7, '45612378952');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Química Inorgânica', 7, '45612378952');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Ciência Política e Social', 6, '65432198765');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Ilicitude e Culpabilidade', 6, '65432198765');
INSERT INTO disciplinas(nome, qtde_creditos, cpf_prof) VALUES ('Fatos e Negócios Jurídicos', 6, '65432198765');

INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (1, 4);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (1, 5);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (1, 6);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (2, 4);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (2, 7);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (2, 8);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (2, 9);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (3, 4);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (3, 10);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (3, 11);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (3, 12);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (4, 1);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (4, 2);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (4, 3);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (5, 13);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (5, 14);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (5, 15);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (6, 1);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (6, 2);
INSERT INTO compoe(codigo_curso, codigo_disciplina) VALUES (6, 3);

INSERT INTO pre_requisitos(cod_disc, cod_disc_depend) VALUES (6, 4);
INSERT INTO pre_requisitos(cod_disc, cod_disc_depend) VALUES (8, 4);
INSERT INTO pre_requisitos(cod_disc, cod_disc_depend) VALUES (9, 4);
INSERT INTO pre_requisitos(cod_disc, cod_disc_depend) VALUES (11, 4);
INSERT INTO pre_requisitos(cod_disc, cod_disc_depend) VALUES (12, 4);

INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('02312312332', 'Pedro', '', '', '', '', '', '', '', '', '', '', '', '', 'M', '1978-12-21');
INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('45645645656', 'Catarina', '', '', '', '', '', '', '', '', '', '', '', '', 'F', '1983-11-14');
INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('78978978989', 'Magali', '', '', '', '', '', '', '', '', '', '', '', '', 'F', '1976-07-06');
INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('98798798798', 'Leandro', '', '', '', '', '', '', '', '', '', '', '', '', 'M', '1993-02-08');
INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('65465465465', 'Samantha', '', '', '', '', '', '', '', '', '', '', '', '', 'F', '1977-01-03');
INSERT INTO alunos(cpf, nome, nome_social, endereco, bairro, cep, cidade, uf, telefone, email, 
naturalidade, nacionalidade, escolaridade, estado_civil, sexo, data_nascimento)
VALUES ('32132132132', 'Teodoro', '', '', '', '', '', '', '', '', '', '', '', '', 'M', '1979-05-07');

INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (1, '45645645656', '2022-03-25');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (2, '45645645656', '2022-03-25');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (2, '65465465465', '2022-03-26');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (3, '32132132132', '2022-03-26');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (4, '02312312332', '2022-03-27');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (6, '02312312332', '2022-03-27');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (5, '78978978989', '2022-03-27');
INSERT INTO matriculas(codigo_curso, cpf_aluno, data_matricula) VALUES (6, '98798798798', '2022-03-28');

INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('45645645656', 4);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('45645645656', 7);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('65465465465', 7);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('32132132132', 10);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('02312312332', 1);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('02312312332', 2);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('78978978989', 13);
INSERT INTO cursa(cpf_aluno, cod_disc) VALUES ('98798798798', 1);

/*
SELECT * FROM departamentos;
SELECT * FROM cursos;
SELECT * FROM professores;
SELECT * FROM disciplinas;
SELECT * FROM compoe;
SELECT * FROM pre_requisitos;
SELECT * FROM alunos;
SELECT * FROM matriculas;
SELECT * FROM cursa;
*/



-- Etapa 2
/* 
a) Produza um relatório que contenha os dados dos alunos matriculados 
em todos os cursos oferecidos pela escola.
*/
CREATE VIEW alunos_matriculados AS
    SELECT 
        a.nome aluno,
        DATE_FORMAT(data_matricula, '%d/%m/%Y') data_matricula,
        c.nome curso,
        d.nome depto
    FROM
        cursos c
            JOIN
        departamentos d ON c.codigo_depto = d.codigo
            JOIN
        matriculas m ON m.codigo_curso = c.codigo
            JOIN
        alunos a ON m.cpf_aluno = a.cpf
    ORDER BY a.nome , c.nome;

SELECT * FROM alunos_matriculados;


/*
b) Produza um relatório com os dados de todos os cursos, com suas respectivas 
disciplinas, oferecidos pela escola.
*/
CREATE VIEW curso_disciplinas AS
    SELECT 
        c.nome curso,
        dep.nome depto,
        d.nome disciplina,
        d.qtde_creditos,
        p.nome professor
    FROM
        cursos c
            JOIN
        departamentos dep ON dep.codigo = c.codigo_depto
            JOIN
        compoe cd ON cd.codigo_curso = c.codigo
            JOIN
        disciplinas d ON cd.codigo_disciplina = d.codigo
            JOIN
        professores p ON d.cpf_prof = p.cpf
    ORDER BY c.nome , d.nome;

SELECT * FROM curso_disciplinas;


/*
c) Produza um relatório que contenha o nome dos alunos e as 
disciplinas em que estão matriculados.
*/
CREATE VIEW aluno_disciplinas AS
    SELECT 
        a.nome aluno,
        a.cpf,
        d.nome disciplina,
        d.qtde_creditos,
        p.nome professor
    FROM
        alunos a
            JOIN
        cursa ad ON ad.cpf_aluno = a.cpf
            JOIN
        disciplinas d ON ad.cod_disc = d.codigo
            JOIN
        professores p ON d.cpf_prof = p.cpf
    ORDER BY a.nome , d.nome;

SELECT * FROM aluno_disciplinas;


/*
d) Produza um relatório com os dados dos professores e 
as disciplinas que ministram.
*/
CREATE VIEW professor_disciplinas AS
    SELECT 
        p.nome professor,
        p.cpf,
        d.codigo id,
        d.nome disciplina,
        d.qtde_creditos
    FROM
        disciplinas d
            JOIN
        professores p ON d.cpf_prof = p.cpf
    ORDER BY p.nome , d.nome;

SELECT * FROM professor_disciplinas;


/*
e) Produza um relatório com os nomes das disciplinas e 
seus pré-requisitos.
*/
CREATE VIEW disciplina_requisitos AS
    SELECT 
        d.codigo id,
        d.nome disciplina,
        p.nome prof,
        dd.codigo id_dd,
        dd.nome pre_requisito,
        pp.nome prof_dd
    FROM
        pre_requisitos pr
            JOIN
        disciplinas AS d ON pr.cod_disc = d.codigo
            JOIN
        disciplinas AS dd ON pr.cod_disc_depend = dd.codigo
            JOIN
        professores AS p ON p.cpf = d.cpf_prof
            JOIN
        professores AS pp ON pp.cpf = dd.cpf_prof;

SELECT * FROM disciplina_requisitos;


/*
f) Produza um relatório com a média de idade dos alunos 
matriculados em cada curso.
*/
CREATE VIEW media_idade_alunos AS
    SELECT 
        c.nome curso,
        FLOOR(AVG(TIMESTAMPDIFF(YEAR,
                    data_nascimento,
                    NOW()))) media_idade,
        COUNT(m.cpf_aluno) AS qtd_alunos
    FROM
        cursos c
            JOIN
        matriculas m ON m.codigo_curso = c.codigo
            JOIN
        alunos a ON m.cpf_aluno = a.cpf
    GROUP BY 1
    ORDER BY c.nome;

SELECT * FROM media_idade_alunos;


/*
g) Produza um relatório com os cursos oferecidos 
por cada departamento.
*/
CREATE VIEW departamento_cursos AS
    SELECT 
        c.codigo id_curso,
        c.nome curso,
        d.codigo id_depto,
        d.nome depto
    FROM
        cursos c
            JOIN
        departamentos d ON d.codigo = c.codigo_depto
    ORDER BY c.nome;

SELECT * FROM departamento_cursos;

