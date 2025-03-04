import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# eto yung file directory ng nagawang EXCEL FILE or CSV
file_path = r"C:\Users\Asus\OneDrive\Desktop\testing1csv.xlsx"

HOST_EMAIL =    'notsoworkingg@gmail.com'
HOST_PASS =     'hmds iiuj rxdm advw'

# email ni therapist (or patient)
RECIPIENT = ['mori30salazar@gmail.com', 'justinlwrnc09@gmail.com', 'workingamap@gmail.com']

msg = MIMEMultipart()
msg['From'] = HOST_EMAIL
msg['To'] = ', '.join(RECIPIENT)
msg['Subject'] = 'Subject: CSV EXERCISE PAKITIGNAN'

# Open the Excel file and read the contents
# FOR EXCEL SHEET

with open(file_path, 'rb') as f:

    # Attach the Excel file
    part = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    part.set_payload(f.read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment', filename=f.name)  # Add header for attachment
    msg.attach(part)

# FOR CSV 

# with open(file_path, 'rb') as f:

#     # Attach the CSV file
#     part = MIMEBase('text', 'csv')
#     part.set_payload(f.read())  
#     encoders.encode_base64(part)  
#     part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(f.name))  # Add header for attachment
#     msg.attach(part)

# Send email

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()                                           # Start TLS encryption
server.login(HOST_EMAIL, HOST_PASS)                         # Login with your email credentials
server.sendmail(msg['From'], RECIPIENT, msg.as_string())    # Send email
server.quit()                                               # Quit the server connection