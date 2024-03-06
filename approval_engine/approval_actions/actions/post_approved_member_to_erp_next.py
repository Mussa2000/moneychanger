# import loguru

# from helpers.erp_next_helpers import post_entity_to_erp_next
# logger = loguru.logger


# class Action(object):
#     def execute(self, approval_ticket):
#         if approval_ticket.is_approved():
#             logger.info("Preparing to post approved member to ERP NEXT")
#             member = approval_ticket.get_action_model()
#             member_erp_next_payload = member.erp_next_payload
#             try:
#                 response = post_entity_to_erp_next('create-member', member_erp_next_payload)
#                 logger.info(f"Response {response.content}")
#             except Exception as e:
#                 logger.critical(f"Error creating Member: {member.pk} -> {e}")