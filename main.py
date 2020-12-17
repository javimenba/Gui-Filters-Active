
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtCore import QSize, pyqtSlot, QTimer
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import math
import sympy
from PIL import ImageTk, Image
from scipy import signal
import matplotlib.pyplot as plt
from sympy import *
from os import remove
from os import path


class Window_main(QMainWindow):
    def __init__(self):
        super(Window_main, self).__init__()
        loadUi('.app/app.ui',self)
        self.list.clicked.connect( self.list_clicked)
        self.button_go.clicked.connect( self.ButtonGo)

    def list_clicked(self):
        item = self.list.currentItem()
        self.text_init.setText( str( item.text() ) )
    def ButtonGo(self):
        self.hide()
        value = self.list.currentRow()
        if value == 0:
            fpb=Window_Fpb(self)
            fpb.show()
        elif value == 1:
            fpb=Window_FpbOSK(self)
            fpb.show()
        elif value == 2:
            fpb=Window_FpaOSK(self)
            fpb.show()
        elif value == 3:
            fpb=Window_FpOSK(self)
            fpb.show()
        elif value == 4:
            fpb=Window_Fpaso(self)
            fpb.show()
        elif value ==5:
            fpb=Window_Fpbso(self)
            fpb.show()
        elif value==6:
            fpb=Window_Fbso(self)
            fpb.show()
        elif value==7:
            fpb=Window_Fprbso(self)
            fpb.show()
<<<<<<< HEAD
        elif value==8:
            fpb=Window_Fpb2opa(self)
            fpb.show()
        elif value==9:
             fpb=Window_fpa2opa(self)
             fpb.show()
        elif value==10:
             fpb=Window_fpbb2opa(self)
             fpb.show()
=======
>>>>>>> fdbf36a8963d572904770d5d91542d29f556a9f0
        else :
            print( "chale carnal" )




class Window_Fpb(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fpb, self).__init__(parent)
        loadUi('.app/fpb.ui',self)
        #Menu plot
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        #iconG
        circuit=QPixmap(".img/fpb.png")
        ecuation_fb=QPixmap(".img/fc_fpb.png")
        self.IMAGE.setPixmap(circuit)
        self.labelFT.setPixmap(ecuation_fb)
        self.editFc.setPlaceholderText( "1x10^n ==> 1e(n)" )
        self.editC.setPlaceholderText( "1x10^n ==> 1e(n)" )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows)
        self.fpb_Button_Calcular.clicked.connect(self.Calcular_fpb)
    def Calcular_fpb(self):


        fc_fpb = self.editFc.text()
        c_fpb = self.editC.text()
        resultado = 1/(float(fc_fpb)*float(c_fpb))
        ans_string = '{0:0.2f}'.format(resultado)
        self.labelRfpb.setText(ans_string)
        numerator = 1 / (float(c_fpb) * float(resultado))
        bode = signal.TransferFunction( [float( numerator )], [1, float( numerator )] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        #plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx(w, mag)
        self.bode.add_subplot( 2, 1, 2)
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def Open_Windows(self):
        if path.exists('icon.png'):
            remove('icon.png')
        self.parent().show()
        self.close()

class Window_FpbOSK(QMainWindow):
    def __init__(self, parent=None):
        super(Window_FpbOSK, self).__init__(parent)
        loadUi('.app/pbsk.ui',self)
        circuit=QPixmap(".img/fpbSK.png")
        self.Fimg.setPixmap(circuit)
        #Menu plot
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows)
        self.fpb_Button_Calcular.clicked.connect( self.Calcular)
        self.ComboBox.currentIndexChanged.connect( self.ComboSelect)
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector )
        self.selectResistor.currentIndexChanged.connect( self.RSelector )
        self.selectResistorA.currentIndexChanged.connect( self.RASelector )
        self.selectResistorB.currentIndexChanged.connect( self.RBSelector )
        self.selectCapacitor2.currentIndexChanged.connect( self.C2Selector )
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def ComboSelect(self):
        global Q, K
        value = self.ComboBox.currentIndex()
        if value ==0:
            Q=0.7071
            K=1.0000
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==1:
            Q=0.7247
            K=0.9774
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==2:
            Q=0.7673
            K=0.9368
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==3:
            Q=0.8093
            K=0.9098
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==4:
            Q=0.8638
            K=0.886
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==5:
            Q=0.9564
            K=0.8623
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==6:
            Q=0.5771
            K=1.2754
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global c
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            c = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            c = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            c = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            c = float(c1)*1e-3


    def Calcular(self):
        global r, ra, RB, C2, Ba, ba
        A = self.ganancia.text()
        if int(A)==1:
            ra = 0
        m1n = 1 + sqrt(1 + (8*(float(Q)**2)*(float(A)-1)))
        m1d = 4*float(Q)
        if m1d == 0:
            self.factorM.setText( "Infinity" )
        else:
            m1 = float(m1n)/float(m1d)
            m = '{0:0.11f}'.format( m1 )
            self.factorM.setText(m)
        rn= 1
        rd = (2 * (math.pi) * float(K) * float(f) * float(m1) * float(c))
        if rd==0:
            self.resistor.setText( "Infinity" )
        else:
            r=float(rn)/float(rd)
            R = '{0:0.11f}'.format( r )
            self.resistor.setText( R )
        raN= (2*float(A)*float(r))
        raD = (float(A)-1)
        if raD == 0:
            self.resistorA.setText("Infinity")
            ra =0
        else:
            ra = float(raN)/float(raD)
            Ra = '{0:0.11f}'.format(ra)
            self.resistorA.setText(Ra)

        RB = 2*float(A)*float(r)
        Rb = '{0:0.11f}'.format(RB)
        self.resistorB.setText(Rb)
        C2 = (float(m1)**2)*float(c)
        c2 = '{0:0.11f}'.format(C2)
        self.capacitor2.setText(c2)
        #Bode
        rr= (1/(float(f)*float(K)*float(m1)*float(c)))
        print("R:",rr)
        x=float(A)
        if x == 0:
            rra =0
        else:
            rra = (2 * float(A) * float(rr)) / float(x)
            print("Ra:",rra)
        rrb = 2*float(A)*float(rr)
        print("Rb:",rrb)
        cc2 = float(m1)*float(m1)*float(c)
        print("C2:",cc2)
        Ba = ((float(rrb))/(float(rra))) if rra !=0 else 0
        ba = ((float(rrb))/(float(cc2)*float(rra))) if rra !=0 else 0
        Bn = ((1 + float(Ba))*(1/(float(c)*float(cc2)*float(rr)*float(rr))))
        Bd1 = (1/(float(c)*float(cc2)*float(rr)*float(rr)))
        Bd2= (1/float(rr))*((2/(float(c))) -float(ba))
        bode = signal.TransferFunction( [float( Bn )], [1, float( Bd2 ), float( Bd1 )] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx(w, mag)
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def RSelector(self):

        value = self.selectResistor.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)

        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
    def RASelector(self):

        value = self.selectResistorA.currentIndex()
        if value == 0:
            r1 = ra/1
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)

        if value ==1:
            r1 = ra/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==2:
            r1 = ra/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)

    def RBSelector(self):

        value = self.selectResistorB.currentIndex()
        if value == 0:
            r1 = RB/1
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

        if value ==1:
            r1 = RB/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==2:
            r1 = RB/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

    def C2Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            c2 = C2/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==1:
            c2 = C2 / (1e-9)
            C = '{0:0.11f}'.format( c2 )
            self.capacitor2.setText( C )
        if value ==2:
            c2 = C2 / (1e-6)
            C = '{0:0.11f}'.format( c2 )
            self.capacitor2.setText( C )
        if value ==3:
            c2 = C2 / (1e-3)
            C = '{0:0.11f}'.format( c2 )
            self.capacitor2.setText( C )

