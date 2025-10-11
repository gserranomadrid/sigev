from .entities.Factura import Factura, DetalleFactura
from ..db import db

class ModelFactura:
    @classmethod
    def get_by_id(cls, db, factura_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                '''
                SELECT f.id, f.cliente_id, f.fecha, f.total, f.estado, c.razon_social
                FROM facturas f
                JOIN clientes c ON f.cliente_id = c.id
                WHERE f.id = %s
                ''', (factura_id,)
            )
            f = cursor.fetchone()
            if not f:
                return None
            cursor.execute(
                '''
                SELECT df.id, df.producto_id, df.cantidad, df.precio_unitario, p.nombre
                FROM detalle_facturas df
                JOIN productos p ON df.producto_id = p.id
                WHERE df.factura_id = %s
                ''', (factura_id,)
            )
            detalles = cursor.fetchall()
            factura = {
                'id': f[0],
                'cliente_id': f[1],
                'fecha': f[2],
                'total': f[3],
                'estado': f[4],
                'cliente_nombre': f[5],
                'detalles': [
                    {
                        'id': d[0],
                        'producto_id': d[1],
                        'cantidad': d[2],
                        'precio_unitario': d[3],
                        'producto_nombre': d[4]
                    } for d in detalles
                ]
            }
            return factura
        except Exception as ex:
            print(f"Error al obtener factura por id: {ex}")
            return None
    @classmethod
    def create(cls, db, factura: Factura):
        try:
            cursor = db.connection.cursor()
            # Iniciar transacción
            db.connection.begin()
            sql = "INSERT INTO facturas (cliente_id, fecha, total) VALUES (%s, %s, %s)"
            cursor.execute(sql, (
                factura.get_cliente_id(),
                factura.get_fecha(),
                factura.get_total()
            ))
            factura_id = cursor.lastrowid
            for det in factura.get_detalles():
                # Validar stock
                cursor.execute("SELECT stock FROM productos WHERE id = %s", (det.get_producto_id(),))
                row = cursor.fetchone()
                if not row:
                    db.connection.rollback()
                    print(f"Producto no encontrado: {det.get_producto_id()}")
                    raise Exception(f"Producto no encontrado: {det.get_producto_id()}")
                stock_actual = row[0]
                if det.get_cantidad() > stock_actual:
                    db.connection.rollback()
                    print(f"Stock insuficiente para producto {det.get_producto_id()} (stock: {stock_actual}, solicitado: {det.get_cantidad()})")
                    raise Exception(f"Stock insuficiente para producto {det.get_producto_id()} (stock: {stock_actual}, solicitado: {det.get_cantidad()})")
                # Descontar stock
                cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (det.get_cantidad(), det.get_producto_id()))
                # Insertar detalle
                cursor.execute(
                    """
                    INSERT INTO detalle_facturas (factura_id, producto_id, cantidad, precio_unitario)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (factura_id, det.get_producto_id(), det.get_cantidad(), det.get_precio_unitario())
                )
            db.connection.commit()
            return factura_id
        except Exception as ex:
            db.connection.rollback()
            print(f"Error al crear factura: {ex}")
            raise

    @classmethod
    def get_all(cls, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                """
                SELECT f.id, f.cliente_id, f.fecha, f.total, f.estado, c.razon_social
                FROM facturas f
                JOIN clientes c ON f.cliente_id = c.id
                ORDER BY f.fecha DESC
                """
            )
            facturas = cursor.fetchall()
            resultado = []
            for f in facturas:
                cursor.execute(
                    """
                    SELECT df.id, df.producto_id, df.cantidad, df.precio_unitario, p.nombre
                    FROM detalle_facturas df
                    JOIN productos p ON df.producto_id = p.id
                    WHERE df.factura_id = %s
                    """,
                    (f[0],)
                )
                detalles = cursor.fetchall()
                resultado.append({
                    'id': f[0],
                    'cliente_id': f[1],
                    'fecha': f[2],
                    'total': f[3],
                    'estado': f[4],
                    'cliente_nombre': f[5],
                    'detalles': [
                        {
                            'id': d[0],
                            'producto_id': d[1],
                            'cantidad': d[2],
                            'precio_unitario': d[3],
                            'producto_nombre': d[4]
                        } for d in detalles
                    ]
                })
            return resultado
        except Exception as ex:
            print(f"Error al obtener facturas: {ex}")
            return []
