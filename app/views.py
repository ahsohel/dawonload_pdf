from django.shortcuts import render, HttpResponse

from .models import test_table

# Create your views here.
from django.db.models import Sum
def index(request):
    k = request.POST.get('start_time')
    print(k)



    f=['1','2','3','4','5','6','7','8','9','10']
    new_f=[]
    new_f_2=[]
    import random

    n = random.randint(1000, 9999)  # returns a random integer
    print("number")
    print("number")

    print(n)

    l=[1,2,3]
    o=[4,5,6]
    for i,j in enumerate (l):
        print("ii")
        print(i+1)
        print(j)

    length_1 = len(f)
    if length_1>6:
        for i in range(5):
            new_f.append(f[i])
        for i in range(5, 10):
            new_f_2.append(f[i])
    print(new_f)
    print(new_f_2)

    return render(request, 'one.html')


# start pdf code here

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.colors import Color, black, blue, red

def pdf_create(request):
    h=str(1)+".pdf"

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = ' filename="somefilename.pdf"'
    response['Content-Disposition'] = ' filename='+h

    # response['Content-Disposition'] = f'attachment; filename="{Invoice_get_ordr_tbl.Order_Id}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    k=[1,2]
    for iol in k:
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        u = test_table.objects.get(roll = iol)

        p.drawString(225, 70, str(u))

        # Close the PDF object cleanly, and we're done.
        p.showPage()


    p.save()
    return response

# end pdf code here









def new(request):
    Product_list = ['p1', 'p2', 'p3', 'p4', 'p5','p6','p7', 'p8','p9','p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17','p18','p19', 'p20','p21','p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28',

                    '1', '2', '3', '4', '5','6','7', '8','9','10',
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',

                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                    ]


    Quantity_list = ['q1', 'q2', 'q3', 'q4', 'q5','q6','q7', 'q8','q9','q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17','q18','q19', 'q20','q21','q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'


                                                                                                                                                                                                                                                            ,'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                     ]
    SubTotal_Price_list = ['1', '2', '3', '4', '5','6','7', '8','9','10', '11', '12', '13', '14', '15', '16', '17','18','19', '20','21','22', '23', '24', '25', '26', '27', '28'

                           ,'1', '2', '3', '4', '5','6','7', '8','9','10',
                           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                           ]

    new_Product_list_1 = []
    new_Product_list_2 = []
    new_Product_list_3 = []
    new_Product_list_4 = []
    new_Product_list_5 = []
    new_Product_list_6 = []

    new_Quantity_list_1 = []
    new_Quantity_list_2 = []
    new_Quantity_list_3 = []
    new_Quantity_list_4 = []
    new_Quantity_list_5 = []
    new_Quantity_list_6 = []

    new_SubTotal_Price_list_1 = []
    new_SubTotal_Price_list_2 = []
    new_SubTotal_Price_list_3 = []
    new_SubTotal_Price_list_4 = []
    new_SubTotal_Price_list_5 = []
    new_SubTotal_Price_list_6 = []



    k ='h'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f' filename="{k}.pdf"'

    p = canvas.Canvas(response)

    len_Product_list =len(Product_list)

    if len_Product_list<17:
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in Product_list:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in Quantity_list:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in SubTotal_Price_list:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response
















    elif len_Product_list > 16 and len_Product_list < 33:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, len_Product_list):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response


        print(new_Product_list_1)
        print(new_Product_list_2)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)











    elif len_Product_list > 32 and len_Product_list < 49:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()



        for i in range(34, len_Product_list):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)















    elif len_Product_list > 48 and len_Product_list < 65:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()





        for i in range(51, len_Product_list):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)


        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)














    elif len_Product_list > 64 and len_Product_list < 80:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(51, 67):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()



        for i in range(67, len_Product_list):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)
        print(new_Product_list_5)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)
        print(new_Quantity_list_5)


        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)
        print(new_SubTotal_Price_list_5)












    else:

        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(51, 67):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(67, 84):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()







        for i in range(84, len_Product_list):
            new_Product_list_6.append(Product_list[i])
            new_Quantity_list_6.append(Quantity_list[i])
            new_SubTotal_Price_list_6.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_6:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_6:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_6:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)
        print(new_Product_list_5)
        print(new_Product_list_6)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)
        print(new_Quantity_list_5)
        print(new_Quantity_list_6)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)
        print(new_SubTotal_Price_list_5)
        print(new_SubTotal_Price_list_6)

