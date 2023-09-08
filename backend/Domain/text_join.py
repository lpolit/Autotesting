from domain.step import Step


class TextJoin(Step):

    short_name = "text_join"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.text = args["text"]
        self.delimiter = args["delimiter"]

    def execute(self):
        formatted_text = list(map(str.strip, self.text.split(",")))
        return self.flow_id, self.delimiter.join(formatted_text)
