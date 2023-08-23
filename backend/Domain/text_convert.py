from Domain.step import Step


class TextConvert(Step):

    short_name = "text_convert"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.text = args["text"]


class ConvertLower(TextConvert):
    short_name = "convert_lower"

    def execute(self):
        return self.flow_id, self.text.lower()


class ConvertUpper(TextConvert):

    short_name = "convert_upper"

    def execute(self):
        return self.flow_id, self.text.upper()


class ConvertTitle(TextConvert):

    short_name = "convert_title"

    def execute(self):
        return self.flow_id, self.text.title()


class ConvertCapitalize(TextConvert):

    short_name = "convert_capitalize"

    def execute(self):
        return self.flow_id, self.text.capitalize()


class ConvertToString(TextConvert):

    short_name = "convert_to_string"

    def execute(self):
        return self.flow_id,  str(self.text)


class ConvertToNumber(TextConvert):

    short_name = "convert_to_number"

    def execute(self):
        return self.flow_id, int(self.text)
