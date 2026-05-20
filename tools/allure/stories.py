from enum import Enum

class AllureStories(str, Enum):
    SUCCESSFUL_LOGIN = 'Successful login'
    INVALID_LOGIN = 'Invalid login'
    SUCCESSFUL_PURCHASE = 'Successful purchase'