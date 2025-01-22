from modules.db_connection import session
from setup_database import Product

def add_product(product_name, vendor_id, quantity, price_per_unit):
    total_price = quantity * price_per_unit
    new_product = Product(
        product_name=product_name,
        vendor_id=vendor_id,
        quantity=quantity,
        price_per_unit=price_per_unit,
        total_price=total_price
    )
    session.add(new_product)
    session.commit()
    return "Product added successfully!"

def get_products():
    return session.query(Product).all()

def issue_product(product_id, quantity_issued):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product and product.quantity >= quantity_issued:
        product.quantity -= quantity_issued
        product.total_price = product.quantity * product.price_per_unit
        session.commit()
        return "Product issued successfully!"
    else:
        return "Insufficient quantity or invalid product!"
