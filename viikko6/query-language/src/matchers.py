class QueryBuilder:
    def __init__(self):
        self._query = All()

    def playsIn(self, team):
        self._query = And(PlaysIn(team), self._query)
        return self

    def hasAtLeast(self, value, attr):
        self._query = And(HasAtLeast(value, attr), self._query)
        return self

    def hasFewerThan(self, value, attr):
        self._query = And(HasFewerThan(value, attr), self._query)
        return self

    def oneOf(self, q1, q2):
        self._query = Or(q1, q2)
        return self

    def build(self):
        query = self._query
        self._query = All()

        return query

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, condition):
        self._condition = condition

    def test(self, player):
        if self._condition.test(player):
            return False
        
        return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *conditions):
        self._conditions = conditions

    def test(self, player):
        result = False
        for condition in self._conditions:
            if result or condition.test(player):
                result = True
        return result