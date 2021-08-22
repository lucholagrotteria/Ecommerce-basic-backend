-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.14-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para tp
CREATE DATABASE IF NOT EXISTS `tp` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `tp`;

-- Volcando estructura para tabla tp.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(70) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.categorias: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`ID`, `nombre`) VALUES
	(20, 'Viento'),
	(21, 'Cuerdas'),
	(22, 'Percusion'),
	(23, 'Electricos');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla tp.ciudades
CREATE TABLE IF NOT EXISTS `ciudades` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `id_provincia` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `provincia` (`id_provincia`),
  CONSTRAINT `provincia` FOREIGN KEY (`id_provincia`) REFERENCES `provincias` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.ciudades: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` (`ID`, `nombre`, `id_provincia`) VALUES
	(1, 'CABA', 1),
	(2, 'Rosario', 5),
	(3, 'Santa Rosa', 8),
	(12, 'Carmelo', 75),
	(15, 'Montevideo', 77),
	(71, 'Barcelona', 96);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;

-- Volcando estructura para tabla tp.compras
CREATE TABLE IF NOT EXISTS `compras` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `medio_pago` varchar(30) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `usuario` (`id_usuario`),
  KEY `producto` (`id_producto`),
  CONSTRAINT `producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.compras: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` (`ID`, `medio_pago`, `fecha`, `id_usuario`, `id_producto`) VALUES
	(100, 'tarjeta', '2020-01-12 00:00:00', 1, 40),
	(101, 'tarjeta', '2020-02-16 00:00:00', 2, 41),
	(102, 'tarjeta', '2020-03-21 00:00:00', 3, 42),
	(103, 'tarjeta', '2020-04-19 00:00:00', 4, 43),
	(104, 'tarjeta', '2020-05-26 00:00:00', 5, 44),
	(105, 'tarjeta', '2020-06-05 00:00:00', 6, 45),
	(106, 'tarjeta', '2020-07-09 00:00:00', 7, 46),
	(107, 'tarjeta', '2020-08-13 00:00:00', 8, 47),
	(108, 'tarjeta', '2020-09-30 00:00:00', 9, 48),
	(109, 'tarjeta', '2020-10-28 00:00:00', 10, 49),
	(110, 'tarjeta', '2020-11-17 00:00:00', 11, 50),
	(111, 'tarjeta', '2020-12-15 00:00:00', 12, 51),
	(112, 'tarjeta', '2020-01-23 00:00:00', 13, 52),
	(113, 'tarjeta', '2020-02-11 00:00:00', 14, 53),
	(114, 'tarjeta', '2020-03-22 00:00:00', 15, 54);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;

-- Volcando estructura para vista tp.datosppales
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `datosppales` (
	`nombre_apellido` VARCHAR(81) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fecha_nac` DATE NOT NULL,
	`id_ciudad` INT(11) NULL
) ENGINE=MyISAM;

-- Volcando estructura para procedimiento tp.eliminar_marca
DELIMITER //
CREATE PROCEDURE `eliminar_marca`(IN nombre VARCHAR(70))
BEGIN 
DELETE FROM marcas WHERE ID = 45;
END//
DELIMITER ;

-- Volcando estructura para procedimiento tp.insercion_marcas
DELIMITER //
CREATE PROCEDURE `insercion_marcas`(IN nombre VARCHAR(70))
BEGIN
INSERT INTO marcas(nombre) VALUES(nombre);
END//
DELIMITER ;

-- Volcando estructura para vista tp.listaprecios
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `listaprecios` (
	`producto` VARCHAR(30) NOT NULL COLLATE 'utf8mb4_general_ci',
	`precio` FLOAT(12) NOT NULL,
	`marca` VARCHAR(70) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para vista tp.mail_contraseña
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `mail_contraseña` (
	`mail` TEXT(65535) NOT NULL COLLATE 'utf8mb4_general_ci',
	`contraseña` TEXT(65535) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para tabla tp.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(70) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.marcas: ~15 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`ID`, `nombre`) VALUES
	(30, 'Hohner'),
	(31, 'Suzuki'),
	(32, 'Fender'),
	(33, 'Casio'),
	(34, 'Yamaha'),
	(35, 'Taylor'),
	(36, 'Stagg'),
	(37, 'Meinl'),
	(38, 'Mapex'),
	(39, 'Paiste'),
	(40, 'Knight'),
	(41, 'Pearl'),
	(42, 'Leonard'),
	(43, 'Texas'),
	(44, 'Guild');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla tp.paises
CREATE TABLE IF NOT EXISTS `paises` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=599 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.paises: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` (`ID`, `nombre`) VALUES
	(34, 'España'),
	(49, 'Alemania'),
	(54, 'Argentina'),
	(598, 'Uruguay');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;

-- Volcando estructura para tabla tp.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `modelo` text DEFAULT NULL,
  `precio` float NOT NULL,
  `caracteristicas` text NOT NULL,
  `calificacion` float NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `id_marca` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `categoria` (`id_categoria`),
  KEY `marca` (`id_marca`),
  CONSTRAINT `categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `marca` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.productos: ~16 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`ID`, `nombre`, `modelo`, `precio`, `caracteristicas`, `calificacion`, `id_categoria`, `id_marca`) VALUES
	(40, 'Guitarra Acustica', 'Fg820l', 60100, 'Zurda Color Natural', 4.7, 21, 34),
	(41, 'Guitarra Electrica', 'Stratocastar Road Worn 60s Vintage', 203000, 'Vintage-estilo sincronizado trémolo', 5, 23, 32),
	(42, 'Bajo Electroacustico', 'GS Mini Bass', 115000, 'compacto, liviano y ultra cómodo en las manos', 4.2, 21, 35),
	(43, 'Armonica', 'Pro Harp Diatonica', 5000, 'innovador diseño de sistema Modular (MS)', 2.5, 20, 30),
	(44, 'Saxo Alto', 'JBAS 200 GL', 70000, 'Dorado', 3.3, 20, 40),
	(45, 'Trompeta', 'YTR2330', 110000, 'Sib para principiantes', 4.1, 20, 34),
	(46, 'Bongo Latin', 'Sb-200ch', 8000, ' Madera 7.5 & 6.5 Rims', 4.5, 22, 36),
	(47, 'Cajon Peruano', 'CAJ50MRD', 15000, 'Rojo madera de Abedul con Funda', 1.7, 22, 36),
	(48, 'Pandereta Media Luna', 'Jb917', 1400, '20 Sonajas Varios Colores', 3.5, 22, 40),
	(49, 'Armonica', 'Harp Master', 3961, '10 hoyos y 20 notas', 4.8, 20, 31),
	(50, 'Piano', 'Celviano Ap270bk', 160000, '3 Pedales/negro', 3.9, 21, 33),
	(51, 'Bajo', 'E81-2ts Jazz Bass', 26000, '21 trastes cromados', 4.6, 23, 43),
	(52, 'Bateria', 'Storm Ltst5295ftdk', 125000, 'Madera de 100% de álamo', 2.5, 22, 38),
	(53, 'Guitarra Electroacustica', 'Jumbo Junior MP', 85000, 'Sistema de electrificación: Guild AP-1', 3.4, 21, 44),
	(54, 'Ukelele Soprano', 'Uk20', 8200, 'Clavijas: Nickel', 2.2, 21, 42);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla tp.provincias