class Window_FpaOSK(QMainWindow):
    def __init__(self, parent=None):
        super(Window_FpaOSK, self).__init__(parent)
        loadUi('.app/pask.ui',self)
        circuit=QPixmap(".img/fpaSK.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows)
        self.ComboBox.currentIndexChanged.connect( self.ComboSelect)
        self.selectFrecuency.currentIndexChanged.connect( self.fSelector )
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector )
        self.fpb_Button_Calcular.clicked.connect( self.Calcular )
        self.selectResistor.currentIndexChanged.connect( self.RSelector )
        self.selectResistor2.currentIndexChanged.connect( self.R2Selector)
        self.selectResistorA.currentIndexChanged.connect( self.RASelector)
        self.selectResistorB.currentIndexChanged.connect( self.RBSelector)

    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def ComboSelect(self):
        self.selectFrecuency.update()
        global Q, K
        value = self.ComboBox.currentIndex()
        if value ==0:
            Q=0.7071
            K=1.0000
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==1:
            Q=0.7247
            K=1.0231
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==2:
            Q=0.7673
            K=1.0674
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==3:
            Q=0.8093
            K=1.0991
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==4:
            Q=0.8638
            K=1.1286
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==5:
            Q=0.9564
            K=1.1596
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==6:
            Q=0.5771
            K=0.7840
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global c
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            c = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            c = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            c = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            c = float(c1)*1e-3

    def Calcular(self):
        global r, R2, RA, RB, C2, Ba, ba
        A = self.ganancia.text()
        if int(A)==1:
            ra = 0
        m1n = 1 + sqrt(1 + (8*(float(Q)**2)*(float(A)-1)))
        m1d = 4*float(Q)
        if m1d == 0:
            self.factorM.setText( "Infinity" )
        else:
            m1 = float(m1n)/float(m1d)
            m = '{0:0.11f}'.format( m1 )
            self.factorM.setText(m)
        rn= float(m1)
        rd = (2 * (math.pi) * float(K) * float(f) * float(c))
        if rd==0:
            self.resistor.setText( "Infinity" )
        else:
            r=float(rn)/float(rd)
            R = '{0:0.11f}'.format( r )
            self.resistor.setText( R )
        R2N=float(r)
        R2D=(float(m1)**2)
        if R2D ==0:
            self.resistor2.setText( "Infinity" )
        else:
            R2 = float(R2N)/float(R2D)
            RR2 = '{0:0.11f}'.format(R2)
            self.resistor2.setText(RR2)
        RAn= float(A)*float(R2)
        RAd= float(A) - 1
        if RAd ==0:
            self.resistorA.setText( "Infinity" )
            RA = 0
        else:
            RA = float(RAn)/float(RAd)
            RRA = '{0:0.11f}'.format(RA)
            self.resistorA.setText(RRA)
        RB= float(A)*float(R2)
        RRB = '{0:0.11f}'.format(RB)
        self.resistorB.setText(RRB)
        #bode
        rr1= float(m1)/(float(K)*float(f)*float(c))
        rr2= float(rr1)/(float(m)**2)
        rran= (float(A)*float(rr2))
        rrad= float(A) - 1
        rra = float(rran)/float(rrad) if rrad != 0 else 0
        rrb = float(A)*float(rr2)
        Fn1 = float(rrb)/float(rra) if rra != 0 else 0
        Fn = 1 + float(Fn1)
        Fd11 = (float(c)**2)*float(rr1)*float(rr2)
        Fd1 = 1/float(Fd11)
        Fd21 = float(rrb)/(float(rr1)*float(rra))if rra != 0 else 0
        Fd22 = 2/float(rr2)
        Fd23 = 1/float(c)
        Fd2 = float(Fd23)*(float(Fd22)-float(Fd21))
        #Trazo de bode
        bode = signal.TransferFunction( [float( Fn ),0 ,0], [1, float(Fd2), float(Fd1)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx(w, mag)
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def RSelector(self):

        value = self.selectResistor.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)

        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)

    def R2Selector(self):

        value = self.selectResistor2.currentIndex()
        if value == 0:
            r1 = R2/1
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)

        if value ==1:
            r1 = R2/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==2:
            r1 = R2/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)

    def RASelector(self):

        value = self.selectResistorA.currentIndex()
        if value == 0:
            r1 = RA/1
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)

        if value ==1:
            r1 = RA/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==2:
            r1 = RA/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)

    def RBSelector(self):

        value = self.selectResistorB.currentIndex()
        if value == 0:
            r1 = RB/1
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

        if value ==1:
            r1 = RB/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==2:
            r1 = RB/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

