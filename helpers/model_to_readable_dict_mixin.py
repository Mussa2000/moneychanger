import stringcase


class ModelToReadableDictMixin:
    def to_readable_dict(self):
        model_raw_dict = self.__dict__
        model_final_dict = {}

        # try:
        #     del model_raw_dict["id"]
        # except:
        #     ...

        for old_key in model_raw_dict.keys():
            if old_key == 'id':
                continue
            new_key = stringcase.titlecase(old_key)
            model_final_dict[new_key] = model_raw_dict[old_key]

        model_items = model_final_dict.items()

        return model_items
