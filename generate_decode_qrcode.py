import qrcode
import cv2
# Function to generate QR code
def gent_qr_cd(input_cont,output_file,fill_color):
        #create QR code with parameters
        QR = qrcode.QRCode(version=5,   
                border=10, 
                box_size=20, #size of each box in QR code
                error_correction=qrcode.constants.ERROR_CORRECT_H ) # Error correction level
        
        QR.add_data(input_cont) # add input data
        QR.make(fit=True)       # create QR code and adjusted version size.
        qr_img = QR.make_image(back_color="white",fill_color=fill_color) # generate QR code with specified fill color
        qr_img.save(output_file)  #save the image file

# function to decode the QR code
def decode_qr_cd(image_path):
        img = cv2.imread(image_path) #read the image that have QR code inside the image
        detector = cv2.QRCodeDetector()
        decoded_text , bounding_box , _  = detector.detectAndDecode(img) #detec & decode QR code
        return decoded_text  # return decoded data/content

def main():
        # loop to generate and decode QR code
        while True:
               # user input for QR code generation
               input_cont = input("Enter the data to encode : ")
               output_file = input("Enter the filename to save with extention(ex-png,JPG) :")
               fill_color = input("Enter the fill color for QR code :")
               print("QR Code generated!")

               gent_qr_cd(input_cont,output_file,fill_color) # generate Qr code and save image.
                  
               # prompt user to decode QR code
               QRdecode_choice=input("Do you want to decode QR code(Y/N) ? :").upper()
               if QRdecode_choice == "Y":
                       image_path = input("Enter the path to QRCode image :")
                        # decode QR code and print decoded data
                       decoded_data = decode_qr_cd(image_path) 
                       if decoded_data:
                          print("The Decoded data is :", decoded_data)
                       else:
                          print("Failed to decode the QR code.")
               else:
                    print("Quit")
                # prompt user to generate another QR code    
               another=input("Do you want to generate another QR code(Y/N)?:").upper()
               if another !="Y":
                     print("existing..!")
                     break

main() # call the main function to start the code/program.