class Window_FpOSK(QMainWindow):
    def __init__(self, parent=None):
        super(Window_FpOSK, self).__init__(parent)
        loadUi('.app/psk.ui',self)
        circuit=QPixmap(".img/fpsk.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows )
        self.selectFrecuency.currentIndexChanged.connect( self.fSelector )
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector )
        self.fpb_Button_Calcular.clicked.connect( self.Calcular )
        self.selectResistor.currentIndexChanged.connect( self.RSelector )
        self.selectResistorA.currentIndexChanged.connect( self.RASelector)
        self.selectResistorB.currentIndexChanged.connect(self.RBSelector )
        self.selectResistorX.currentIndexChanged.connect( self.RXSelector )
        self.selectCapacitor2.currentIndexChanged.connect( self.c1Selector )


    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global c
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            c = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            c = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            c = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            c = float(c1)*1e-3
    def Calcular(self):
        global r, ra, rb, rx, c1
        A = self.ganancia.text()
        Q = self.calidad.text()
        #corregir a partir de aqui
        mn1 = ((float(A)**2)+float(A)-1)
        mn2 = (((float(A)**2)+float(A)-1)**2)
        mn3 = 4*float(Q)*float(Q)*float(A)*((float(A)+1)**2)
        md = 2*float(A)
        mn = -float(mn1)+sqrt(float(mn2)+float(mn3))
        m = float(mn)/float(md)
        xn = float(A)*float(A)
        xd = float(m)*float(A) + float(A) - 1
        x = float(xn)/float(xd)
        rf1 = 1/(2*(math.pi)*float(f)*float(c))
        rf2 = sqrt((1+float(x))/(float(x)*float(m)))
        r = float(rf1)*float(rf2)
        ran = (float(A)+1)*float(r)
        rad = float(A)
        ra = float(ran)/float(rad)
        rb=(float(A)+1)*float(r)
        rx = float(x)*float(r)
        c1=float(m)*float(c)
        M = '{0:0.11f}'.format(m)
        self.factorM.setText(M)
        R = '{0:0.11f}'.format(r)
        self.resistor.setText(R)
        Ra = '{0:0.11f}'.format(ra)
        self.resistorA.setText(Ra)
        Rb = '{0:0.11f}'.format(rb)
        self.resistorB.setText(Rb)
        Rx = '{0:0.11f}'.format(rx)
        self.resistorX.setText(Rx)
        C1 = '{0:0.11f}'.format(c1)
        self.capacitor2.setText(C1)
        #Equation from bode
        rrf1 = 1/(float(f)*float(c)*2*math.pi)
        rrf2 = sqrt((1+float(x))/(float(x))*float(m))
        rr= float(rrf1)*float(rrf2)
        rran=(float(A)+1)*float(rr)
        rrad=float(A)
        rra = float(rran)/float(rrad)
        rrb = (float(A)+1)*float(rr)
        rrx = float(x)*float(rr)
        cc1 = float(m)*float(c1)
        #Bode equation
        fn1 = 1 + (float(rrb)/float(rra))
        fn2 = 1/(float(rr)*float(c1))
        fn = float(fn1)*float(fn2)
        fd1 = ((float(rr)+float(rrx))/(float(rr)*float(rr)*float(rrx)*float(c1)*float(c)))
        fd21 = ((float(rrb))/(float(rra)*float(rrx)*float(c1)))
        fd22 = 1/(float(rr)*float(c))
        fd23 = 2/(float(rr)*float(c1))
        fd2 = float(fd23) + float(fd22) - float(fd21)
        # Trazo de bode
        bode = signal.TransferFunction( [0, float(fn), 0], [1, float(fd2), float(fd1)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()



    def RSelector(self):
        value = self.selectResistor.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)

        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
    def RASelector(self):
        value = self.selectResistorA.currentIndex()
        if value == 0:
            r1 = ra/1
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)

        if value ==1:
            r1 = ra/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==2:
            r1 = ra/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
    def RBSelector(self):
        value = self.selectResistorB.currentIndex()
        if value == 0:
            r1 = rb/1
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

        if value ==1:
            r1 = rb/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==2:
            r1 = rb/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
    def RXSelector(self):
        value = self.selectResistorX.currentIndex()
        if value == 0:
            r1 = rx/1
            R = '{0:0.11f}'.format(r1)
            self.resistorX.setText(R)
        if value ==1:
            r1 = rx/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorX.setText(R)
        if value ==2:
            r1 = rx/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorX.setText(R)
    def c1Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            c2 = c1/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==1:
            c2 = c1/(1e-9)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==2:
            c2 = c1/(1e-6)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==3:
            c2 = c1/(1e-3)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)

