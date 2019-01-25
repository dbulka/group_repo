class User(object):

    def __init__(self, role, id, email, password, project, team):
        self.role = role
        self.id = id
        self.email = email
        self.password = password
        self.project = project
        self.team = team

    def __init__(self):
        pass


class Task(object):

    def __init__(self, id, type, priority, severity, author, assignee, tag, estimation):
        self.id = id
        self.type = type
        self.priority = priority
        self.severity = severity
        self.author = author
        self.assignee = assignee
        self.tag = tag
        self.estimation = estimation

    def __init__(self):
        pass


class Project(object):

    def __init__(self, board, team, name):
        self.name = name
        self.board = board
        self.team = team

    def __init__(self):
        pass