def dashboard_customer_order_edit_Generate_Invoice(request):

    invoice_subtotal_amount = "sddsd"
    invoice_Delivery_Charge = "sddsd"
    invoice_GrandTotal_Price = "sddsd"

    invoice_GrandTotal_Order = "sddsd"
    invoice_GrandTotal_date = "sddsd"
    invoice_GrandTotal_payment_method = "sddsd"

    Customer_delivery_information_first_name = "sddsd"
    Customer_delivery_information_last_name = "sddsd"
    Customer_delivery_information_full_name = "sddsd"
    Customer_delivery_information_Street_Address = "sddsd"
    Customer_delivery_information_Town_City = "sddsd"
    Customer_delivery_information_District = "sddsd"
    Customer_delivery_information_Post_Code = "sddsd"
    Customer_delivery_information_Phone_Number = "sddsd"
    Customer_delivery_information_Email_Address = "sddsd"

    Product_list = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
                    'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28',

                    '1',

                    ]

    Quantity_list = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15',
                     'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'

        , '1',

                     ]
    SubTotal_Price_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                           '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'

        , '1',

                           ]



    new_Product_list_1 = []
    new_Product_list_2 = []
    new_Product_list_3 = []
    new_Product_list_4 = []
    new_Product_list_5 = []
    new_Product_list_6 = []

    new_Quantity_list_1 = []
    new_Quantity_list_2 = []
    new_Quantity_list_3 = []
    new_Quantity_list_4 = []
    new_Quantity_list_5 = []
    new_Quantity_list_6 = []

    new_SubTotal_Price_list_1 = []
    new_SubTotal_Price_list_2 = []
    new_SubTotal_Price_list_3 = []
    new_SubTotal_Price_list_4 = []
    new_SubTotal_Price_list_5 = []
    new_SubTotal_Price_list_6 = []

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f' filename="{invoice_GrandTotal_Order}.pdf"'
    p = canvas.Canvas(response)

    len_Product_list = len(Product_list)

    if len_Product_list < 16:
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   "+str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   "+str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   "+str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   "+str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in Product_list:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in Quantity_list:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in SubTotal_Price_list:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, str(invoice_subtotal_amount))
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response



    elif len_Product_list > 15 and len_Product_list < 31:
        for i in range(0, 15):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, str(invoice_subtotal_amount))
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(15, len_Product_list):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, str(invoice_subtotal_amount))
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response



    elif len_Product_list > 30 and len_Product_list < 46:
        for i in range(0, 15):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(15, 30):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(30, len_Product_list):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response



    elif len_Product_list > 45 and len_Product_list < 61:
        for i in range(0, 15):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(15, 30):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(30, 45):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(45, len_Product_list):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response



    elif len_Product_list > 60 and len_Product_list < 76:
        for i in range(0, 15):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(15, 30):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(30, 45):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(45, 60):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(60, len_Product_list):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)
        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response


    else:

        for i in range(0, 15):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(15, 30):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(30, 45):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(45, 60):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(60, 75):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)
        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")


        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")
        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")
        p.drawString(225, 15, "WWW.boomboom.com.bd")
        p.line(0, 60, 600, 60)
        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(75, len_Product_list):
            new_Product_list_6.append(Product_list[i])
            new_Quantity_list_6.append(Quantity_list[i])
            new_SubTotal_Price_list_6.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)

        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)

        p.drawString(300, 630, "Order:   " + str(invoice_GrandTotal_Order))
        p.drawString(300, 614, "Date:   " + str(invoice_GrandTotal_date))
        p.drawString(300, 600, "Payment   " + str(invoice_GrandTotal_payment_method[0:39]))
        p.drawString(300, 588, "Method:   " + str(invoice_GrandTotal_payment_method[39:]))

        p.drawString(40, 630, str(Customer_delivery_information_full_name))
        p.drawString(40, 618, str(Customer_delivery_information_Street_Address))
        p.drawString(40, 606, str(Customer_delivery_information_Town_City))
        p.drawString(40, 594, str(Customer_delivery_information_District))
        p.drawString(40, 582, str(Customer_delivery_information_Post_Code))
        p.drawString(40, 570, str(Customer_delivery_information_Phone_Number))
        p.drawString(40, 558, str(Customer_delivery_information_Email_Address))

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        position_Product_list = 490
        for r in new_Product_list_6:
            p.drawString(70, position_Product_list, str(r))
            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_6:
            p.drawString(300, position_Quantity_list, str(r))
            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_6:
            p.drawString(450, position_SubTotal_Price_list, str(r))
            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response












































































