BEGIN;

-- INSERT INTO rotativa_myra.api_cargo (id, cargo)

-- INSERT INTO rotativa_myra.api_contrato (id, contrato, fecha_inicio, fecha_termino)

-- Centro
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (1, "Residencia");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (2, "Regiones");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (3, "Cuidados");

-- Area
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (1, "Administracion");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (2, "Cuidados");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (3, "Kinesiologia");

-- Cargo
INSERT INTO rotativa_myra.api_cargo (id, cargo, tipoContrato, fechaInicio, fechaTermino) VALUES (1, "TENS", "contrato", "2023-03-01", "2023-03-31");
INSERT INTO rotativa_myra.api_cargo (id, cargo, tipoContrato, fechaInicio, fechaTermino) VALUES (2, "TENS", "contrato", "2023-03-01", "2023-03-31");
INSERT INTO rotativa_myra.api_cargo (id, cargo, tipoContrato, fechaInicio, fechaTermino) VALUES (3, "CUIDADOR", "contrato", "2023-03-01", "2023-03-31");
INSERT INTO rotativa_myra.api_cargo (id, cargo, tipoContrato, fechaInicio, fechaTermino) VALUES (4, "TENS", "contrato", "2023-03-01", "2023-03-31");
INSERT INTO rotativa_myra.api_cargo (id, cargo, tipoContrato, fechaInicio, fechaTermino) VALUES (5, "CUIDADORA", "contrato", "2023-03-01", "2023-03-31");

-- Profesional
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id, idCargo_id) VALUES (1, "Natalia Damaris Perello Contreras", "19456957-5", 2, 1, 1);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id, idCargo_id) VALUES (2, "Mariela Leonardo Tantarico", "20345687-7", 1, 2, 2);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id, idCargo_id) VALUES (3, "Will Hermes Torrealba Alvarez", "9234876-0", 1, 2, 3);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id, idCargo_id) VALUES (4, "Angelina Elizabeth Cespedes Cortes", "14987436-7", 2, 3, 4);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, idCentro_id, idArea_id, idCargo_id) VALUES (5, "Maria Ines Torres Fuentes", "9901664-7", 3, 2, 5);

-- Pago
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (1, 440000,
130000, 338887, 80000, 0, 0, 0, 0, 0, 0, 0, 988887, 988887, 104625, 0, 69222, 5933, 0, 0, 0, 0, 0, 179780, 809107, "2023-04-30",2);


-- Asistencia
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id) VALUES (1, "2023-03-01", True, 1, 1);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id) VALUES (2, "2023-03-01", True, 1, 2);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id) VALUES (3, "2023-03-24", True, 1, 3);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id) VALUES (4, "2023-03-16", True, 1, 4);

-- Region
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (1, "Metropolitana");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (2, "Valparaíso");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (3, "Coquimbo");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (4, "Los Lagos");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (5, "Bío-Bío");

-- Zona
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (1, "Santiago Poniente");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (2, "Santiago Oriente");

-- Cliente
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (1, "ISL");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (2, "mutual");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (3, "particular");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (4, "ACHS");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (5, "Human Solutions");

-- Paciente
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, idZona_id, idRegion_id, idCliente_id)
VALUES (1, "Guillermo Quiñones Guzman", "2023-03-03", True, 1, 1, 1);

-- Turno
INSERT INTO rotativa_myra.api_turno (id, tipoTurno, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (1, "24 x 7", "2023-03-03", "2023-03-04", 24, 1, 5);