class Window_Fpaso(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fpaso, self).__init__(parent)
        loadUi('.app/fpaso.ui',self)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect(self.ButtonReturnWindows )
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor.currentIndexChanged.connect(self.cSelector)
        self.selectResistor.currentIndexChanged.connect( self.RSelector)
        self.selectResistor1.currentIndexChanged.connect( self.R1Selector)
        self.selectResistorf.currentIndexChanged.connect( self.RfSelector)
        self.fpb_Button_Calcular.clicked.connect( self.Calcular )
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
            global f
            value = self.selectFrecuency.currentIndex()

            if value == 0:
                fc = self.frecuency.text()
                f = float( fc ) * 1
            if value == 1:
                fc = self.frecuency.text()
                f = float( fc ) * 1e3
            if value == 2:
                fc = self.frecuency.text()
                f = float( fc ) * 1e6

    def cSelector(self):
            global c
            value = self.selectCapacitor.currentIndex()
            if value == 0:
                c1 = self.capacitor.text()
                c = float( c1 ) * 1e-12
            if value == 1:
                c1 = self.capacitor.text()
                c = float( c1 ) * 1e-9
            if value == 2:
                c1 = self.capacitor.text()
                c = float( c1 ) * 1e-6
            if value == 3:
                c1 = self.capacitor.text()
                c = float( c1 ) * 1e-3
    def Calcular(self):
        global r, rr1, rf
        A = self.ganancia.text()
        r = 1/(2*(math.pi)*float(f)*float(c))
        rr1d = float(A)-1
        rr1 = (float(A)*float(r))/(float(rr1d))  if rr1d!= 0 else 0
        rf = float(A)*float(r)
        R = '{0:0.11f}'.format(r)
        self.resistor.setText(R)
        R1 = '{0:0.11f}'.format(rr1)
        self.resistor1.setText(R1)
        Rf = '{0:0.11f}'.format(rf)
        self.resistorf.setText(Rf)
        #Bode Equation
        br= 1/(float(f)*float(c))
        br1 = (float(A)*float(br))/(float(rr1d)) if rr1d!= 0 else 0
        brf = (float(A)*float(br))
        fn= ((float(brf))/(float(br1)))+1
        fd = 1/(float(c)*float(br))
        # Trazo de bode
        bode = signal.TransferFunction( [0, float(fn), 0], [0, 1, float( fd )] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def RSelector(self):
        value = self.selectResistor.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            r1 = rr1/1
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==1:
            r1 = rr1/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==2:
            r1 = rr1/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
    def RfSelector(self):
        value = self.selectResistorf.currentIndex()
        if value == 0:
            r1 = rf/1
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==1:
            r1 = rf/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==2:
            r1 = rf/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
class Window_Fpbso(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fpbso, self).__init__(parent)
        loadUi('.app/fpbso.ui',self)
        circuit=QPixmap(".img/fpbso.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows )
        self.ComboBox.currentIndexChanged.connect( self.ComboSelect )
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector)
        self.fpb_Button_Calcular.clicked.connect(self.Calcular)
        self.selectResistor1.currentIndexChanged.connect( self.R1Selector)
        self.selectResistor2.currentIndexChanged.connect( self.R2Selector)
        self.selectResistor3.currentIndexChanged.connect( self.R3Selector)
        self.selectResistor4.currentIndexChanged.connect( self.R4Selector)
        self.selectCapacitor2.currentIndexChanged.connect( self.C2Selector )
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def ComboSelect(self):
        self.selectFrecuency.update()
        global Q, K
        value = self.ComboBox.currentIndex()
        if value ==0:
            Q=0.7071
            K=1.0000
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==1:
            Q=0.7247
            K=0.9774
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==2:
            Q=0.7673
            K=0.9368
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==3:
            Q=0.8093
            K=0.9098
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==4:
            Q=0.8638
            K=0.886
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==5:
            Q=0.9564
            K=0.8623
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
        if value ==6:
            Q=0.5771
            K=1.2754
            q= '{0:0.4f}'.format(Q)
            self.valueq.setText(q)
            k= '{0:0.4f}'.format(K)
            self.valuek.setText(k)
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global c
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            c = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            c = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            c = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            c = float(c1)*1e-3
    def Calcular(self):
        global r11, r2, r3, r4, cc2
        A = self.ganancia.text()
        r3n=float(Q)*(float(A)+1)
        r3d= (math.pi)*(K)*float(f)*float(c)
        r3=float(r3n)/float(r3d)
        cc2= 1/(4*(math.pi)*(float(K))*(float(f))*(float(Q))*(float(r3)))
        ccc2=float(cc2)/(1e-12)
        r11= float(r3)/float(A)
        r2n=float(r3)
        r2d=float(A)+1
        r2= float(r2n)/float(r2d) if r2d!= 0 else 0
        r4= 2*float(r2)
        R1 = '{0:0.11f}'.format(r11)
        self.resistor1.setText(R1)
        R2 = '{0:0.11f}'.format(r2)
        self.resistor2.setText(R2)
        R3 = '{0:0.11f}'.format(r3)
        self.resistor3.setText(R3)
        R4 = '{0:0.11f}'.format(r4)
        self.resistor4.setText(R4)
        C2 = '{0:0.11f}'.format(ccc2)
        self.capacitor2.setText(C2)
        #Bode equation
        br3n=float(Q)*(float(A)+1)
        br3d= (math.pi)*(K)*float(f)*float(c)
        br3=float(br3n)/float(br3d)
        bc2 = 1 /((float(K))*(float(f))*(float(Q))*(float(br3)))
        br1 = float(br3)/float(A)
        br2n = float(br3)
        br2d = float(A)+1
        br2 = float(br2n)/float(br2d) if br2d != 0 else 0
        br4 = 2*float(br2)
        fn=1/(float(c)*float(bc2)*float(br1)*float(br2))
        fd1=1/(float(c)*float(bc2)*float(br2)*float(br3))
        fd21=1/(float(br3))
        fd22= 1/(float(br2))
        fd23= 1/(float(br1))
        fd24 = 1/(float(c))
        fd2 = float(fd24)*(float(fd23)+float(fd22)+float(fd21))
        # Trazo de bode
        bode = signal.TransferFunction( [0, 0, float(fn)], [1, float(fd2), float(fd1)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()
    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            r1 = r11/1
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==1:
            r1 = r11/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==2:
            r1 = r11/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
    def R2Selector(self):
        value = self.selectResistor2.currentIndex()
        if value == 0:
            r1 = r2/1
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==1:
            r1 = r2/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==2:
            r1 = r2/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
    def R3Selector(self):
        value = self.selectResistor3.currentIndex()
        if value == 0:
            r1 = r3/1
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
        if value ==1:
            r1 = r3/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
        if value ==2:
            r1 = r3/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
    def R4Selector(self):
        value = self.selectResistor4.currentIndex()
        if value == 0:
            r1 = r4/1
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
        if value ==1:
            r1 = r4/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
        if value ==2:
            r1 = r4/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
    def C2Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            c2 = cc2/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==1:
            c2 = cc2/(1e-9)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==2:
            c2 = cc2/(1e-6)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==3:
            c2 = cc2/(1e-3)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)

class Window_Fbso(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fbso, self).__init__(parent)
        loadUi('.app/fbso.ui',self)
        circuit=QPixmap(".img/fpso.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows )
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector)
        self.fpb_Button_Calcular.clicked.connect( self.Calcular )
        self.selectResistor1.currentIndexChanged.connect( self.R1Selector )
        self.selectResistor2.currentIndexChanged.connect( self.R2Selector )
        self.selectResistor3.currentIndexChanged.connect( self.R3Selector )
        self.selectResistor4.currentIndexChanged.connect( self.R4Selector )
        self.selectCapacitor2.currentIndexChanged.connect( self.C2Selector )
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global c
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            c = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            c = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            c = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            c = float(c1)*1e-3

    def Calcular(self):
        global r11, r2, r3, r4 ,c22
        A = self.ganancia.text()
        Q = self.calidad.text()
        r11= float(Q)/(2*(math.pi)*float(f)*float(A)*float(c))
        r2= 1/(4*(math.pi)*float(f)*float(Q)*float(c))
        r31=float(Q)/(2*(math.pi)*float(f)*float(c))
        r32= (float(Q)*float(Q))/((float(Q)*float(Q))+float(A))
        r33= float(r32)+1
        r3= (float(r33))*float(r31)
        r4 = float(r3)
        c22= ((float(A)/(float(Q)*float(Q)))+1)*float(c)
        cc2 = float(c22)/(1e-12)
        R1 = '{0:0.11f}'.format(r11)
        self.resistor1.setText(R1)
        R2 = '{0:0.11f}'.format(r2)
        self.resistor2.setText(R2)
        R3 = '{0:0.11f}'.format(r3)
        self.resistor3.setText(R3)
        R4 = '{0:0.11f}'.format(r4)
        self.resistor4.setText(R4)
        C2 = '{0:0.11f}'.format(cc2)
        self.capacitor2.setText(C2)
        #bode equation
        br11= float(Q)/(float(f)*float(A)*float(c))
        br2= 1/(float(f)*float(Q)*float(c))
        br31=float(Q)/(float(f)*float(c))
        br32= (float(Q)*float(Q))/((float(Q)*float(Q))+float(A))
        br33= float(br32)+1
        br3= (float(br33))*float(br31)
        br4 = float(br3)
        bc22= ((float(A)/(float(Q)*float(Q)))+1)*float(c)
<<<<<<< HEAD
        fn= -1/(float(c)*float(br11))
=======
        fn= 1/(float(c)*float(br11))
>>>>>>> fdbf36a8963d572904770d5d91542d29f556a9f0
        fd11= (1/(float(br11))) + (1/(float(br2)))
        fd12= 1/(float(c)*float(bc22)*float(br3))
        fd1 = float(fd11)*float(fd12)
        fd21 = 1/(float(c)) + 1/(float(bc22))
        fd22 = 1/(float(br3))
        fd2 = float(fd21)*float(fd22)
        # Trazo de bode
        bode = signal.TransferFunction( [0, float(fn), 0], [1, float(fd2), float(fd1)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            r1 = r11/1
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==1:
            r1 = r11/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==2:
            r1 = r11/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)

    def R2Selector(self):
        value = self.selectResistor2.currentIndex()
        if value == 0:
            r1 = r2/1
            R = '{0:0.11f}'.format( r1 )
            self.resistor2.setText( R )
        if value == 1:
            r1 = r2/1e3
            R = '{0:0.11f}'.format( r1 )
            self.resistor2.setText( R )
        if value == 2:
            r1 = r2/1e6
            R = '{0:0.11f}'.format( r1 )
            self.resistor2.setText( R )

    def R3Selector(self):
        value = self.selectResistor3.currentIndex()
        if value == 0:
            r1 = r3/ 1
            R = '{0:0.11f}'.format( r1 )
            self.resistor3.setText( R )
        if value == 1:
            r1 = r3/1e3
            R = '{0:0.11f}'.format( r1 )
            self.resistor3.setText( R )
        if value == 2:
            r1 = r3/ 1e6
            R = '{0:0.11f}'.format( r1 )
            self.resistor3.setText( R )

    def R4Selector(self):
        value = self.selectResistor4.currentIndex()
        if value == 0:
            r1 = r4/ 1
            R = '{0:0.11f}'.format( r1 )
            self.resistor4.setText( R )
        if value == 1:
            r1 = r4/1e3
            R = '{0:0.11f}'.format( r1 )
            self.resistor4.setText( R )
        if value == 2:
            r1 = r4/ 1e6
            R = '{0:0.11f}'.format( r1 )
            self.resistor4.setText( R )

    def C2Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            c2 = c22/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==1:
            c2 = c22/(1e-9)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==2:
            c2 = c22/(1e-6)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==3:
            c2 = c22/(1e-3)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)

class Window_Fprbso(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fprbso, self).__init__(parent)
        loadUi('.app/fprbso.ui',self)
        circuit=QPixmap(".img/fpsrbso.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect( self.ButtonReturnWindows )
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor.currentIndexChanged.connect( self.cSelector)
        self.selectResistorc.currentIndexChanged.connect( self.RcSelector)
        self.fpb_Button_Calcular.clicked.connect( self.Calcular )
        self.selectResistora.currentIndexChanged.connect( self.RaSelector )
        self.selectResistorb.currentIndexChanged.connect( self.RbSelector )
        self.selectResistorlp.currentIndexChanged.connect( self.RlpSelector )
        self.selectResistorhp.currentIndexChanged.connect( self.RhpSelector )
        self.selectCapacitorhp.currentIndexChanged.connect( self.ChpSelector )

<<<<<<< HEAD

=======
>>>>>>> fdbf36a8963d572904770d5d91542d29f556a9f0
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()

        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def cSelector(self):
        global clp
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            c1 = self.capacitor.text()
            clp = float(c1)*1e-12
        if value ==1:
            c1 = self.capacitor.text()
            clp = float(c1)*1e-9
        if value ==2:
            c1 = self.capacitor.text()
            clp = float(c1)*1e-6
        if value ==3:
            c1 = self.capacitor.text()
            clp = float(c1)*1e-3

    def RcSelector(self):
        global rc
        value = self.selectResistorc.currentIndex()
        if value == 0:
            rcc = self.resistorc.text()
            rc = float(rcc)*1
        if value == 1:
            rcc = self.resistorc.text()
            rc = float(rcc)*(1e3)
        if value == 2:
            rcc = self.resistorc.text()
            rc = float(rcc)*(1e6)

    def Calcular(self):
        global ra, rb, rlp, rhp, chp
        A = self.ganancia.text()
        Q = 0.5
        ra=(float(A)*float(rc))/(2*float(A)+1)
        rb=float(A)*float(rc)
        mn=1-sqrt((1-4*float(Q)*float(Q)))
        md=2*float(Q)*float(Q)
        m=float(mn)/float(md)
        rlp=(float(m)*float(Q))/(2*(math.pi)*float(f)*float(clp))
        rhp=float(Q)/(2*(math.pi)*float(f)*float(clp))
        chp=(float(m)*float(clp))/(float(m)-1)
        cchp=chp/(1e-12)
        Ra = '{0:0.11f}'.format(ra)
        self.resistora.setText(Ra)
        Rb = '{0:0.11f}'.format(rb)
        self.resistorb.setText(Rb)
        Rlp = '{0:0.11f}'.format(rlp)
        self.resistorlp.setText(Rlp)
        Rhp = '{0:0.11f}'.format(rhp)
        self.resistorhp.setText(Rhp)
        Chp = '{0:0.11f}'.format(cchp)
        self.capacitorhp.setText(Chp)
        #bode equation
        brlp=(float(m)*float(Q))/(float(f)*float(clp))
        brhp=float(Q)/(float(f)*float(clp))
        bchp=(float(m)*float(clp))/(float(m)-1)
        fn=1/(float(bchp)*float(clp)*float(brhp)*float(brlp))
        fd1=1/(float(bchp)*float(clp)*float(brhp)*float(brlp))
        fd21= 1/(float(clp)*float(brlp))
        fd22=1/(float(bchp)*float(brhp))
        fd2 = float(fd22)+float(fd21)
        # Trazo de bode
<<<<<<< HEAD
        bode = signal.TransferFunction( [1,0,float(fn)], [1, float(fd2), float(fd1)] )
=======
        bode = signal.TransferFunction( [1, float(fn), 0], [1, float(fd2), float(fd1)] )
>>>>>>> fdbf36a8963d572904770d5d91542d29f556a9f0
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()
    def RaSelector(self):
        value = self.selectResistora.currentIndex()
        if value == 0:
            r1 = ra/1
            R = '{0:0.11f}'.format(r1)
            self.resistora.setText(R)
        if value ==1:
            r1 = ra/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistora.setText(R)
        if value ==2:
            r1 = ra/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistora.setText(R)

    def RbSelector(self):
        value = self.selectResistorb.currentIndex()
        if value == 0:
            r1 = rb/1
            R = '{0:0.11f}'.format(r1)
            self.resistorb.setText(R)
        if value ==1:
            r1 = rb/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorb.setText(R)
        if value ==2:
            r1 = rb/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorb.setText(R)

    def RhpSelector(self):
        value = self.selectResistorhp.currentIndex()
        if value == 0:
            r1 = rhp/1
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)
        if value ==1:
            r1 = rhp/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)
        if value ==2:
            r1 = rhp/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)

    def RlpSelector(self):
        value = self.selectResistorlp.currentIndex()
        if value == 0:
            r1 = rlp/1
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)
        if value ==1:
            r1 = rlp/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)
        if value ==2:
            r1 = rlp/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)


    def ChpSelector(self):
        value = self.selectCapacitorhp.currentIndex()
        if value == 0:
            c2 = chp/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitorhp.setText(C)
        if value ==1:
            c2 = chp/(1e-9)
            C = '{0:0.11f}'.format(c2)
            self.capacitorhp.setText(C)
        if value ==2:
            c2 = chp/(1e-6)
            C = '{0:0.11f}'.format(c2)
            self.capacitorhp.setText(C)
        if value ==3:
            c2 = chp/(1e-3)
            C = '{0:0.11f}'.format(c2)
            self.capacitorhp.setText(C)

