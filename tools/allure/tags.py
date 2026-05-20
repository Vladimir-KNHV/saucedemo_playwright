from enum import Enum

class AllureTag(str, Enum):
    REGRESSION = 'REGRESSION'
    AUTHORIZATION = 'AUTHORIZATION'
    E2E = 'e2e'