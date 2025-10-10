from ..entities.OrdenCompra import OrdenCompra, DetalleCompra
from ..db import db

class ModelOrdenCompra:
    @staticmethod
    def create(orden, detalles):
        try:
            cursor = db.connection.cursor()
            print ('Creating order:', orden)
            print ('With details:', detalles)
            cursor.execute(
                """
                INSERT INTO orden_compras (proveedor_id, fecha, activo)
                VALUES (%s, %s, %s)
                """,
                (orden['proveedor_rif'], orden.get('fecha'), orden.get('activo', 1))
            )
            orden_id = cursor.lastrowid
            for det in detalles:
                cursor.execute(
                    """
                    INSERT INTO detalle_compras (cantidad, precio_unitario, orden_id, producto_id)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (det['cantidad'], det['precio_unitario'], orden_id, det['producto_codigo'])
                )
            db.connection.commit()
            return orden_id
        except Exception as e:
            db.connection.rollback()
            print('Error al crear orden de compra:', e)
            return None

    @staticmethod
    def get_all():
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                """
                SELECT oc.id, oc.proveedor_id, oc.fecha, oc.activo, p.razon_social
                FROM orden_compras oc
                JOIN proveedores p ON oc.proveedor_id = p.id
                ORDER BY oc.fecha DESC
                """
            )
            ordenes = cursor.fetchall()
            resultado = []
            for o in ordenes:
                cursor.execute(
                    """
                    SELECT dc.id, dc.cantidad, dc.precio_unitario, dc.producto_id, pr.nombre
                    FROM detalle_compras dc
                    JOIN productos pr ON dc.producto_id = pr.id
                    WHERE dc.orden_id = %s
                    """,
                    (o[0],)
                )
                detalles = cursor.fetchall()
                resultado.append({
                    'id': o[0],
                    'proveedor_id': o[1],
                    'fecha': o[2],
                    'activo': o[3],
                    'proveedor_nombre': o[4],
                    'detalles': [
                        {
                            'id': d[0],
                            'cantidad': d[1],
                            'precio_unitario': d[2],
                            'producto_id': d[3],
                            'producto_nombre': d[4]
                        } for d in detalles
                    ]
                })
            print('Órdenes recuperadas:', resultado)
            return resultado
        except Exception as e:
            print('Error al obtener ordenes de compra:', e)
            return []
