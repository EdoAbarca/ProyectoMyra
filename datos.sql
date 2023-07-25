BEGIN;

-- INSERT INTO rotativa_myra.api_cargo (id, cargo)

-- INSERT INTO rotativa_myra.api_contrato (id, contrato, fecha_inicio, fecha_termino)

-- DATOS DEL SISTEMA
-- Centro
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (1, "Todos");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (2, "Administración");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (3, "Cuidados");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (4, "Residencia");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (5, "Hotel Clínico");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (6, "SMI");
INSERT INTO rotativa_myra.api_centro (id, nombreCentro) VALUES (7, "Otro");

-- Area
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (1, "Todos");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (2, "Administradores");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (3, "Auxiliares");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (4, "Coordinadores");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (5, "Cuidadores");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (6, "Enfermeros");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (7, "Fonoaudiólogos");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (8, "Kinesiólogos");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (9, "Médicos");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (10, "Nutricionistas");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (11, "Podólogos");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (12, "Practicantes");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (13, "TENS");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (14, "Terapeutas");
INSERT INTO rotativa_myra.api_area (id, nombreArea) VALUES (15, "Otros");


-- Cliente
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (1, "Todos");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (2, "ACHS");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (3, "Human Solutions");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (4, "ISL");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (5, "Mutual");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (6, "Particular");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (7, "Residencia");
INSERT INTO rotativa_myra.api_cliente (id, nombreCliente) VALUES (8, "Otro");


-- Tipo Alerta
INSERT INTO rotativa_myra.api_tipoalerta (id, tipoalerta) VALUES (1, "Todos");
INSERT INTO rotativa_myra.api_tipoalerta (id, tipoalerta) VALUES (2, "Inasistencia");
INSERT INTO rotativa_myra.api_tipoalerta (id, tipoalerta) VALUES (3, "Paciente Complejo");
INSERT INTO rotativa_myra.api_tipoalerta (id, tipoalerta) VALUES (4, "Exceso Horas");
INSERT INTO rotativa_myra.api_tipoalerta (id, tipoalerta) VALUES (5, "Otro");

