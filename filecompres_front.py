from tkinter import *
import huffman as hf
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
def choosefile():
	global file,choosenfile
	file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
	print(file)
	choosenfile.set(file)
def compressfile():
	if file!=None:
		newfilename="file"+".z"
		value=hf.HuffmanCoding(file)
		outputpath=value.compress()
		print(outputpath)
		showinfo("Output path",outputpath)
def decompressfile():
	if file!=None:
		newfilename=file+".txt"
		value=hf.HuffmanCoding(file)
		outputpath=value.compress()
		output1=value.decompress(outputpath)
		print(output1)
		showinfo("Decompress file",outputpath )
if __name__=='__main__':
	root=Tk()
	root.title("File compression")
	root.geometry("644x288")
	file=None
	button1=Button(root,text="choose a file",command=choosefile)
	button1.pack()
	choosenfile=StringVar()
	file_choose=Entry(root,textvariable=choosenfile)
	file_choose.pack()
	button2=Button(root,text="compress this selected file ",command=compressfile)
	button2.pack()
	button3=Button(root,text="Decompress this file ",command=decompressfile)
	button4=Button(root,text="Leave",command=quit)
	button3.pack()
	button4.pack()
	root.mainloop()