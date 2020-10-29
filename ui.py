from tkinter import *

#Main Window
root=Tk()

root.title("WoT Randomizer")
root.geometry("700x500")


#Select Tiers
mylabel1=Label(root, text="Select Tiers of Tanks you want to play")

mylabel1.grid(row=0, column=0, columnspan=3)

tier5=IntVar()

c5=Checkbutton(root, text="Tier V", variable=tier5)

tier6=IntVar()

c6=Checkbutton(root, text="Tier VI", variable=tier6)

tier7=IntVar()

c7=Checkbutton(root, text="Tier VII", variable=tier7)

tier8=IntVar()

c8=Checkbutton(root, text="Tier VIII", variable=tier8)

tier9=IntVar()

c9=Checkbutton(root, text="Tier IX", variable=tier9)

tier10=IntVar()

c10=Checkbutton(root, text="Tier X", variable=tier10)

c5.grid(row=1, column=0)
c6.grid(row=1, column=1)
c7.grid(row=1, column=2)
c8.grid(row=1, column=3)
c9.grid(row=1, column=4)
c10.grid(row=1, column=5)

#Select Nations

mylabel2=Label(root, text="    Select Nations of Tanks you want to play")

mylabel2.grid(row=4, column=0, columnspan=3)


china=IntVar()

ch=Checkbutton(root, text="Chinese", variable=china)

france=IntVar()

fr=Checkbutton(root, text="French", variable=france)

germany=IntVar()

ge=Checkbutton(root, text="German", variable=germany)

japan=IntVar()

jp=Checkbutton(root, text="Japanese", variable=japan)

sweden=IntVar()

sw=Checkbutton(root, text="Swedish", variable=sweden)

unitedk=IntVar()

uk=Checkbutton(root, text="British", variable=unitedk)

uniteds=IntVar()

us=Checkbutton(root, text="American", variable=uniteds)

ussr=IntVar()

ru=Checkbutton(root, text="Russian", variable=ussr)

czech=IntVar()

cz=Checkbutton(root, text="Czech", variable=czech)

italy=IntVar()

it=Checkbutton(root, text="Italian", variable=italy)

poland=IntVar()

pl=Checkbutton(root, text="Polish", variable=poland)

ch.grid(row=5, column=0)
fr.grid(row=5, column=1)
ge.grid(row=5, column=2)
jp.grid(row=5, column=3)
sw.grid(row=5, column=4)
uk.grid(row=5, column=5)
us.grid(row=6, column=0)
ru.grid(row=6, column=1)
cz.grid(row=6, column=2)
it.grid(row=6, column=3)
pl.grid(row=6, column=4)


#Types of tanks

mylabel3=Label(root, text="Select Types of Tanks you want to play")

mylabel3.grid(row=8, column=0, columnspan=3)

lights=IntVar()

lt=Checkbutton(root, text="Lights", variable=lights)

mediums=IntVar()

med=Checkbutton(root, text="Mediums", variable=mediums)

heavies=IntVar()

ht=Checkbutton(root, text="Heavies", variable=heavies)

tankdestroyers=IntVar()

td=Checkbutton(root, text="Tank Destroyers", variable=tankdestroyers)

artillery=IntVar()

arty=Checkbutton(root, text="Artillery(DansGame)", variable=artillery)

lt.grid(row=9, column=0)
med.grid(row=9, column=1)
ht.grid(row=9, column=2)
td.grid(row=9, column=3)
arty.grid(row=9, column=4)

root.mainloop()