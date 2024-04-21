from helpers.erp_api_handler import ERPAPIHandler


def get_erp_next_api():
    headers = {
        "Authorization": "token 4289c3d6f92da18:449ab606a7cffcc",
        "Cookie": "full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=",
    }
    erp_next_api = ERPAPIHandler(
        url="https://Accounts Receivablespilotrun.frappe.cloud/", headers=headers
    )
    return erp_next_api


def post_entity_to_erp_next(method_name, data):
    erp_next_api = get_erp_next_api()
    response = erp_next_api.post(method_name, data)
    return response