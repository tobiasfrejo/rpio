class LaserScan(object):
    def __init__(self):

        self.name= "LaserScan"
        self._ranges= None
        self._angle_increment= 0.0


    @property
    def ranges(self):
        """The ranges (read-only)."""
        return self._ranges

    @ranges.setter
    def ranges(self, cmp):
        """The ranges (write)."""
        self._ranges = cmp

    @property
    def angle_increment(self):
        """The angle_increment (read-only)."""
        return self._angle_increment

    @angle_increment.setter
    def angle_increment(self, cmp):
        """The angle_increment (write)."""
        self._angle_increment = cmp


class Direction(object):
    def __init__(self):

        self.name= "Direction"
        self._omega= None
        self._duration= None


    @property
    def omega(self):
        """The omega (read-only)."""
        return self._omega

    @omega.setter
    def omega(self, cmp):
        """The omega (write)."""
        self._omega = cmp

    @property
    def duration(self):
        """The duration (read-only)."""
        return self._duration

    @duration.setter
    def duration(self, cmp):
        """The duration (write)."""
        self._duration = cmp


class AnomalyMessage(object):
    def __init__(self):

        self.name= "AnomalyMessage"
        self._anomaly= None


    @property
    def anomaly(self):
        """The anomaly (read-only)."""
        return self._anomaly

    @anomaly.setter
    def anomaly(self, cmp):
        """The anomaly (write)."""
        self._anomaly = cmp


class NewPlanMessage(object):
    def __init__(self):

        self.name= "NewPlanMessage"
        self._NewPlan= None


    @property
    def NewPlan(self):
        """The NewPlan (read-only)."""
        return self._NewPlan

    @NewPlan.setter
    def NewPlan(self, cmp):
        """The NewPlan (write)."""
        self._NewPlan = cmp


class new_data_message(object):
    def __init__(self):

        self.name= "new_data_message"
        self._new_data= None


    @property
    def new_data(self):
        """The new_data (read-only)."""
        return self._new_data

    @new_data.setter
    def new_data(self, cmp):
        """The new_data (write)."""
        self._new_data = cmp


