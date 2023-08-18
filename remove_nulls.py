import bpy

# Создайте временный видовой слой для обработки объектов
temp_view_layer = bpy.context.scene.view_layers.new("temp_view_layer")

try:
    # Примените все трансформации ко всем объектам во всех слоях
    for obj in bpy.data.objects:
        # Сделайте объект активным во временном видовом слое
        temp_view_layer.objects.active = obj
        # Выделите объект
        obj.select_set(True)
        # Примените трансформации
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        # Снимите выделение с объекта
        obj.select_set(False)

    # Удалите все null объекты
    for obj in bpy.data.objects:
        if obj.type == 'EMPTY':  # Объекты типа EMPTY обычно используются как null объекты
            bpy.data.objects.remove(obj, do_unlink=True)

    # Переместите все полигональные объекты на верхний уровень
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.parent = None
finally:
    # Удалите временный видовой слой
    bpy.context.scene.view_layers.remove(temp_view_layer)
