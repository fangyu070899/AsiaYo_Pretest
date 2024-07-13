class ValidationError(Exception):
    def __init__(self, errors):
        super().__init__(self)  
        self.errors = errors

    def __str__(self):
        return f"Validation errors: {', '.join(self.errors)}"

def validate_order(order_data):
    required_fields = ['id', 'name', 'address', 'price', 'currency']
    
    # 檢查訂單是否包含所有必要欄位
    for field in required_fields:
        if field not in order_data:
            raise ValidationError(f"Missing required field: {field}")

    # 檢查欄位是否為指定型態
    if not isinstance(order_data['id'], str):
        raise ValidationError("Field 'id' must be a string")
    if not isinstance(order_data['name'], str):
        raise ValidationError("Field 'name' must be a string")
    if not isinstance(order_data['address'], dict):
        raise ValidationError("Field 'address' must be a dictionary")
    if not isinstance(order_data['price'], str):
        raise ValidationError("Field 'price' must be a string")
    if not isinstance(order_data['currency'], str):
        raise ValidationError("Field 'currency' must be a string")
    
    # 檢查地址的子欄位
    address_fields = ['city', 'district', 'street']
    for field in address_fields:
        if field not in order_data['address']:
            raise ValidationError(f"Missing required field in address: {field}")
        if not isinstance(order_data['address'][field], str):
            raise ValidationError(f"Field 'address.{field}' must be a string")

def format_check_and_transform(order):
    errors = []

    # 驗證名稱
    if not all(c.isalpha() or c.isspace() for c in order.name):
        errors.append("Name contains non-English characters")
    if not all(word[0].isupper() for word in order.name.split()):
        errors.append("Name is not capitalized")

    # 驗證貨幣
    if order.currency not in ["TWD", "USD"]:
        errors.append("Currency format is wrong")
    
    if order.currency == "USD":
        order.price = str(int(order.price) * 31)
        order.currency = "TWD"

    # 驗證價格
    # 先驗證貨幣再驗證價格，USD*31 超過2000 也算error
    if int(order.price) > 2000:
        errors.append("Price is over 2000")

    if errors:
        raise ValidationError(errors)