<<<<<<< HEAD
class Window_Fpb2opa(QMainWindow):
    def __init__(self, parent=None):
        super(Window_Fpb2opa, self).__init__(parent)
        loadUi('.app/fpb2opa.ui',self)
        circuit=QPixmap(".img/fpb2opam.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect(self.ButtonReturnWindows)
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor1.currentIndexChanged.connect(self.c1Selector)
        self.selectCapacitor.currentIndexChanged.connect(self.cSelector)
        self.fpb_Button_Calcular.clicked.connect(self.Calcular)
        self.selectResistor.currentIndexChanged.connect(self.RSelector)
        self.selectResistorA.currentIndexChanged.connect(self.RaSelector)
        self.selectResistorB.currentIndexChanged.connect(self.RbSelector)
        self.selectCapacitor2.currentIndexChanged.connect(self.C2Selector)
        self.selectResistorf.currentIndexChanged.connect(self.RfSelector)
        self.selectResistorR.currentIndexChanged.connect(self.Re2Selector)
        self.selectResistor1.currentIndexChanged.connect(self.R1Selector)
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()
        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def c1Selector(self):
        global C1
        value = self.selectCapacitor1.currentIndex()
        if value == 0:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-12
        if value ==1:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-9
        if value ==2:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-6
        if value ==3:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-3
    def cSelector(self):
        global C
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            cc = self.capacitor.text()
            C = float(cc)*1e-12
        if value ==1:
            cc = self.capacitor.text()
            C = float(cc)*1e-9
        if value ==2:
            cc = self.capacitor.text()
            C = float(cc)*1e-6
        if value ==3:
            cc1 = self.capacitor.text()
            C = float(cc)*1e-3

    def Calcular(self):
        # Etapa 1
        global r,ra,rb,cc2
        A1 = self.ganancia1.text()
        A2 = self.ganancia2.text()
        Qlp=0.7071
        Klp=1
        mn= 1 + sqrt(1+8*(float(Qlp)*float(Qlp))*(float(A1)-1))
        md= 4*(float(Qlp))
        m = float(mn)/float(md)
        r= 1/(2*(math.pi)*float(Klp)*float(f)*float(m)*float(C1))
        ran= 2*float(A1)*float(r)
        rad= float(A1)-1
        ra = float(ran)/float(rad) if rad != 0 else 0
        rb = 2*float(A1)*float(r)
        cc2 = float(m)*float(m)*float(C1)
        c2 =float(cc2)/(1e-12)
        #Etapa 2
        global rf, r1, re2
        rf=1/(2*(math.pi)*float(Klp)*float(f)*float(C))
        re2= float(rf)/float(A2)
        r1=1/((1/float(rf))+(1/float(re2)))
        #Etapa 1
        R = '{0:0.11f}'.format(r)
        self.resistor.setText(R)
        Ra = '{0:0.11f}'.format(ra)
        self.resistorA.setText(Ra)
        Rb = '{0:0.11f}'.format(rb)
        self.resistorB.setText(Rb)
        C2 = '{0:0.11f}'.format(c2)
        self.capacitor2.setText(C2)
        #Etapa 2
        Rf = '{0:0.11f}'.format(rf)
        self.resistorf.setText(Rf)
        Re2 = '{0:0.11f}'.format(re2)
        self.resistorR.setText(Re2)
        R1 = '{0:0.11f}'.format(r1)
        self.resistor1.setText(R1)
        #bode
        brf=1/(2*float(Klp)*float(f)*float(C))
        br= float(rf)/float(A2)
        br1=1/((1/float(rf))+(1/float(br)))
        fn=-(float(brf)/float(br))*(1/(float(C)*float(brf)))
        fd=1/(float(C)*float(brf))
        bode = signal.TransferFunction( [0,0,float(fn)], [0, 1, float(fd)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def RSelector(self):
        value = self.selectResistor.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor.setText(R)
    def RaSelector(self):
        value = self.selectResistorA.currentIndex()
        if value == 0:
            r1 = ra/1
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==1:
            r1 = ra/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==2:
            r1 = ra/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
    def RbSelector(self):
        value = self.selectResistorB.currentIndex()
        if value == 0:
            r1 = rb/1
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==1:
            r1 = rb/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==2:
            r1 = rb/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)

    def C2Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            c2 = cc2/(1e-12)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==1:
            c2 = cc2/(1e-9)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==2:
            c2 = cc2/(1e-6)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
        if value ==3:
            c2 = cc2/(1e-3)
            C = '{0:0.11f}'.format(c2)
            self.capacitor2.setText(C)
    def RfSelector(self):
        value = self.selectResistorf.currentIndex()
        if value == 0:
            r1 = rf/1
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==1:
            r1 = rf/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==2:
            r1 = rf/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
    def Re2Selector(self):
        value = self.selectResistorR.currentIndex()
        if value == 0:
            r1 = re2/1
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)
        if value ==1:
            r1 = re2/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)
        if value ==2:
            r1 = re2/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)
    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            rr1 = r1/1
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)
        if value ==1:
            rr1 = r1/1e3
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)
        if value ==2:
            rr1 = r1/1e6
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)