-- Tipo Turno
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (1, "Todos");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (2, "2 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (3, "4 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (4, "6 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (5, "8 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (6, "10 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (7, "12 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (8, "24 Hrs");
INSERT INTO rotativa_myra.api_tipoturno (id, tipoTurno) VALUES (9, "Otro");


-- Contrato
INSERT INTO rotativa_myra.api_contrato (id, tipoContrato) VALUES (1, "Normal");
INSERT INTO rotativa_myra.api_contrato (id, tipoContrato) VALUES (2, "V2");
INSERT INTO rotativa_myra.api_contrato (id, tipoContrato) VALUES (3, "Nc");
INSERT INTO rotativa_myra.api_contrato (id, tipoContrato) VALUES (4, "Honorarios");


-- Region
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (1, "Arica y Parinacota");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (2, "Tarapacá");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (3, "Antofagasta");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (4, "Atacama");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (5, "Coquimbo");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (6, "Valparaíso");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (7, "Metropolitana");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (8, "Libertador General Bernardo O’Higgins");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (9, "Maule");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (10, "Ñuble");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (11, "Bío-Bío");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (12, "La Araucanía");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (13, "Los Ríos");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (14, "Los Lagos");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (15, "Aysén");
INSERT INTO rotativa_myra.api_region (id, nombreRegion) VALUES (16, "Antártica");

-- Zona
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (1, "Santiago Poniente");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (2, "Santiago Oriente");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (3, "Santiago Sur");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (4, "Santiago Norte");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (5, "Rancagua");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (6, "Graneros");
INSERT INTO rotativa_myra.api_zona (id, nombreZona) VALUES (7, "Melipilla");



-- DATOS DE PRUEBA DEL SISTEMA
-- Cargo
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (1, "TENS");
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (2, "TENS");
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (3, "CUIDADOR");
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (4, "TENS");
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (5, "CUIDADORA");
INSERT INTO rotativa_myra.api_cargo (id, cargo) VALUES (6, "COORDINADOR");

-- Coordinador
INSERT INTO rotativa_myra.api_coordinador (id, nombre, rut, idCargo_id, idCentro_id) VALUES (1, "Gonzalo Esteban Palacios", "17476393-3", 6, 1);
INSERT INTO rotativa_myra.api_coordinador (id, nombre, rut, idCargo_id, idCentro_id) VALUES (2, "Veronica Ines Henriquez", "8712193-3", 6, 1);
INSERT INTO rotativa_myra.api_coordinador (id, nombre, rut, idCargo_id, idCentro_id) VALUES (3, "Francesca Pilar Monroi", "16792115-9", 6, 2);
/*
-- Profesional
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, inasistencias, horasTotales, horasExtras, vacaciones, licencia,
 idCentro_id, idArea_id, idCargo_id, idContrato_id, idCoordinador_id, valorHora, horasCont,horasObj,turnosTrab,bonoColacion, bonoMov, bonoResp) 
 VALUES (1, "Fabiola Suillan Lagos Cuevas", "13080327-K", 15, 96, 360, 0, 0, 3, 2, 5, 2, 1);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, inasistencias, horasTotales, horasExtras, vacaciones, licencia,
 idCentro_id, idArea_id, idCargo_id, idContrato_id, idCoordinador_id) VALUES (2, "Mariela Leonardo Tantarico", "20345687-7", 19, 96, 0, 0, 0, 1, 2, 2, 1, 2);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, inasistencias, horasTotales, horasExtras, vacaciones, licencia,
 idCentro_id, idArea_id, idCargo_id, idContrato_id, idCoordinador_id) VALUES (3, "Damari Ester Saldaño Valderrama", "14364143-0", 11, 192, 264, 0, 0, 3, 2, 5, 3, 1);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, inasistencias, horasTotales, horasExtras, vacaciones, licencia,
 idCentro_id, idArea_id, idCargo_id, idContrato_id, idCoordinador_id) VALUES (4, "Angelina Elizabeth Cespedes Cortes", "14987436-7", 0, 288, 0, 0, 0, 2, 3, 4, 1, 3);
INSERT INTO rotativa_myra.api_profesional (id, nombre, rut, inasistencias, horasTotales, horasExtras, vacaciones, licencia,
 idCentro_id, idArea_id, idCargo_id, idContrato_id, idCoordinador_id) VALUES (5, "Maria Ines Torres Flores", "9901664-7", 2, 288, 0, 0, 0, 3, 2, 5, 1, 1);

-- Pago
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (1, 440000,
130000, 338887, 80000, 0, 0, 0, 0, 0, 0, 0, 988887, 988887, 104625, 0, 69222, 5933, 0, 0, 0, 0, 0, 179780, 809107, "2023-04-30",2);
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (2, 425000,
117250, 0, 44000, 0, 0, 72000, 20654, 11000, 11000, 0, 700904, 586250, 67126, 0, 41038, 3518, 0, 0, 0, 0, 0, 111682, 589222, "2023-04-30",3);
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (3, 460000,
115000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 575000, 575000, 61468, 0, 40250, 3450, 0, 0, 0, 0, 0, 105168, 469832, "2023-04-30",1);
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (4, 287000,
71750, 0, 0, 0, 0, 28000, 0, 0, 0, 0, 386750, 358750, 37956, 0, 25113, 2153, 0, 0, 0, 0, 0, 65222, 321528, "2023-04-30",4);
INSERT INTO rotativa_myra.api_pago (id, sueldoBase, gratificacion, horaExtra, bonos, aguinaldo, vacaciones, viatico,
asignacionFamiliar, colacion, movilizacion, salaCuna, totalHaberes, totalImponible, afp, isapre, fonasa, segCes,
imptoUnico, ctaAfp, anticipos, descuento, ley3, totalDescuento, liquido, fechaPago, idProfesional_id) VALUES (5, 410000,
102500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 512500, 512500, 58630, 0, 35875, 3075, 0, 0, 0, 0, 0, 97580, 414920, "2023-04-30",5);





-- Paciente
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (1, "Guillermo Quiñones Guzman", "2023-03-03", True, 20000, 1, 1, 1, 1);
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (2, "Rodrigo Belmar Pando", "2023-03-01", True, 30000, 2, 3, 1, 1);
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (3, "Juan Munita Alfaro", "2023-03-01", True, 35000, 3, 4, 1, 1);
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (4, "Oscar Orlando Lopez Roldan", "2023-03-01", True,40000,4, 5, 6, 1);
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (5, "Carlos Antonio Fernandez Hernandez", "2023-03-01", True,25000,5, 6, 6, 1);
INSERT INTO rotativa_myra.api_paciente (id, nombre, fechaInicioAtencion, vigente, gasto, idTipoTurno_id, idZona_id, idRegion_id, idCliente_id)
VALUES (6, "Residencia Myrasalud", "2023-03-01", True,10000, 6, 7, 1, 6);

-- Turno (añadir mas)
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (1, "2023-03-03", "2023-03-04", 24, 1, 5);
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (2, "2023-03-01", "2023-03-02", 24, 2, 1);
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (3, "2023-03-01", "2023-03-02", 24, 3, 3);
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (4, "2023-03-16", "2023-03-17", 24, 4, 4);
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (5, "2023-03-01", "2023-03-02", 24, 5, 4);
INSERT INTO rotativa_myra.api_turno (id, fechaInicio, fechaTermino, horas, idPaciente_id, idProfesional_id)
VALUES (6, "2023-03-01", "2023-03-02", 24, 6, 2);

-- Asistencia (añadir mas)
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id, idPaciente_id, idTurno_id)
VALUES (1, "2023-03-01", True, 1, 1, 2, 2);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id, idPaciente_id, idTurno_id)
VALUES (2, "2023-03-01", True, 1, 3, 3, 3);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id, idPaciente_id, idTurno_id)
VALUES (3, "2023-03-16", True, 1, 4, 4, 4);
INSERT INTO rotativa_myra.api_asistencia (id, fechaAsistencia, asisteProfesional, estado, idProfesional_id, idPaciente_id, idTurno_id)
VALUES (4, "2023-03-03", True, 1, 5, 1, 1);

*/
COMMIT;
