from enum import Enum


class Priority(Enum):
    BLOCKER = 0
    HIGHEST = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4
    LOWEST = 5


class Severity(Enum):
    CRITICAL = 0
    MAJOR = 1
    MINOR = 2
    COSMETIC = 3


class Tag(Enum):
    RESOLVED = 'Resolved'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    IN_REVIEW = 'In review'
    QA = 'QA'
