from Domain.step import Step


class AsserEquals(Step):

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.actual_value = "actual_value"
        self.expected_value = "expected_value"


class AsserEqual(AsserEquals):

    short_name= "assert_equal"

    def execute(self):
        assert self.expected_value == self.actual_value
        return self.flow_id, None


class AssertGreater(AsserEquals):

    short_name = "assert_greater"

    def execute(self, flow_id):
        assert self.expected_value > self.actual_value
        return self.flow_id, None


class AssertGreaterEqual(AsserEquals):

    short_name = "assert_greater_equal"

    def execute(self, flow_id):
        assert self.expected_value >= self.actual_value
        return self.flow_id, None


class AssertLess(AsserEquals):

    short_name = "assert_less"

    def execute(self, flow_id):
        assert self.expected_value < self.actual_value
        return self.flow_id, None


class AssertLessEqual(AsserEquals):

    short_name = "assert_less_equal"

    def execute(self, flow_id):
        assert self.expected_value <= self.actual_value
        return self.flow_id, None


class AssertNotEqual(AsserEquals):

    short_name = "assert_not_equal"

    def execute(self, flow_id):
        assert self.expected_value != self.actual_value
        return self.flow_id, None


class AssertContains(AsserEquals):

    short_name = "assert_contains"

    def execute(self, flow_id):
        assert self.expected_value.contains(self.actual_value)
        return self.flow_id, None
