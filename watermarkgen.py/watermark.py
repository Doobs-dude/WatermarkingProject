from datetime import datetime
import random



class Watermark:
    def __init__(self, name, email, copyrightnumber, title):
        self.name = name
        self.email = email
        self.copyright_number = copyrightnumber
        self.title = title
        self.key = "secretkey123456789012345678901234" # something random for now
        self.cipher = Fernet(self.key)
        self.date_created = datetime.datetime.now()
        self.distortions = None
        
    def distortion_generator(self):
        user_data = self.name + "/" + self.email + "/" + str(self.copyright_number) + "/" + self.title + "/" + str(self.date_created)
        
        hashed_data = hash.lib.sha256(user_data.encode()) #encryption of the users data
        
        random.seed(hashed_data.hex_digest()) #encryption deterministic on the user info
        
        self.distortions = [(ord(char) + random.randit(0,255)) % 256/51 for char in user_data]
        # the distortions are made between the range 0 to 5 to make sure the RGB difference is not visible

    def distort_generator(self):
        user_data = self.name + "/" + self.email + "/" + str(self.copyright_number) + "/" + self.title + "/" + str(self.date_created)
        encrypted_data = self.cipher_suite.encrypt(user_data.encode())

        self.distortions = [var / 6 for var in encrypted_data] # the distortions are made to make sure the RGB difference is not visible
    
    def decrypt_distortions(self, distortions):
        
        encrypted_data = [var * 6 for var in distortions]
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        name, email, copyright_number, title, date = decrypted_data.split("/")
        
        return name, email, copyright_number, title

    def watermark_percentage(self,distortions):
        nodistortion = 0
        highdistortion = 0
        olddatedistortion = 0
        newdatedistortion = 0
        invaliddatedistortion = 0
        wrongnamedistortion = 0
        wrongemaildistortion = 0
        shortemaildistortion = 0
        wrongtitledistortion = 0




        name, email, copyright_number, title, date = self.decrypt_distortions(distortions)
        for i in range(len(distortions)):
            if distortions[i] == 0:
                nodistortion += 1
            if distortions[i] > 5:
                highdistortion += 1

        if len(name) < 2:
            wrongnamedistortion += 1
        if "@" not in email:
            wrongemaildistortion += 1
        if len(email) < 5:
            shortemaildistortion += 1
        if len(title) < 3:
            wrongtitledistortion += 1       


        
        try:
            actual_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            if actual_date > datetime.now():
                newdatedistortion += 1
            if actual_date.year < 1900:  # Assuming no valid watermarks before 1900
                olddatedistortion += 1
        except ValueError:
            invaliddatedistortion += 1
        
            weights = {
        'email': 0.20,
        'date': 0.20,
        'name': 0.20,
        'title': 0.20,
        'no_distortion': 0.10,
        'high_distortion': 0.10 }
    

       
    

        email_validity = 1 - ((wrongemaildistortion + shortemaildistortion) / 100)
        date_validity = 1 - ((olddatedistortion + newdatedistortion + invaliddatedistortion) / 100)
        name_validity = 1 - (wrongnamedistortion / 100)
        title_validity = 1 - (wrongtitledistortion / 100)
        no_distortion_validity = nodistortion / 100
        high_distortion_validity = 1 - (highdistortion / 100)

        overall_validity = (
            email_validity * weights['email'] +
            date_validity * weights['date'] +
            name_validity * weights['name'] +
            title_validity * weights['title'] +
            no_distortion_validity * weights['no_distortion'] +
            high_distortion_validity * weights['high_distortion'] )*100
         