# import tkinter and create an object of it
from tkinter import *
from tkinter import messagebox
window = Tk()

# Set the title, size, and color of the window
window.title(" ES IP Address Calculator ")
window.geometry("400x400")
window.configure(bg=("light blue"))
window.maxsize(350, 350)
window.minsize(200, 200)  # (69, 420)

# create the menu bar
my_menu = Menu(window)
window.config(menu=my_menu)

# menu command
def menu_command():
    pass

# create the file menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="BMI Calculator", command=menu_command)
file_menu.add_command(label="Currency Converter", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

#about popup
def about_popup():
    messagebox.showinfo("About", "Eyo Sam IP Address Calculator is a system that helps automate the process of IP subnet calculation")

#contact popup
def contact_popup():
    messagebox.showinfo("Contact", "You can contact the developer directly on eyosam97@gmail.com or +2348118171616")

# create the help menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_popup)
help_menu.add_command(label="Contact", command=contact_popup)

# IP_Error popup
def ip_error_popup():
    messagebox.showerror("Error", "Invalid IP, retry")

# Subnet_Error popup
def subnet_error_popup():
    messagebox.showerror("Error", "Invalid Subnet Mask, retry")

try:
    # Prompt for IP Address
    ip_addr = Label(window, text=" IP Address ", bg="light blue")
    ip_addr.place(x=35, y=10)

    # Entry for IP Address
    ip_addr_entry = Entry(window, )
    ip_addr_entry.place(x=35, y=35)

    # IP_Validation Function
    def ip_validattion():
        while True:

            # Validate the IP
            octet_ip = ip_addr_entry.split(".")
            #print octet_ip
            int_octet_ip = [int(i) for i in octet_ip]

            if (len(int_octet_ip) == 4) and \
                    (int_octet_ip[0] != 127) and \
                    (int_octet_ip[0] != 169) and \
                    (0 <= int_octet_ip[1] <= 255) and \
                    (0 <= int_octet_ip[2] <=255) and \
                    (0 <= int_octet_ip[3] <= 255):
                break
            else:
                ip_error_popup()
                continue
    # Prompt for Subnet Mask
    subnet_mask = Label(window, text=" Subnet Mask ", bg="light blue")
    subnet_mask.place(x=35, y=55)

    # Entry for Subnet Mask
    subnet_mask_entry = Entry(window)
    subnet_mask_entry.place(x=35, y=75)

    # Subnet_Mask_Validation Function
    def subnet_mask_validation():
        # Predefine possible subnet masks
        masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        while True:

            # Validate the subnet mask
            octet_subnet = [int(j) for j in subnet_mask_entry.split(".")]
            # print octet_subnet
            if (len(octet_subnet) == 4) and \
                    (octet_subnet[0] == 255) and \
                    (octet_subnet[1] in masks) and \
                    (octet_subnet[2] in masks) and \
                    (octet_subnet[3] in masks) and \
                    (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
                break
            else:
                subnet_error_popup()
                continue

    # Calculate Button
    c_button = Button(window, text = " Calculate ", command = lambda:[ip_validattion(), subnet_mask_validation()])
    c_button.place(x = 110, y = 100)

except KeyboardInterrupt:
    print ("Interrupted by the User, exiting\n")
except ValueError:
    print ("Seem to have entered an incorrect value, exiting\n")





window.mainloop()
