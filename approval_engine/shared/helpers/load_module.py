import importlib


def load_model_from_module(module_location: str, module_record_id):
    module = importlib.import_module(module_location)
    model = module.get_model(module_record_id)
    return model
