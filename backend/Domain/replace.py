import re

from Domain.step import Step


class Replace(Step):
    OCC_TYPE = "Todas"
    short_name = "replace"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.text_origin = args["text_origin"]
        self.text_target = args["text_target"]
        self.replace_with = args["replace_with"]
        self.occurrency_type = args["occurrency_type"]
        self.occurrency_number = int(args["occurrency_number"])
        self.check_ignore = args["check_ignore"]

    def execute(self):
        result = ""
        if self.occurrency_number < 0:
            raise Exception("La cantidad de elementos a encontrar debe ser mayor o igual a 0")

        if self.check_ignore:
            occurences = re.findall(self.text_target, self.text_origin, re.IGNORECASE)
        else:
            occurences = re.findall(self.text_target, self.text_origin)

        if self.occurrency_type == self.OCC_TYPE:
            for occurence in occurences:
                self.text_origin = self.text_origin.replace(occurence, self.replace_with)
        else:
            if self.occurrency_number <= len(occurences):

                for occurence in occurences[:self.occurrency_number]:
                    self.text_origin = self.text_origin.replace(occurence, self.replace_with)
            else:
                for occurence in occurences:
                    self.text_origin = self.text_origin.replace(occurence, self.replace_with)

        return self.flow_id, self.text_origin