#//////////////////////////////////////////////////////////////////////////////////////////////
def making_for_get_single_pdf_by_sohel(a, b, c):
    k = 'h'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f' filename="{k}.pdf"'

    p = canvas.Canvas(response)


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawString((+)left, (+)Top, "Hello world.")
    p.drawString(320, 780, "Boom Boom Shopping")
    p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
    p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
    p.drawString(320, 735, "Phone : 09642601538")
    p.drawString(320, 720, "Mail: support@boomboom.com.bd")

    i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
    p.drawImage(i, 40, 730, width=270, height=72)
    u = 'kkk'
    p.setFont("Helvetica", 25)
    p.drawString(40, 655, "INVOICE")
    p.setFont("Helvetica", 12)
    p.drawString(300, 630, "Order:" + u)
    p.drawString(300, 618, "Date:")
    p.drawString(300, 606, "Payment:")
    p.drawString(300, 594, "Method:")

    p.drawString(40, 630, "Method:")
    p.drawString(40, 618, "Method:")
    p.drawString(40, 606, "Method:")
    p.drawString(40, 594, "Method:")
    p.drawString(40, 582, "Method:")
    p.drawString(40, 570, "Method:")

    # color(r,g,b, alpha)
    red50transparent = Color(0, 0, 205, alpha=0.2)
    Yellow = Color(205, 205, 0, alpha=1)
    p.setFillColor(Yellow)
    p.rect(40, 510, 520, 30, fill=True, stroke=False)

    p.setFillColor(black)
    p.drawString(70, 520, "Product")
    p.setFillColor(black)
    p.drawString(300, 520, "Quantity")
    p.setFillColor(black)
    p.drawString(450, 520, "Price")

    print("Invoice_filter_ordr_tbl_2")
    print("Invoice_filter_ordr_tbl_2")



    position_Product_list = 490
    for r in a:
        p.drawString(70, position_Product_list, str(r))

        position_Product_list = position_Product_list - 20

    position_Quantity_list = 490
    for r in b:
        p.drawString(300, position_Quantity_list, str(r))

        position_Quantity_list = position_Quantity_list - 20

    position_SubTotal_Price_list = 490
    for r in c:
        p.drawString(450, position_SubTotal_Price_list, str(r))

        position_SubTotal_Price_list = position_SubTotal_Price_list - 20

    line_position_Quantity_list = position_Quantity_list + 15
    p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
    p.drawString(300, position_Quantity_list, "subtotal")
    position_Quantity_list = position_Quantity_list - 20
    p.drawString(300, position_Quantity_list, "shipping")
    position_Quantity_list = position_Quantity_list - 20
    line_position_Quantity_list = position_Quantity_list + 15
    p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
    p.drawString(300, position_Quantity_list, "Total")

    p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
    position_SubTotal_Price_list = position_SubTotal_Price_list - 20
    p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
    position_SubTotal_Price_list = position_SubTotal_Price_list - 20
    p.drawString(450, position_Quantity_list, "Total amount")

    p.drawString(225, 15, "WWW.boomboom.com.bd")

    p.line(0, 60, 600, 60)

    p.setFillColor(blue)
    p.drawString(190, 45, "Thank you for shopping with BoomBoom")
    p.drawString(241, 30, "We Deliver Quality")
    p.drawString(225, 15, "WWW.boomboom.com.bd")

    # Close the PDF object cleanly, and we're done.
    p.showPage()

    print("opora")
    return response