CREATE TABLE IF NOT EXISTS `provincias` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `id_pais` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `pais` (`id_pais`),
  CONSTRAINT `pais` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.provincias: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` (`ID`, `nombre`, `id_pais`) VALUES
	(1, 'CABA', 54),
	(5, 'Santa Fe', 54),
	(8, 'La Pampa', 54),
	(75, 'Colonia', 598),
	(77, 'Montevideo', 598),
	(96, 'Cataluña', 34);
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;

-- Volcando estructura para tabla tp.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `apellido` varchar(40) NOT NULL,
  `mail` text NOT NULL,
  `contraseña` text NOT NULL,
  `fecha_nac` date NOT NULL,
  `reputacion` int(11) DEFAULT NULL,
  `id_ciudad` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ciudad` (`id_ciudad`),
  CONSTRAINT `ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudades` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla tp.usuarios: ~15 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`ID`, `nombre`, `apellido`, `mail`, `contraseña`, `fecha_nac`, `reputacion`, `id_ciudad`) VALUES
	(1, 'Maria', 'Dominguez', 'mariadominguez@gmail.com', 'Dom123@', '1990-07-18', 2, 1),
	(2, 'Jose', 'Rodriguez', 'joserodriguez@gmail.com', 'Rod123', '1987-12-15', 4, 2),
	(3, 'Esteban', 'Martinez', 'estebanmartinez@hotmail.com', 'Mar123@', '1993-03-05', 3, 3),
	(4, 'Santiago', 'Farias', 'santiagofarias@yahoo.com.ar', 'Far123@', '1994-06-01', 1, 71),
	(5, 'Carolina', 'Gallardo', 'carolinagallardo@gmail.com', 'Gal123@', '1989-08-14', 5, 12),
	(6, 'Mariana', 'Fernandez', 'marianafernandez@hotmail.com', 'Fer123@', '1996-10-25', 3, 15),
	(7, 'Sebastian', 'Andrada', 'sebasandrada@yahoo.com.ar', 'And123@', '2000-09-23', 4, 1),
	(8, 'Sofia', 'Planes', 'sofiaplanes@gmail.com', 'Pla123@', '1993-11-06', 3, 71),
	(9, 'Matias', 'Armani', 'matiasarmani@gmail.com', 'Arm123@', '1991-04-12', 2, 12),
	(10, 'Paz', 'Ahumada', 'pazahumada@hotmail.com', 'Ahu123@', '1990-03-16', 1, 15),
	(11, 'Lucas', 'Boye', 'lucasboye@yahoo.com.ar', 'Boy123@', '1995-07-24', 5, 3),
	(12, 'Tamara', 'Pereyra', 'tamarapereyra@gmail.com', 'Per123@', '2001-08-19', 2, 2),
	(13, 'Carlos', 'Cavani', 'carloscavani@hotmail.com', 'Cav123@', '1983-12-13', 3, 15),
	(14, 'Pedro', 'Sanchez', 'pedrosanchez@hotmail.com', 'San123@', '1997-02-15', 4, 71),
	(15, 'Denise', 'Palma', 'denisepalma@gmail.com', 'Pal123@', '1994-01-17', 5, 2);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- Volcando estructura para vista tp.datosppales
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `datosppales`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `datosppales` AS SELECT CONCAT(nombre,SPACE(1),apellido) AS nombre_apellido,fecha_nac,id_ciudad
FROM usuarios ;

-- Volcando estructura para vista tp.listaprecios
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `listaprecios`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `listaprecios` AS SELECT (productos.nombre) producto,productos.precio,(marcas.nombre) marca FROM productos
INNER JOIN marcas ON productos.id_marca=marcas.ID ;

-- Volcando estructura para vista tp.mail_contraseña
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `mail_contraseña`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `mail_contraseña` AS select `usuarios`.`mail` AS `mail`,`usuarios`.`contraseña` AS `contraseña` from `usuarios`;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
