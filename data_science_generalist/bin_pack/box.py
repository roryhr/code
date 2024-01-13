class Part:
    def __init__(self, volume, weight):
        self.volume = volume
        self.weight = weight

    def __repr__(self):
        return "Part({}, {})".format(self.volume, self.weight)


class Box:
    def __init__(self, volume_capacity, weight_capacity, cost=3):
        self.volume_capacity = volume_capacity
        self.weight_capacity = weight_capacity
        self.cost = cost
        self.current_volume = 0
        self.current_weight = 0
        self.contents = []

    def __repr__(self):
        return f"Box({self.volume_capacity}, {self.weight_capacity})"

    def add(self, part):
        """Add part to current box

        Parameters
        ----------
        part : Part
            Part to add to Box

        Returns
        -------
        added : bool
            Was the part added?
        """
        added = self.can_add(part)
        if added:
            self._add(part)

        return added

    def can_add(self, part):
        if self.current_volume + part.volume > self.volume_capacity:
            return False
        elif self.current_weight + part.weight > self.weight_capacity:
            return False

        return True

    def _add(self, part):
        self.contents.append(part)
        self.current_volume += part.volume
        self.current_weight += part.weight
