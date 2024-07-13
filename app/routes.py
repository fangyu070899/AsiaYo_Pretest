from flask import Blueprint, request, jsonify, render_template
from app.order import Order
from app.validation import validate_order, format_check_and_transform, ValidationError

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    try:
        validate_order(data)  # 檢查訂單是否包含所有必要欄位，並且是否為指定型態
    except ValidationError as e:
        return jsonify({"errors": e.errors}), 400

    order = Order(
        id=data['id'],
        name=data['name'],
        address=data['address'],
        price=data['price'],
        currency=data['currency']
    )
    
    try:
        format_check_and_transform(order)  # 驗證訂單格式並轉換
    except ValidationError as e:
        return jsonify({"errors": e.errors}), 400

    return jsonify({
        "id": order.id,
        "name": order.name,
        "address": order.address,
        "price": order.price,
        "currency": order.currency
    }), 200

# 網站可測試 api
@orders_bp.route('/')
def order_form():
    return render_template('order_form.html')
