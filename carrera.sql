create database carreras;

use carreras;

CREATE TABLE carrerasuniversitarias(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    carrera varchar(100) COLLATE latin1_spanish_ci NOT NULL,
    universidad varchar(30) COLLATE latin1_spanish_ci NOT NULL,
    duracion varchar(5) COLLATE latin1_spanish_ci NOT NULL,
    modalidad varchar(30) COLLATE latin1_spanish_ci NOT NULL,
    telefono varchar(10) COLLATE latin1_spanish_ci NOT NULL,
    direccion varchar(1000) COLLATE latin1_spanish_ci NOT NULL
);

INSERT INTO `carreras`.`carrerasuni` (`carrera`, `universidad`, `duracion`, `modalidad`, `telefono`, `direccion`) VALUES ('ITI', 'UTEC', '3', 'VESPERTINO', '123456', 'TULANCINGO HGO.');
INSERT INTO `carreras`.`carrerasuni` (`carrera`, `universidad`, `duracion`, `modalidad`, `telefono`, `direccion`) VALUES ('MEDICINA', 'UAEH', '6', 'VESPERTINO', '555555', 'PACHUCA DE SOTO HGO.');
INSERT INTO `carreras`.`carrerasuni` (`carrera`, `universidad`, `duracion`, `modalidad`, `telefono`, `direccion`) VALUES ('DERECHO', 'UAEH', '3', 'MATUTINO', '777777', 'PACHUCA DE SOTO HGO.');
