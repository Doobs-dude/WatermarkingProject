import smtplib #library used for SMTP 
from email.message import EmailMessage
import ssl #also helps with the transfer
from PIL import Image

img = "GUI_test/info_button.png"
email = "doobsdude@gmail.com"
def send_email(watermarked_image, watermark_email):
    
    my_email = "kavinkarthick.2007@gmail.com" #email used for emailing the customers, may be replaced by a work email later
    my_password = "ezcn htsx qybq ansv" # a password used for the sender work email to log in securely
    customer_email = watermark_email

    subject = "Your image has been successfully watermarked!"
    body = "Here is your watermarked image ready for download, thank you for using our software"

    message = EmailMessage() # initialise a variable to the email message function
    message['From'] = my_email #match the appropriate variables
    message['To'] = customer_email
    message['Subject'] = subject
    message.set_content(body)
    
    image = open(watermarked_image, "rb") # open the image file
    image_data = image.read() # read the image file
    image_name = "watermarked_image.png" # name the image file
    message.add_attachment(image_data, maintype = "image", subtype ='png', filename = image_name) #add the attachment with image data, type and name
    image.close()
    
    context = ssl.create_default_context() #create the ssl layer for secure transmission

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) #gmails ssl email, along with ssl encrypted email transmission port number
    smtp.login(my_email, my_password) #login snippet of code
    smtp.send_message(message) #the email snippet
    smtp.quit()

    print(f"Sent to {customer_email}") #debugging statment

send_email(img, email)