from flask import Flask, request, jsonify
from initial_data import Item, inventory

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Obtener el inventario completo
@app.route('/stock/get', methods=['GET'])
def get_inventory():
    items = [{'id': item.id, 'name': item.name, 'quantity': item.quantity} for item in inventory]
    return jsonify(items)

# Obtener el inventario de un elemento especificado por ID
@app.route('/stock/get/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in inventory if item.id == item_id), None)
    if item:
        return jsonify({'id': item.id, 'name': item.name, 'quantity': item.quantity})
    return jsonify({'message': 'Item no encontrado'}), 404

# Crear un nuevo registro en el inventario
@app.route('/stock/create', methods=['POST'])
def create_item():
    data = request.json
    new_id = len(inventory) + 1
    new_item = Item(new_id, data['name'], data['quantity'])
    inventory.append(new_item)
    return jsonify({'id': new_id}), 201

# Actualizar los datos de un elemento de inventario especificado por ID
@app.route('/stock/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in inventory if item.id == item_id), None)
    if item:
        data = request.json
        item.name = data['name']
        item.quantity = data['quantity']
        return jsonify({'message': 'Item actualizado exitosamente'})
    return jsonify({'message': 'Item no encontrado'}), 404

# Eliminar un elemento de inventario especificado por ID
@app.route('/stock/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    item = next((item for item in inventory if item.id == item_id), None)
    if item:
        inventory = [item for item in inventory if item.id != item_id]
        return jsonify({'message': 'Item eliminado exitosamente'})
    return jsonify({'message': 'Item no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
