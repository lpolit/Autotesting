from Domain.step import Step


class TextSplit(Step):

    short_name = "text_split"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.text = args["text"]
        self.delimiter = args["delimiter"]
        self.index = args["index"]

    def execute(self):
        if self.index == "":
            return self.flow_id, self.text.split(self.delimiter)
        else:
            return self.flow_id, self.text.split(self.delimiter)[int(self.index)]