class Window_fpa2opa(QMainWindow):
    def __init__(self, parent=None):
        super(Window_fpa2opa, self).__init__(parent)
        loadUi('.app/fpa2opa.ui',self)
        circuit=QPixmap(".img/fpa2opam.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect(self.ButtonReturnWindows)
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor1.currentIndexChanged.connect(self.c1Selector)
        self.selectCapacitor.currentIndexChanged.connect(self.cSelector)
        self.fpb_Button_Calcular.clicked.connect(self.Calcular)
        self.selectResistor1.currentIndexChanged.connect(self.R1Selector)
        self.selectResistor2.currentIndexChanged.connect(self.R2Selector)
        self.selectResistorA.currentIndexChanged.connect(self.RaSelector)
        self.selectResistorB.currentIndexChanged.connect(self.RbSelector)
        self.selectResistorf.currentIndexChanged.connect(self.RfSelector)
        self.selectResistorR.currentIndexChanged.connect(self.RSelector)

    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()
        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def c1Selector(self):
        global C1
        value = self.selectCapacitor1.currentIndex()
        if value == 0:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-12
        if value ==1:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-9
        if value ==2:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-6
        if value ==3:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-3
    def cSelector(self):
        global C
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            cc = self.capacitor.text()
            C = float(cc)*1e-12
        if value ==1:
            cc = self.capacitor.text()
            C = float(cc)*1e-9
        if value ==2:
            cc = self.capacitor.text()
            C = float(cc)*1e-6
        if value ==3:
            cc1 = self.capacitor.text()
            C = float(cc)*1e-3

    def Calcular(self):
        A1 = self.ganancia1.text()
        A2 = self.ganancia2.text()
       #Qhp=0.7071
        #Etapa 1
        global r1,r2, ra, rb
        #Qhp = 1
        Qhp = 0.7071
        khp=1
        mn= 1 + sqrt(1+8*(float(Qhp)*float(Qhp))*(float(A1)-1))
        md= 4*(float(Qhp))
        m = float(mn)/float(md)
        r1 = float(m)/(2*(math.pi)*float(khp)*float(f)*float(C1))
        r2 =  float(r1)/(float(m)*float(m))
        ran = float(A1)*float(r2)
        rad = float(A1) - 1
        ra = float(ran)/(float(rad)) if rad != 0 else 0
        rb = float(A1)*float(r2)
        #Etapa 2
        global r, rf
        r = 1/(2*(math.pi)*float(khp)*float(f)*float(C))
        rf = float(A2)*float(r)
        rplus = rf
        #Etapa 1
        R1 = '{0:0.11f}'.format(r1)
        self.resistor1.setText(R1)
        R2 = '{0:0.11f}'.format(r2)
        self.resistor2.setText(R2)
        Ra = '{0:0.11f}'.format(ra)
        self.resistorA.setText(Ra)
        Rb = '{0:0.11f}'.format(rb)
        self.resistorB.setText(Rb)
        #Etapa 2
        Rf = '{0:0.11f}'.format(rf)
        self.resistorf.setText(Rf)
        R = '{0:0.11f}'.format(r)
        self.resistorR.setText(R)
        #BODE
        Br = 1/(2*float(khp)*float(f)*float(C))
        Brf = float(A2)*float(Br)
        fn = -(float(Brf))/(float(Br))
        fd = 1/(float(Br)*float(C))
        bode = signal.TransferFunction( [0,float(fn),0], [0, 1, float(fd)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()

    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            rr1 = r1/1
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)
        if value ==1:
            rr1 = r1/1e3
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)
        if value ==2:
            rr1 = r1/1e6
            R = '{0:0.11f}'.format(rr1)
            self.resistor1.setText(R)
    def R2Selector(self):
        value = self.selectResistor2.currentIndex()
        if value == 0:
            r1 = r2/1
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==1:
            r1 = r2/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==2:
            r1 = r2/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
    def RaSelector(self):
        value = self.selectResistorA.currentIndex()
        if value == 0:
            r1 = ra/1
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==1:
            r1 = ra/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
        if value ==2:
            r1 = ra/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorA.setText(R)
    def RbSelector(self):
        value = self.selectResistorB.currentIndex()
        if value == 0:
            r1 = rb/1
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==1:
            r1 = rb/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
        if value ==2:
            r1 = rb/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorB.setText(R)
    def RfSelector(self):
        value = self.selectResistorf.currentIndex()
        if value == 0:
            r1 = rf/1
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==1:
            r1 = rf/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
        if value ==2:
            r1 = rf/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorf.setText(R)
    def RSelector(self):
        value = self.selectResistorR.currentIndex()
        if value == 0:
            r1 = r/1
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)
        if value ==1:
            r1 = r/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)
        if value ==2:
            r1 = r/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorR.setText(R)

