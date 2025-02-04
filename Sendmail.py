def Tosend_il(recipient):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from EmailBody import EnterBody
    from EmailSubject import Sub_Email
    # Email details
    sender_email = "081bei037.shasank@pcampus.edu.np"
    sender_password = "hlstykrdvvmhzwxm"  # Use an app password if using Gmail with 2FA
    receiver_email = recipient

    # Email content
    subject = Sub_Email()
    body = EnterBody()

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade to a secure connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()
