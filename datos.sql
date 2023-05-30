BEGIN;

-- INSERT INTO rotativa_myra.api_cargo (id, cargo)

-- INSERT INTO rotativa_myra.api_contrato (id, contrato, fecha_inicio, fecha_termino)

-- Centro
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (1, "Residencia");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (2, "Regiones");

-- Area
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (1, "Administracion");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (2, "Cuidados");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (3, "Kinesiologia");

-- Profesional
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id) VALUES (1, "Natalia Damaris Perello Contreras", "19456957-5", 2, 1);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id) VALUES (2, "Mariela Leonardo Tantarico", "20345687-7", 1, 2);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id) VALUES (3, "Will Hermes Torrealba Alvarez", "9234876-0", 1, 2);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id) VALUES (4, "Angelina Elizabeth Cespedes Cortes", "14987436-7", 2, 3);
