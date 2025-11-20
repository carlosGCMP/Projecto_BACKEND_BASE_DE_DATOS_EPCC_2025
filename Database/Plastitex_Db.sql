CREATE DATABASE plastitex_db;

\c plastitex_db; ---Pa conectar--

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    clave TEXT NOT NULL,
    rol_id INT NOT NULL REFERENCES roles(id),
    estado BOOLEAN DEFAULT TRUE
);
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    categoria_id INT REFERENCES categorias(id),
    stock_actual INT DEFAULT 0,
    stock_min INT DEFAULT 0,
    stock_max INT DEFAULT 0,
    precio NUMERIC(10,2) DEFAULT 0
);
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    razon_social VARCHAR(150) NOT NULL,
    ruc VARCHAR(15) UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT,
    correo VARCHAR(100)
);
CREATE TABLE orden_compra (
    id SERIAL PRIMARY KEY,
    proveedor_id INT NOT NULL REFERENCES proveedores(id),
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    total NUMERIC(10,2) DEFAULT 0,
    estado VARCHAR(20) DEFAULT 'PENDIENTE'
);
CREATE TABLE detalle_orden_compra (
    id SERIAL PRIMARY KEY,
    orden_id INT NOT NULL REFERENCES orden_compra(id) ON DELETE CASCADE,
    producto_id INT NOT NULL REFERENCES productos(id),
    cantidad INT NOT NULL,
    precio_unitario NUMERIC(10,2) NOT NULL
);
CREATE TABLE nota_ingreso (
    id SERIAL PRIMARY KEY,
    proveedor_id INT REFERENCES proveedores(id),
    usuario_id INT REFERENCES usuarios(id),
    fecha DATE NOT NULL DEFAULT CURRENT_DATE
);
CREATE TABLE detalle_nota_ingreso (
    id SERIAL PRIMARY KEY,
    nota_ingreso_id INT NOT NULL REFERENCES nota_ingreso(id) ON DELETE CASCADE,
    producto_id INT NOT NULL REFERENCES productos(id),
    cantidad INT NOT NULL
);
CREATE TABLE nota_salida (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id),
    motivo VARCHAR(200),
    destino VARCHAR(200),
    fecha DATE NOT NULL DEFAULT CURRENT_DATE
);
CREATE TABLE detalle_nota_salida (
    id SERIAL PRIMARY KEY,
    nota_salida_id INT NOT NULL REFERENCES nota_salida(id) ON DELETE CASCADE,
    producto_id INT NOT NULL REFERENCES productos(id),
    cantidad INT NOT NULL
);
