#python 3.6 only because of fpdf
from fpdf import FPDF
import pyqrcode
import time



#arguments
order = {
"name":"a very long order name, to check how it would behave if the sting is very long", "code":"0001"
}

part = {
"name":"part name, long in text - Pavadinimas: Rėmas viršutinis", "code":"2462.11.00","order_quantity":1000
}

operations = [
{"name":"Miltelinis dažymas RAL7035-1", "workstation":"Montavimo barai", "qr_code":"1178671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-2", "workstation":"Montavimo barai", "qr_code":"1278671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-3", "workstation":"Montavimo barai", "qr_code":"1378671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-4", "workstation":"Montavimo barai", "qr_code":"1478671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-5", "workstation":"Montavimo barai", "qr_code":"1578671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-7", "workstation":"Montavimo barai", "qr_code":"7-7d01f-53b7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-8", "workstation":"Montavimo barai", "qr_code":"8678671d3-7d01-53fb7-ba25-db10b5aac7ab"},
{"name":"Miltelinis dažymas RAL7035-9", "workstation":"Montavimo barai", "qr_code":"9678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-10", "workstation":"Montavimo barai", "qr_code":"10678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-11", "workstation":"Montavimo barai", "qr_code":"11678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-12", "workstation":"Montavimo barai", "qr_code":"12678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-13", "workstation":"Montavimo barai", "qr_code":"13678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-14", "workstation":"Montavimo barai", "qr_code":"14678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-15", "workstation":"Montavimo barai", "qr_code":"15678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-6", "workstation":"Montavimo barai", "qr_code":"1678671d3-7d01-53b7-ba25-db10b5ac7abf"},
{"name":"Miltelinis dažymas RAL7035-7", "workstation":"Montavimo barai", "qr_code":"1778671d3-7d01-5f3b7-ba25-db10b5aac7ab"}
]
#it's function. yep.

def createpdf(order,part,operations):
    #that's the function to make qr code images to folder qrimages:
    def qrcodemake(inputqr,i):
        qr = pyqrcode.create(inputqr)
        qr.png('./qrimages/filename'+ str(i) +'.png', scale=10)


#header and footer can be removed
    class PDF(FPDF):
        def header(self):

            self.set_font('DejaVu', '', 9)
            #the title string
            title_order = 'Užsakymo pavadinimas: '+ order["name"] + "\n" + "Užsakymo kodas: " + order["code"]
            self.multi_cell(190, 5, title_order, 1, 1, 'C')
            
            result = time.localtime()
            if result.tm_min < 10:
                minutes = '0' +str(result.tm_min)
            else:
                minutes = str(result.tm_min)
            timer = str(result.tm_year) + "-" + str(result.tm_mon)+"-"+ str(result.tm_mday) +'  '+ str(result.tm_hour) +':'+ minutes
            
            self.set_font('DejaVu', 'B', 11)
            title_part = 'Pavadinimas: '+ part["name"] + "\n" + "Kodas: " + part["code"] + "\n" + 'Kiekis: ' + str(part["order_quantity"])

            self.multi_cell(190, 5, title_part, 1, 1, 'R')
            self.cell(320, -10, timer, 0, 1, 'C')
            self.cell(180, 10, '', 0, 1, 'C') #placeholder to align raws of 'operations' below
            

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            self.set_font('DejaVu', '', 9)
            self.cell(0, 0, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # Instantiation of inherited class
    pdf = PDF()


    #add fonts to support signs
    #Italian is supported- others non latin- no, need more (or other) font imports in that case.
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
    pdf.set_font('DejaVu', '', 10)


    pdf.alias_nb_pages()
    pdf.add_page()



    for i in range(0,len(operations)):
        pdf.cell(80, 15, operations[i]["name"], 'T', 0)
        pdf.cell(80, 15, operations[i]["workstation"], 'T', 0, 'L')
        
        qrcodemake(operations[i]["qr_code"],i)
        image = ('./qrimages/filename'+str(i)+'.png')
        pdf.image(image, x = None, y = None, w = 17, h = 17, type = '', link = '') #w and h of the qr code in mm
        pdf.cell(0, 0, '', 0, 1, 'L')
    pdf.output('print.pdf', 'F') #output can be changed to byte string here- 'F' to 'S'

#run
createpdf(order,part,operations)