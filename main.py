from aiogram.dispatcher.filters.state import State.StatesGroup

class Registration(StateGroup):
    getting_name_state = State()
    getting_phone_number_state = State()
    getting_location_state = State()
    getting_gender_state = State()

class GetProduct(StateGroup):
    getting_pr_name = State()
    getting_pr_count = State()

class Cart(StateGroup):
    waiting_for_product = State()
    waiting_new_count = State()

class Order(StateGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()

