DROP TABLE usuario;

CREATE TABLE usuario(
    rut VARCHAR2(10) PRIMARY KEY,
    tipo_usuario VARCHAR2 (15) NOT NULL,
    p_nombre VARCHAR2 (20) NOT NULL,
    s_nombre VARCHAR2(20),
    p_apellido VARCHAR2 (20) NOT NULL,
    s_apellido VARCHAR2 (20),
    direccion VARCHAR2 (100) NOT NULL,
    correo VARCHAR2(100) NOT NULL,
    contra VARCHAR2 (30) NOT NULL    
);

INSERT INTO usuario VALUES('20876932-3', 'admin', 'Roberto' , null, 
'Pacheco', 'Ruiz', 'Av. Mexico 2051', 'roberto@gmail.com', 'roberto123');

INSERT INTO usuario VALUES('17234894-8', 'vendedor', 'Ricardo' , 'Milano', 
'Aguilera', 'Manquian', 'Pedro Leon Gallo 1929', 'ricardo@gmail.com', 'ricardo123');

INSERT INTO usuario VALUES('19487923-5', 'contador', 'Raquel' , null, 
'Muñoz', 'Rojas', 'Villa Cariño 2969', 'raquel@gmail.com', 'raquel123');

INSERT INTO usuario VALUES('20347632-7', 'bodega', 'Enrique' , 'Pavel', 
'Iglesias', 'Morales', 'Av. Brasil 7820', 'enrique@gmail.com', 'enrique123');

INSERT INTO usuario VALUES('10033190-k', 'invitado', 'Ximena' , 'Alberta', 
'Ilabaca', 'Silva', 'Blest Gana 2270', 'ximena@gmail.com', 'ximena123');
COMMIT;
