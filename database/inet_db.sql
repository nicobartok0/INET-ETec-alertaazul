-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-11-2022 a las 17:08:16
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inet_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alertas`
--

CREATE TABLE `alertas` (
  `id_alerta` int(11) NOT NULL,
  `id_usuario_fk` int(11) NOT NULL,
  `origen` varchar(255) NOT NULL,
  `hora_inicio` time NOT NULL DEFAULT current_timestamp(),
  `hora_fin` time NOT NULL,
  `estado` varchar(255) NOT NULL DEFAULT 'Sin atender',
  `fecha_inicio` date NOT NULL DEFAULT current_timestamp(),
  `fecha_fin` date NOT NULL,
  `tipo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alertas`
--

INSERT INTO `alertas` (`id_alerta`, `id_usuario_fk`, `origen`, `hora_inicio`, `hora_fin`, `estado`, `fecha_inicio`, `fecha_fin`, `tipo`) VALUES
(3, 4, 'Banio', '10:55:39', '12:21:16', 'Atendido', '2022-11-15', '2022-11-17', 'emergencia'),
(4, 4, 'Banio', '11:26:36', '12:21:19', 'Atendido', '2022-11-15', '2022-11-17', 'normal'),
(5, 1, 'Cama', '11:26:56', '12:21:21', 'Atendido', '2022-11-15', '2022-11-17', 'normal'),
(6, 1, 'Cama', '11:26:57', '12:21:24', 'Atendido', '2022-11-15', '2022-11-17', 'normal'),
(7, 1, 'Cama', '11:26:58', '12:21:26', 'Atendido', '2022-11-15', '2022-11-17', 'normal'),
(8, 1, 'Cama', '11:27:00', '00:00:00', 'Sin atender', '2022-11-17', '0000-00-00', 'normal'),
(9, 1, 'Cama', '11:27:12', '00:00:00', 'Sin atender', '2022-11-17', '0000-00-00', 'emergencia'),
(10, 1, 'Cama', '11:38:57', '00:00:00', 'Sin atender', '2022-11-17', '0000-00-00', 'emergencia'),
(11, 1, 'Cama', '11:38:58', '00:00:00', 'Sin atender', '2022-11-17', '0000-00-00', 'emergencia'),
(12, 1, 'Cama', '11:38:59', '00:00:00', 'Sin atender', '2022-11-17', '0000-00-00', 'emergencia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areas`
--

CREATE TABLE `areas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `areas`
--

INSERT INTO `areas` (`id`, `nombre`) VALUES
(1, 'area prueba'),
(18, 'area2'),
(21, 'area2'),
(23, 'area3'),
(25, 'area4'),
(26, 'area1'),
(27, 'Cardiología');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fichas`
--

CREATE TABLE `fichas` (
  `id_ficha` int(11) NOT NULL,
  `id_persona_fk` int(11) NOT NULL,
  `peso` int(11) NOT NULL,
  `temperatura` int(11) NOT NULL,
  `presion` int(11) NOT NULL,
  `enfermedades_preexistentes` varchar(100) NOT NULL,
  `observaciones` text NOT NULL,
  `area_fk` int(30) NOT NULL,
  `enfermero_fk` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fichas`
--

INSERT INTO `fichas` (`id_ficha`, `id_persona_fk`, `peso`, `temperatura`, `presion`, `enfermedades_preexistentes`, `observaciones`, `area_fk`, `enfermero_fk`) VALUES
(1, 3, 80, 36, 120, 'diabetes', 'Buena salud física.', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id_persona` int(11) NOT NULL,
  `nombre_persona` varchar(255) NOT NULL,
  `apellido_persona` varchar(255) NOT NULL,
  `dni_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id_persona`, `nombre_persona`, `apellido_persona`, `dni_persona`) VALUES
(1, 'John', 'Doe', 12345678),
(3, 'José', 'Gomez', 32298876),
(4, 'Pedro', 'Pascal', 28376375);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(255) NOT NULL,
  `id_persona_fk` int(11) NOT NULL,
  `id_area_fk` int(11) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `rol` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre_usuario`, `id_persona_fk`, `id_area_fk`, `contraseña`, `rol`) VALUES
(1, 'johndoeuser', 1, 1, '123321', ''),
(4, 'josegomezuser', 3, 26, '123', 'paciente'),
(5, 'drPedro', 4, 27, '123', 'medico');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alertas`
--
ALTER TABLE `alertas`
  ADD PRIMARY KEY (`id_alerta`),
  ADD KEY `id_usuario_fk` (`id_usuario_fk`);

--
-- Indices de la tabla `areas`
--
ALTER TABLE `areas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fichas`
--
ALTER TABLE `fichas`
  ADD PRIMARY KEY (`id_ficha`),
  ADD KEY `id_persona_fk` (`id_persona_fk`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_persona_fk` (`id_persona_fk`),
  ADD KEY `id_area_fk` (`id_area_fk`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alertas`
--
ALTER TABLE `alertas`
  MODIFY `id_alerta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `areas`
--
ALTER TABLE `areas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `fichas`
--
ALTER TABLE `fichas`
  MODIFY `id_ficha` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alertas`
--
ALTER TABLE `alertas`
  ADD CONSTRAINT `alertas_ibfk_1` FOREIGN KEY (`id_usuario_fk`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `fichas`
--
ALTER TABLE `fichas`
  ADD CONSTRAINT `fichas_ibfk_1` FOREIGN KEY (`id_persona_fk`) REFERENCES `personas` (`id_persona`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_persona_fk`) REFERENCES `personas` (`id_persona`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`id_area_fk`) REFERENCES `areas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