class Window_fpbb2opa(QMainWindow):
    def __init__(self, parent=None):
        super(Window_fpbb2opa, self).__init__(parent)
        loadUi('.app/fpbb2opa.ui',self)
        circuit=QPixmap(".img/fpbb2opam.png")
        self.Fimg.setPixmap(circuit)
        self.bode = plt.figure()
        self.canvas = FigureCanvas( self.bode )
        self.toolbar = NavigationToolbar( self.canvas, self )
        self.layout.addWidget( self.toolbar )
        self.layout.addWidget( self.canvas )
        self.buttonReturn.clicked.connect(self.ButtonReturnWindows)
        self.selectFrecuency.currentIndexChanged.connect(self.fSelector)
        self.selectCapacitor1.currentIndexChanged.connect(self.c1Selector)
        self.selectCapacitor.currentIndexChanged.connect(self.cSelector)
        self.fpb_Button_Calcular.clicked.connect(self.Calcular)
        self.selectResistor1.currentIndexChanged.connect(self.R1Selector)
        self.selectResistor2.currentIndexChanged.connect(self.R2Selector)
        self.selectResistor3.currentIndexChanged.connect(self.R3Selector)
        self.selectResistor4.currentIndexChanged.connect(self.R4Selector)
        self.selectCapacitor2.currentIndexChanged.connect(self.C2Selector)
        self.selectResistorhp.currentIndexChanged.connect(self.RhpSelector)
        self.selectResistorlp.currentIndexChanged.connect(self.RlpSelector)
        self.selectCapacitorhp.currentIndexChanged.connect(self.ChpSelector)
    def ButtonReturnWindows(self):
        self.parent().show()
        self.close()
    def fSelector(self):
        global f
        value = self.selectFrecuency.currentIndex()
        if value == 0:
            fc = self.frecuency.text()
            f = float(fc)*1
        if value ==1:
            fc = self.frecuency.text()
            f = float(fc) * 1e3
        if value ==2:
            fc = self.frecuency.text()
            f = float(fc) * 1e6
    def c1Selector(self):
        global C1
        value = self.selectCapacitor1.currentIndex()
        if value == 0:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-12
        if value ==1:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-9
        if value ==2:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-6
        if value ==3:
            cc1 = self.capacitor1.text()
            C1 = float(cc1)*1e-3
    def cSelector(self):
        global C
        value = self.selectCapacitor.currentIndex()
        if value == 0:
            cc = self.capacitor.text()
            C = float(cc)*1e-12
        if value ==1:
            cc = self.capacitor.text()
            C = float(cc)*1e-9
        if value ==2:
            cc = self.capacitor.text()
            C = float(cc)*1e-6
        if value ==3:
            cc = self.capacitor.text()
            C = float(cc)*1e-3
    def Calcular(self):
        global rr1, r2, r3, r4, c2, rlp, rhp, chp
        A1 = self.ganancia1.text()
        A2 = self.ganancia2.text()
        Q = 0.5
        Q2 = float(Q)*float(Q)
        rr1 = (float(Q))/(2*(math.pi)*float(f)*float(A1)*float(C1))
        r2 = 1/(4*(math.pi)*float(f)*float(Q)*float(C1))
        r3 = ((float(Q2)/(float(Q2)+float(A1))) + 1)*(float(Q)/(2*(math.pi)*float(f)*float(C1)))
        r4 = float(r3)
        c2 = ((float(A1)/float(Q2)) + 1)*float(C1)
        cc2 = (float(c2))/(1e-12)
        #Etapa 1
        R1 = '{0:0.11f}'.format(rr1)
        self.resistor1.setText(R1)
        R2 = '{0:0.11f}'.format(r2)
        self.resistor2.setText(R2)
        R3 = '{0:0.11f}'.format(r3)
        self.resistor3.setText(R3)
        R4 = '{0:0.11f}'.format(r4)
        self.resistor4.setText(R4)
        C2 = '{0:0.11f}'.format(cc2)
        self.capacitor2.setText(C2)
        #Etapa 2
        mn = 1 - sqrt(1 -4*float(Q2))
        md = 2*float(Q2)
        m = float(mn)/float(md)
        rlp = (float(m)*float(Q))/(2*(math.pi)*float(f)*float(C))
        rhp = float(Q)/(2*(math.pi)*float(f)*float(A2)*float(C))
        chp = (float(m)*float(A2)*float(C))/(float(m)-1)
        cchp = float(chp)/(1e-12)
        Rlp = '{0:0.11f}'.format(rlp)
        self.resistorlp.setText(Rlp)
        Rhp = '{0:0.11f}'.format(rhp)
        self.resistorhp.setText(Rhp)
        Chp = '{0:0.11f}'.format(cchp)
        self.capacitorhp.setText(Chp)
        #bode
        brlp = (float(m)*float(Q))/(float(f)*float(C))
        brhp = float(Q)/(float(f)*float(A2)*float(C))
        bchp = (float(m)*float(A2)*float(C))/(float(m)-1)
        fn = 1/(float(C)*float(brhp))
        fd1 = 1/(float(bchp)*float(C)*float(brhp)*float(brlp))
        fd2 = (1/(float(bchp)*float(brhp)))+(1/(float(C)*float(brlp)))
        bode = signal.TransferFunction( [0,float(fn),0], [1, float(fd2), float(fd1)] )
        w, mag, phase = signal.bode( bode )
        self.bode.clear()
        # plt.figure()
        self.bode.add_subplot( 2, 1, 1 )
        plt.gca().set_title( 'Bode Diagram' )
        plt.gca().set_ylabel( 'Magnitude(DB)' )
        plt.semilogx( w, mag )
        self.bode.add_subplot( 2, 1, 2 )
        plt.semilogx( w, phase )
        plt.gca().set_ylabel( 'Phase(deg)' )
        self.canvas.draw()



    def R1Selector(self):
        value = self.selectResistor1.currentIndex()
        if value == 0:
            r1 = rr1/1
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==1:
            r1 = rr1/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
        if value ==2:
            r1 = rr1/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor1.setText(R)
    def R2Selector(self):
        value = self.selectResistor2.currentIndex()
        if value == 0:
            r1 = r2/1
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==1:
            r1 = r2/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
        if value ==2:
            r1 = r2/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor2.setText(R)
    def R3Selector(self):
        value = self.selectResistor3.currentIndex()
        if value == 0:
            r1 = r3/1
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
        if value ==1:
            r1 = r3/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
        if value ==2:
            r1 = r3/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor3.setText(R)
    def R4Selector(self):
        value = self.selectResistor4.currentIndex()
        if value == 0:
            r1 = r3/1
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
        if value ==1:
            r1 = r4/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
        if value ==2:
            r1 = r4/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistor4.setText(R)
    def C2Selector(self):
        value = self.selectCapacitor2.currentIndex()
        if value == 0:
            cc2 = c2/(1e-12)
            C = '{0:0.11f}'.format(cc2)
            self.capacitor2.setText(C)
        if value ==1:
            cc2 = c2/(1e-9)
            C = '{0:0.11f}'.format(cc2)
            self.capacitor2.setText(C)
        if value ==2:
            cc2 = c2/(1e-6)
            C = '{0:0.11f}'.format(cc2)
            self.capacitor2.setText(C)
        if value ==3:
            cc2 = c2/(1e-3)
            C = '{0:0.11f}'.format(cc2)
            self.capacitor2.setText(C)
    def RhpSelector(self):
        value = self.selectResistorhp.currentIndex()
        if value == 0:
            r1 = rhp/1
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)
        if value ==1:
            r1 = rhp/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)
        if value ==2:
            r1 = rhp/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorhp.setText(R)
    def RlpSelector(self):
        value = self.selectResistorlp.currentIndex()
        if value == 0:
            r1 = rlp/1
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)
        if value ==1:
            r1 = rlp/1e3
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)
        if value ==2:
            r1 = rlp/1e6
            R = '{0:0.11f}'.format(r1)
            self.resistorlp.setText(R)
    def ChpSelector(self):
        value = self.selectCapacitorhp.currentIndex()
        if value == 0:
            cc2 = chp/(1e-12)
            C = '{0:0.11f}'.format(cc2)
            self.capacitorhp.setText(C)
        if value ==1:
            cc2 = chp/(1e-9)
            C = '{0:0.11f}'.format(cc2)
            self.capacitorhp.setText(C)
        if value ==2:
            cc2 = chp/(1e-6)
            C = '{0:0.11f}'.format(cc2)
            self.capacitorhp.setText(C)
        if value ==3:
            cc2 = chp/(1e-3)
            C = '{0:0.11f}'.format(cc2)
            self.capacitorhp.setText(C)
=======







>>>>>>> fdbf36a8963d572904770d5d91542d29f556a9f0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window_main()
    GUI.show()
    sys.exit(app.exec_())