def new_1(request):
    Product_list = ['p1', 'p2', 'p3', 'p4', 'p5','p6','p7', 'p8','p9','p10']#, 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17','p18','p19', 'p20','p21','p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28',

                    # '1', '2', '3', '4', '5','6','7', '8','9','10',
                    # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',

                    # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                    # ]


    Quantity_list = ['q1', 'q2', 'q3', 'q4', 'q5','q6','q7', 'q8','q9','q10'#, 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17','q18','q19', 'q20','q21','q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'


                                                                                                                                                                                                                                                            # ,'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                     # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                     # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                     ]
    SubTotal_Price_list = ['1', '2', '3', '4', '5','6','7', '8','9','10'#, '11', '12', '13', '14', '15', '16', '17','18','19', '20','21','22', '23', '24', '25', '26', '27', '28'

                           # ,'1', '2', '3', '4', '5','6','7', '8','9','10',
                           # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           # '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',



                           ]

    new_Product_list_1 = []
    new_Product_list_2 = []
    new_Product_list_3 = []
    new_Product_list_4 = []
    new_Product_list_5 = []
    new_Product_list_6 = []

    new_Quantity_list_1 = []
    new_Quantity_list_2 = []
    new_Quantity_list_3 = []
    new_Quantity_list_4 = []
    new_Quantity_list_5 = []
    new_Quantity_list_6 = []

    new_SubTotal_Price_list_1 = []
    new_SubTotal_Price_list_2 = []
    new_SubTotal_Price_list_3 = []
    new_SubTotal_Price_list_4 = []
    new_SubTotal_Price_list_5 = []
    new_SubTotal_Price_list_6 = []

    k = 'h'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f' filename="{k}.pdf"'

    p = canvas.Canvas(response)


    len_Product_list =len(Product_list)

    if len_Product_list<17:
        making_for_get_single_pdf_by_sohel(Product_list, Quantity_list, SubTotal_Price_list)


        print("necha")

        p.save()
        return response

















    elif len_Product_list > 16 and len_Product_list < 33:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, len_Product_list):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response


        print(new_Product_list_1)
        print(new_Product_list_2)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)











    elif len_Product_list > 32 and len_Product_list < 49:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()



        for i in range(34, len_Product_list):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)















    elif len_Product_list > 48 and len_Product_list < 65:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()


        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()





        for i in range(51, len_Product_list):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)


        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)














    elif len_Product_list > 64 and len_Product_list < 80:
        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(51, 67):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()



        for i in range(67, len_Product_list):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)
        print(new_Product_list_5)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)
        print(new_Quantity_list_5)


        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)
        print(new_SubTotal_Price_list_5)












    else:

        for i in range(0, 17):
            new_Product_list_1.append(Product_list[i])
            new_Quantity_list_1.append(Quantity_list[i])
            new_SubTotal_Price_list_1.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_1:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_1:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_1:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(17, 34):
            new_Product_list_2.append(Product_list[i])
            new_Quantity_list_2.append(Quantity_list[i])
            new_SubTotal_Price_list_2.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_2:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_2:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_2:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(34, 51):
            new_Product_list_3.append(Product_list[i])
            new_Quantity_list_3.append(Quantity_list[i])
            new_SubTotal_Price_list_3.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_3:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_3:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_3:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(51, 67):
            new_Product_list_4.append(Product_list[i])
            new_Quantity_list_4.append(Quantity_list[i])
            new_SubTotal_Price_list_4.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_4:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_4:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_4:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        for i in range(67, 84):
            new_Product_list_5.append(Product_list[i])
            new_Quantity_list_5.append(Quantity_list[i])
            new_SubTotal_Price_list_5.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_5:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_5:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_5:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()







        for i in range(84, len_Product_list):
            new_Product_list_6.append(Product_list[i])
            new_Quantity_list_6.append(Quantity_list[i])
            new_SubTotal_Price_list_6.append(SubTotal_Price_list[i])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString((+)left, (+)Top, "Hello world.")
        p.drawString(320, 780, "Boom Boom Shopping")
        p.drawString(320, 765, "House-11, Road-18, Flat-6E, Sector-04")
        p.drawString(320, 750, "Uttara, Dhaka-1230, Bangladesh")
        p.drawString(320, 735, "Phone : 09642601538")
        p.drawString(320, 720, "Mail: support@boomboom.com.bd")

        i = 'https://www.seekpng.com/png/full/301-3018897_logos-15-png-logo-creator-online-for-free.png'
        p.drawImage(i, 40, 730, width=270, height=72)
        u = 'kkk'
        p.setFont("Helvetica", 25)
        p.drawString(40, 655, "INVOICE")
        p.setFont("Helvetica", 12)
        p.drawString(300, 630, "Order:" + u)
        p.drawString(300, 618, "Date:")
        p.drawString(300, 606, "Payment:")
        p.drawString(300, 594, "Method:")

        p.drawString(40, 630, "Method:")
        p.drawString(40, 618, "Method:")
        p.drawString(40, 606, "Method:")
        p.drawString(40, 594, "Method:")
        p.drawString(40, 582, "Method:")
        p.drawString(40, 570, "Method:")

        # color(r,g,b, alpha)
        red50transparent = Color(0, 0, 205, alpha=0.2)
        Yellow = Color(205, 205, 0, alpha=1)
        p.setFillColor(Yellow)
        p.rect(40, 510, 520, 30, fill=True, stroke=False)

        p.setFillColor(black)
        p.drawString(70, 520, "Product")
        p.setFillColor(black)
        p.drawString(300, 520, "Quantity")
        p.setFillColor(black)
        p.drawString(450, 520, "Price")

        print("Invoice_filter_ordr_tbl_2")
        print("Invoice_filter_ordr_tbl_2")

        print("Product_list")
        print(Product_list)

        position_Product_list = 490
        for r in new_Product_list_6:
            p.drawString(70, position_Product_list, str(r))

            position_Product_list = position_Product_list - 20

        position_Quantity_list = 490
        for r in new_Quantity_list_6:
            p.drawString(300, position_Quantity_list, str(r))

            position_Quantity_list = position_Quantity_list - 20

        position_SubTotal_Price_list = 490
        for r in new_SubTotal_Price_list_6:
            p.drawString(450, position_SubTotal_Price_list, str(r))

            position_SubTotal_Price_list = position_SubTotal_Price_list - 20

        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "subtotal")
        position_Quantity_list = position_Quantity_list - 20
        p.drawString(300, position_Quantity_list, "shipping")
        position_Quantity_list = position_Quantity_list - 20
        line_position_Quantity_list = position_Quantity_list + 15
        p.line(250, line_position_Quantity_list, 600, line_position_Quantity_list)
        p.drawString(300, position_Quantity_list, "Total")

        p.drawString(450, position_SubTotal_Price_list, "subtotal amount")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_SubTotal_Price_list, "Invoice_get_ordr_tbl.Shopping")
        position_SubTotal_Price_list = position_SubTotal_Price_list - 20
        p.drawString(450, position_Quantity_list, "Total amount")

        p.drawString(225, 15, "WWW.boomboom.com.bd")

        p.line(0, 60, 600, 60)

        p.setFillColor(blue)
        p.drawString(190, 45, "Thank you for shopping with BoomBoom")
        p.drawString(241, 30, "We Deliver Quality")
        p.drawString(225, 15, "WWW.boomboom.com.bd")

        # Close the PDF object cleanly, and we're done.
        p.showPage()

        p.save()
        return response

        print(new_Product_list_1)
        print(new_Product_list_2)
        print(new_Product_list_3)
        print(new_Product_list_4)
        print(new_Product_list_5)
        print(new_Product_list_6)

        print(new_Quantity_list_1)
        print(new_Quantity_list_2)
        print(new_Quantity_list_3)
        print(new_Quantity_list_4)
        print(new_Quantity_list_5)
        print(new_Quantity_list_6)

        print(new_SubTotal_Price_list_1)
        print(new_SubTotal_Price_list_2)
        print(new_SubTotal_Price_list_3)
        print(new_SubTotal_Price_list_4)
        print(new_SubTotal_Price_list_5)
        print(new_SubTotal_Price_list_6)

