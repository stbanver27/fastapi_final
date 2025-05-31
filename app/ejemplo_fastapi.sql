DROP TABLE cliente;
CREATE TABLE cliente(
    rut NUMBER(8) PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) NOT NULL
);
INSERT INTO cliente VALUES(12222,'Lalo','lalo@gmail.com');
INSERT INTO cliente VALUES(13333,'Elvis','elvis@gmail.com');
INSERT INTO cliente VALUES(14444,'Maria','maria@gmail.com');
COMMIT;