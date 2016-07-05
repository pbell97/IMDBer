import urllib2
import Tkinter
import csv
do1 = False
movieEdits = open('movieEdits.txt', 'a')



#Getting Title
def getTitle():
	global do1; global title;
	f.seek(0)
	for line in f:
		if do1 == True:
			title = line
			do1 = False
			break
		if 'Title:' in line:
			do1 = True
	title = title[:-10]
	title = title[24:len(title)]
	print title

#Getting Date
def getDate():
	global do1; global title; global date;
	f.seek(0)
	for line in f:
		if do1 == True:
			date = line
			do1 = False		
			break
		if ('<strong>' + title + '</strong>') in line:
			do1 = True
	date = date[:-2]
	date = date[17:len(date)]
	print date

#Getting Rating
def getRating():
	global do1; global rating;
	f.seek(0)
	for line in f:
		if '="G"' in line:
			rating = "G"
		if '"PG"' in line:
			rating = "PG"
		if "PG-13" in line:
			rating = "PG-13"
		if '="R"' in line:
			rating = "R"
	print rating

#Getting Run Time
def getRuntime():
	global do1; global f; global movieEdits; global title; global date; global rating; global runtime;
	f.seek(0)
	for line in f:
		if do1 == True:
			runtime = line
			do1 = False		
			break
		if ('<span class="ghost">|</span>                    <time') in line:
			do1 = True
	runtime = runtime[24:len(runtime)]
	print runtime
	textToWrite = ("\n%s %s %s %s\n" % (title, date, rating, runtime))
	print textToWrite
	movieEdits.write(textToWrite)
	f.close()

def writeDVD():
	global title; global date; global rating; global runtime;
	DVDnum = field2.get(); field2.delete(0, len(DVDnum));
	xin = open('DVDMOVIES.CSV', 'rb')
	dvdin = csv.reader(xin)
	tempList = []			
	for row in dvdin:			#Stores entire DVDMOVIES to tempList, then closes
		tempList.append(row)
	xin.close()
	yout = open('DVDMOVIES.CSV', 'wb')		#Re-opens DVDMOVIES but in write mode
	dvdout = csv.writer(yout)
	for row in tempList:					#Rewrites DVDMOVIES, but makes edits
		if row[1] == DVDnum:
			row[0] = title
			row[2] = date
			row[3] = rating
			row[4] = runtime
		dvdout.writerow(row)
	yout.close()
	
#Supply URL
def getURL():
	global f;
	myurl = field.get()
	field.delete( 0, len(myurl))
	myText = urllib2.urlopen(myurl).read()
	f = open('newSite.txt', 'w+')
	f.write(myText)	
	getTitle();getDate();getRating();getRuntime();writeDVD();
	
	
	
	
#Supply URL v2
def getURL2():
	global f;
	root = Tkinter.Tk()
	myurl = root.clipboard_get()
	root.destroy()
	myText = urllib2.urlopen(myurl).read()
	f = open('newSite.txt', 'w+')
	f.write(myText)	
	getTitle();getDate();getRating();getRuntime();writeDVD();
	


window = Tkinter.Tk()
label1 = Tkinter.Label(text = "Please enter the IMDB URL"); label1.pack(side = 'top', pady = 8)
button2 = Tkinter.Button(text = "Copied URL", command = getURL2); button2.pack(side = 'bottom',padx = 5, pady = 5)
field = Tkinter.Entry(); field.pack(side = 'left',padx = 5, pady = 5)
field2 = Tkinter.Entry(); field2.pack(side = 'right', padx = 10, pady = 10, )
button1 = Tkinter.Button(text = "Sumbit URL", command = getURL); button1.pack(side = 'bottom',padx = 5, pady = 5)
window.mainloop()

movieEdits.close()




