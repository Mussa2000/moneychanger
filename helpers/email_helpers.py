from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_with_attachments(subject, html_template, text_content, from_email, to_emails, attachments=None, context={}):
    # Render the HTML template to a string
    html_content = render_to_string(html_template, context)

    # Create the email message object
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    msg.attach_alternative(html_content, "text/html")

    # Attach each file
    if attachments:
        for attachment in attachments:
            msg.attach(attachment[0], attachment[1].read(), attachment[2])

    # Send the email
    msg.send()