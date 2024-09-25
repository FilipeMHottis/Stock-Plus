from typing import TypedDict, List


class ProductInfo(TypedDict):
    product_id: int
    product_name: str
    quantity: int
    price: float
    total_price: float


class UserInfo(TypedDict):
    user_id: int
    name: str
    role: str


class PaymentMethodInfo(TypedDict):
    payment_method_id: int
    method: str


class SaleInfo(TypedDict):
    sale_id: int
    user: UserInfo
    sale_date: str
    payment_method: PaymentMethodInfo
    discount: float
    products: List[ProductInfo]
    total_sale_price: float
