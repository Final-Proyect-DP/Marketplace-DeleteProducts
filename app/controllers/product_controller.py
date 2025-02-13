from flask import Blueprint, jsonify, request
from app.models.models import Product
from app.extensions.extensions import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200



@product_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='OK', service='user-read'), 200


