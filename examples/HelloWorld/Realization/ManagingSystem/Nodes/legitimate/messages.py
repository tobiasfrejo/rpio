class laserScan(object):
    def __init__(self):

        self.name= "laserScan"
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


class direction(object):
    def __init__(self):

        self.name= "direction"
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
        self._Anomaly= None


    @property
    def Anomaly(self):
        """The Anomaly (read-only)."""
        return self._Anomaly

    @Anomaly.setter
    def Anomaly(self, cmp):
        """The Anomaly (write)."""
        self._Anomaly = cmp


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


