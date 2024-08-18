#importing modules
from tkinter import * #type:ignore
from tkinter.filedialog import * #type:ignore
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox
# decoding the file
def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.title("Decode- Kunwar")
    DecScreen.geometry("500x500+300+300")
    DecScreen.config(bg="pink")

    def OpenFile():
        global FileOpen
        FileOpen = askopenfilename(initialdir="/Desktop", title="Select the File", filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))
        if FileOpen:
            label_file_selected.config(text=f"File selected: {FileOpen}")

    def Decoder():
        try:
            if not FileOpen:
                messagebox.showerror("Error", "No file selected")
                return
            Message = stg.reveal(FileOpen)
            if Message:
                label3 = Label(text=Message.decode())
                label3.place(relx=0.3, rely=0.3)
            else:
                messagebox.showerror("Error", "No hidden message found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    SelectButton = Button(text="Select the file", command=OpenFile)
    SelectButton.place(relx=0.1, rely=0.4)

    label_file_selected = Label(text="No file selected")
    label_file_selected.place(relx=0.1, rely=0.5)

    EncodeButton = Button(text="Decode", command=Decoder)
    EncodeButton.place(relx=0.1, rely=0.6)
#encoding the file
def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode- Kunwar")
    EncScreen.geometry("500x500+300+300")
    EncScreen.config(bg="yellow")
    label = Label(text="Confidential Message")
    label.place(relx=0.1,rely=0.2)
    entry=Entry()
    entry.place(relx=0.5,rely=0.2)
    label1 = Label(text="Name of the File")
    label1.place(relx=0.1,rely=0.3)
    SaveEntry = Entry()
    SaveEntry.place(relx=0.5,rely=0.3)

    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.3,rely=0.3)

    def Encoder():
        Response= messagebox.askyesno("PopUp","Do you want to encode the image?")
        if Response == 1:
            stg.hide(FileOpen,SaveEntry.get()+".jpg",entry.get())
            messagebox.showinfo("Pop Up","Successfully Encoded")
        else:
            messagebox.showwarning("Pop Up","Unsuccessful, please try again")

    SelectButton = Button(text="Select the file",command=OpenFile)
    SelectButton.place(relx=0.1,rely=0.4)
    EncodeButton=Button(text="Encode",command=Encoder)
    EncodeButton.place(relx=0.4,rely=0.5)
#Initializing the screen
Screen = Tk()
Screen.title("Image Steganography by - Kunwar ")
Screen.geometry("500x500+300+300")
Screen.config(bg= "blue")
#creating buttons
EncodeButton = Button(text="Encode",command=Encode)
EncodeButton.place(relx=0.3,rely=0.4)

DecodeButton = Button(text="Decode",command=Decode)
DecodeButton.place(relx=0.6,rely=0.4)

mainloop()