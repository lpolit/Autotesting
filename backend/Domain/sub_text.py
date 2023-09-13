from Domain.step import Step


class SubText(Step):

    short_name = "sub_text"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.text_origin = args["text_origin"]
        self.option_type = args["option_type"]
        self.start_index = args["start_index"] if "start_index" in args else None
        self.end_index = args["end_index"] if "end_index" in args else None

    def execute(self):
        if self.option_type == "after":
            self.end_index = None
        elif self.option_type == "before":
            self.start_index = None

        if self.start_index is not None and self.end_index is None:
            if int(self.start_index) > len(self.text_origin):
                raise Exception("El indice de comienzo no puede ser mayor a largo del texto")
            elif int(self.start_index) < 0:
                raise Exception("El indice de comienzo no puede ser menor a 0")
            else:
                result = self.text_origin[int(self.start_index):self.end_index]
        elif self.start_index is None and self.end_index is not None:
            if int(self.end_index) > len(self.text_origin):
                raise Exception("El indice de fin no puede ser mayor a largo del texto")
            elif int(self.end_index) < 0:
                raise Exception("El indice de fin no puede ser menor a 0")
            else:
                result = self.text_origin[self.start_index:int(self.end_index)]
        elif self.start_index is not None and self.end_index is not None:
            if int(self.start_index) > int(self.end_index):
                raise Exception("El indice de comienzo no puede ser mayor que el de fin")
            elif int(self.start_index) < 0 or int(self.end_index) < 0:
                raise Exception("El indice de comienzo o fin no puede ser menor que 0")
            elif int(self.start_index) > len(self.text_origin) or int(self.end_index) > len(self.text_origin):
                raise Exception("El indice de comienzo o fin no puede ser mayor al largo del texto")
            else:
                result = self.text_origin[int(self.start_index):int(self.end_index)]
        else:
            result = self.text_origin[self.start_index:self.end_index]

        return self.flow_id, result
