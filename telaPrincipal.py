from tkinter import ttk
from tkinter import *
import sqlite3


class Product(object):

    #db_name = 'database.db'
    def __init__(self, window):
        self.wind = window
        self.wind.title("NOME DO SISTEMA")
        self.wind.geometry("803x500+150+120")
        self.wind.configure(bg='#FFFF00')

        self.frame_02 = Frame(self.wind, width=799, height=26, bg='#000000', bd=2, relief='groove')
        self.frame_02.place(x=2, y=1)
        self.lbl_01_02 = Label(self.frame_02, text='Usuário', font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_01_02.place(x=2, y=1)
        self.lbl_01_02 = Label(self.frame_02, text='NOME DA EMPRESA', font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_01_02.place(x=300, y=1)
        self.lbl_01_02 = Label(self.frame_02, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_01_02.place(x=550, y=1)

        self.frame_01 = Frame(self.wind, width=799, height=39, bg='#000000', bd=2, relief='groove')
        self.frame_01.place(x=2, y=40)
        self.lbl_01_01 = Label(self.frame_01, text="HOME", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_01_01.place(x=370, y=8)

        # Botões modulares do sistema
        self.frame_03 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_03.place(x=2, y=100)
        self.btn_03 = Button(self.frame_03, text='Administrativo', font='Georgia 15 bold', width=13, bg='pink', height=5, command=self.administrativo)
        self.btn_03.pack()

        self.frame_04 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_04.place(x=203, y=100)
        self.btn_04 = Button(self.frame_04, text='Comercial', font='Georgia 15 bold', width=13, height=5, command=self.comercial)
        self.btn_04.pack()

        self.frame_05 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_05.place(x=404, y=100)
        self.btn_05 = Button(self.frame_05, text='Financeiro', font='Georgia 15 bold', width=13, height=5, command=self.financeiro)
        self.btn_05.pack()

        self.frame_06 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_06.place(x=605, y=100)
        self.btn_06 = Button(self.frame_06, text='Logística', font='Georgia 15 bold', width=13, height=5, command=self.logistica)
        self.btn_06.pack()

        self.frame_07 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_07.place(x=2, y=248)
        self.btn_07 = Button(self.frame_07, text='Transporte', font='Georgia 15 bold', width=13, height=5, command=self.transporte)
        self.btn_07.pack()

        self.frame_08 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_08.place(x=203, y=248)
        self.btn_08 = Button(self.frame_08, text='Fiscal', font='Georgia 15 bold', width=13, height=5)
        self.btn_08.pack()

        self.frame_09 = Frame(self.wind, width=200, height=150, bg='Chocolate', bd=2, relief='groove')
        self.frame_09.place(x=404, y=248)
        self.btn_09 = Button(self.frame_09, text='Contábil', font='Georgia 15 bold', width=13, height=5)
        self.btn_09.pack()

        self.frame_10 = Frame(self.wind, width=200, height=150, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_10.place(x=605, y=248)
        self.btn_10 = Button(self.frame_10, text='Pessoal', font='Georgia 15 bold', width=13, height=5)
        self.btn_10.pack()


        # Botão de Configuração
        self.frame_11 = Frame(self.wind, width=130, height=50, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_11.place(x=25, y=433)
        self.btn_11 = Button(self.frame_11, text='Configuração', width=18, height=2)
        self.btn_11.pack()

        # Botão de fechar sistema
        self.frame_12 = Frame(self.wind, width=130, height=50, bg='#4F4F4F', bd=2, relief='groove')
        self.frame_12.place(x=166, y=433)
        self.btn_12 = Button(self.frame_12, text='Fechar', width=18, height=2)
        self.btn_12.pack()

    # Telas de Módulos
    def administrativo(self):
        #self.botaocadastro = PhotoImage('./img/cadastro.gif')
        self.tela_administrativo = Toplevel()
        self.tela_administrativo.title('NOME DO SISTEMA')
        self.tela_administrativo.geometry("803x500+190+120")
        self.tela_administrativo.configure(bg='#FFFF00')

        self.frame_adm_01 = Frame(self.tela_administrativo, width=799, height=26, bg='#000000', bd=2, relief='flat')
        self.frame_adm_01.place(x=2, y=2)
        self.lbl_m1_01 = Label(self.frame_adm_01, text="Usuário", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_01.place(x=2, y=1)
        self.lbl_m1_03 = Label(self.frame_adm_01, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_03.place(x=600, y=1)

        self.frame_adm_02 = Frame(self.tela_administrativo, width=799, height=39, bg='#000000', bd=2, relief='flat')
        self.frame_adm_02.place(x=2, y=44)
        self.lbl_m1_04 = Label(self.frame_adm_02, text="ADMINISTRATIVO", font='Georgia 16 bold', bg='#000000', fg='white')
        self.lbl_m1_04.place(x=291, y=2)

        # Frame Cadastro
        self.frame_adm_03 = Frame(self.tela_administrativo, width=190, height=300, bg='black')
        self.frame_adm_03.place(x=20, y=106)
        self.lbl_m1_05 = Label(self.frame_adm_03, text='Cadastros', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_05.place(x=2, y=2)
        self.btn_cad_fin_01 = Button(self.frame_adm_03, width=18, height=14, bg='green')
        self.btn_cad_fin_01.place(x=1, y=33)

        self.frame_adm_04 = Frame(self.tela_administrativo, width=190, height=300)
        self.frame_adm_04.place(x=305, y=106)
        self.lbl_m1_06 = Label(self.frame_adm_04, text='Movimentação', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_06.place(x=2, y=2)

        self.frame_adm_05 = Frame(self.tela_administrativo, width=190, height=300)
        self.frame_adm_05.place(x=592, y=106)
        self.lbl_m1_07 = Label(self.frame_adm_05, text='Visualização', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_07.place(x=2, y=2)

        self.frame_adm_06 = Frame(self.tela_administrativo, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_adm_06.place(x=25, y=437)
        self.btn_m1_01 = Button(self.frame_adm_06, text='Configuração', width=18, height=2)
        self.btn_m1_01.pack()

        self.frame_adm_07 = Frame(self.tela_administrativo, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_adm_07.place(x=166, y=437)
        self.btn_m1_02 = Button(self.frame_adm_07, text='Manual', width=18, height=2)
        self.btn_m1_02.pack()

        self.frame_adm_08 = Frame(self.tela_administrativo, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_adm_08.place(x=640, y=437)
        self.btn_m1_03 = Button(self.frame_adm_08, text='Fechar', width=18, height=2)
        self.btn_m1_03.pack()

        self.tela_administrativo.mainloop()


    def comercial(self):
        self.tela_Comercial = Toplevel()
        self.tela_Comercial.title('NOME DO SISTEMA')
        self.tela_Comercial.geometry("803x500+190+120")
        self.tela_Comercial.configure(bg='#FFFF00')

        self.frame_com_01 = Frame(self.tela_Comercial, width=799, height=26, bg='#000000', bd=2, relief='flat')
        self.frame_com_01.place(x=2, y=2)
        self.lbl_m1_01 = Label(self.frame_com_01, text="Usuário", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_01.place(x=2, y=1)
        self.lbl_m1_02 = Label(self.frame_com_01, text="NOME DA EMPRESA", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_02.place(x=300, y=1)
        self.lbl_m1_03 = Label(self.frame_com_01, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_03.place(x=600, y=1)

        self.frame_com_02 = Frame(self.tela_Comercial, width=799, height=39, bg='#000000', bd=2, relief='flat')
        self.frame_com_02.place(x=2, y=44)
        self.lbl_m1_04 = Label(self.frame_com_02, text="COMERCIAL", font='Georgia 16 bold', bg='#000000', fg='white')
        self.lbl_m1_04.place(x=291, y=2)

        self.frame_com_03 = Frame(self.tela_Comercial, width=190, height=300)
        self.frame_com_03.place(x=20, y=106)
        self.lbl_m1_05 = Label(self.frame_com_03, text='Cadastros', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_05.place(x=2, y=2)

        self.frame_com_04 = Frame(self.tela_Comercial, width=190, height=300)
        self.frame_com_04.place(x=305, y=106)
        self.lbl_m1_06 = Label(self.frame_com_04, text='Movimentação', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_06.place(x=2, y=2)

        self.frame_com_05 = Frame(self.tela_Comercial, width=190, height=300)
        self.frame_com_05.place(x=592, y=106)
        self.lbl_m1_07 = Label(self.frame_com_05, text='Visualização', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_07.place(x=2, y=2)

        self.frame_com_06 = Frame(self.tela_Comercial, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_com_06.place(x=25, y=437)
        self.btn_m1_01 = Button(self.frame_com_06, text='Configuração', width=18, height=2)
        self.btn_m1_01.pack()

        self.frame_com_07 = Frame(self.tela_Comercial, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_com_07.place(x=166, y=437)
        self.btn_m1_02 = Button(self.frame_com_07, text='Manual', width=18, height=2)
        self.btn_m1_02.pack()

        self.frame_com_08 = Frame(self.tela_Comercial, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_com_08.place(x=640, y=437)
        self.btn_m1_03 = Button(self.frame_com_08, text='Fechar', width=18, height=2)
        self.btn_m1_03.pack()



        self.tela_Comercial.mainloop()


    # Tela módulo Financeiro
    def financeiro(self):
        self.tela_Financeiro = Toplevel()
        self.tela_Financeiro.title('NOME DO SISTEMA')
        self.tela_Financeiro.geometry("803x500+190+120")
        self.tela_Financeiro.configure(bg='#FFFF00')

        self.frame_fin_01 = Frame(self.tela_Financeiro, width=799, height=26, bg='#000000', bd=2, relief='flat')
        self.frame_fin_01.place(x=2, y=2)
        self.lbl_m1_01 = Label(self.frame_fin_01, text="Usuário", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_01.place(x=2, y=1)
        self.lbl_m1_02 = Label(self.frame_fin_01, text="NOME DA EMPRESA", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_02.place(x=300, y=1)
        self.lbl_m1_03 = Label(self.frame_fin_01, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_03.place(x=600, y=1)

        self.frame_fin_02 = Frame(self.tela_Financeiro, width=799, height=39, bg='#000000', bd=2, relief='flat')
        self.frame_fin_02.place(x=2, y=44)
        self.lbl_m1_04 = Label(self.frame_fin_02, text="COMERCIAL", font='Georgia 16 bold', bg='#000000', fg='white')
        self.lbl_m1_04.place(x=291, y=2)

        self.frame_fin_03 = Frame(self.tela_Financeiro, width=190, height=300)
        self.frame_fin_03.place(x=20, y=106)
        self.lbl_m1_05 = Label(self.frame_fin_03, text='Cadastros',bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_05.place(x=2, y=2)

        self.frame_fin_04 = Frame(self.tela_Financeiro, width=190, height=300)
        self.frame_fin_04.place(x=305, y=106)
        self.lbl_m1_06 = Label(self.frame_fin_04, text='Movimentação', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_06.place(x=2, y=2)

        self.frame_fin_05 = Frame(self.tela_Financeiro, width=190, height=300)
        self.frame_fin_05.place(x=592, y=106)
        self.lbl_m1_07 = Label(self.frame_fin_05, text='Visualização', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_07.place(x=2, y=2)

        self.frame_fin_06 = Frame(self.tela_Financeiro, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_fin_06.place(x=25, y=437)
        self.btn_m1_01 = Button(self.frame_fin_06, text='Configuração', width=18, height=2)
        self.btn_m1_01.pack()

        self.frame_fin_07 = Frame(self.tela_Financeiro, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_fin_07.place(x=166, y=437)
        self.btn_m1_02 = Button(self.frame_fin_07, text='Manual', width=18, height=2)
        self.btn_m1_02.pack()

        self.frame_fin_08 = Frame(self.tela_Financeiro, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_fin_08.place(x=640, y=437)
        self.btn_m1_03 = Button(self.frame_fin_08, text='Fechar', width=18, height=2)
        self.btn_m1_03.pack()

        self.tela_Financeiro.mainloop()


    # Tela módulo Logística
    def logistica(self):
        self.tela_Logistica = Toplevel()
        self.tela_Logistica.title('NOME DO SISTEMA')
        self.tela_Logistica.geometry("803x500+190+120")
        self.tela_Logistica.configure(bg='#FFFF00')

        self.frame_log_01 = Frame(self.tela_Logistica, width=799, height=26, bg='#000000', bd=2, relief='flat')
        self.frame_log_01.place(x=2, y=2)
        self.lbl_m1_01 = Label(self.frame_log_01, text="Usuário", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_01.place(x=2, y=1)
        self.lbl_m1_02 = Label(self.frame_log_01, text="NOME DA EMPRESA", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_02.place(x=300, y=1)
        self.lbl_m1_03 = Label(self.frame_log_01, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_03.place(x=600, y=1)

        self.frame_log_02 = Frame(self.tela_Logistica, width=799, height=39, bg='#000000', bd=2, relief='flat')
        self.frame_log_02.place(x=2, y=44)
        self.lbl_m1_04 = Label(self.frame_log_02, text="LOGÍSTICA", font='Georgia 16 bold', bg='#000000', fg='white')
        self.lbl_m1_04.place(x=291, y=2)

        self.frame_log_03 = Frame(self.tela_Logistica, width=190, height=300)
        self.frame_log_03.place(x=20, y=106)
        self.lbl_m1_05 = Label(self.frame_log_03, text='Cadastros',bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_05.place(x=2, y=2)

        self.frame_log_04 = Frame(self.tela_Logistica, width=190, height=300)
        self.frame_log_04.place(x=305, y=106)
        self.lbl_m1_06 = Label(self.frame_log_04, text='Movimentação', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_06.place(x=2, y=2)

        self.frame_log_05 = Frame(self.tela_Logistica, width=190, height=300)
        self.frame_log_05.place(x=592, y=106)
        self.lbl_m1_07 = Label(self.frame_log_05, text='Visualização', bg='blue', width=15, font='Georgia 14 bold', fg='white')
        self.lbl_m1_07.place(x=2, y=2)

        self.frame_log_06 = Frame(self.tela_Logistica, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_log_06.place(x=25, y=437)
        self.btn_m1_01 = Button(self.frame_log_06, text='Configuração', width=18, height=2)
        self.btn_m1_01.pack()

        self.frame_log_07 = Frame(self.tela_Logistica, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_log_07.place(x=166, y=437)
        self.btn_m1_02 = Button(self.frame_log_07, text='Manual', width=18, height=2)
        self.btn_m1_02.pack()

        self.frame_log_08 = Frame(self.tela_Logistica, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_log_08.place(x=640, y=437)
        self.btn_m1_03 = Button(self.frame_log_08, text='Fechar', width=18, height=2)
        self.btn_m1_03.pack()

        self.tela_Logistica.mainloop()

        # Tela módulo Logística
    def transporte(self):
        self.tela_Transporte = Toplevel()
        self.tela_Transporte.title('NOME DO SISTEMA')
        self.tela_Transporte.geometry("803x500+190+120")
        self.tela_Transporte.configure(bg='#FFFF00')

        self.frame_tra_01 = Frame(self.tela_Transporte, width=799, height=26, bg='#000000', bd=2, relief='flat')
        self.frame_tra_01.place(x=2, y=2)
        self.lbl_m1_01 = Label(self.frame_tra_01, text="Usuário", font='Georgia 12 bold', bg='#000000', fg='white')
        self.lbl_m1_01.place(x=2, y=1)
        self.lbl_m1_02 = Label(self.frame_tra_01, text="NOME DA EMPRESA", font='Georgia 12 bold', bg='#000000',
                               fg='white')
        self.lbl_m1_02.place(x=300, y=1)
        self.lbl_m1_03 = Label(self.frame_tra_01, text="'Dia' de 'Mês' de 'Ano'", font='Georgia 12 bold',
                               bg='#000000', fg='white')
        self.lbl_m1_03.place(x=600, y=1)

        self.frame_tra_02 = Frame(self.tela_Transporte, width=799, height=39, bg='#000000', bd=2, relief='flat')
        self.frame_tra_02.place(x=2, y=44)
        self.lbl_m1_04 = Label(self.frame_tra_02, text="TRANSPORTE", font='Georgia 16 bold', bg='#000000',
                               fg='white')
        self.lbl_m1_04.place(x=291, y=2)

        self.frame_tra_03 = Frame(self.tela_Transporte, width=190, height=300)
        self.frame_tra_03.place(x=20, y=106)
        self.lbl_m1_05 = Label(self.frame_tra_03, text='Cadastros', bg='blue', width=15, font='Georgia 14 bold',
                               fg='white')
        self.lbl_m1_05.place(x=2, y=2)

        self.frame_tra_04 = Frame(self.tela_Transporte, width=190, height=300)
        self.frame_tra_04.place(x=305, y=106)
        self.lbl_m1_06 = Label(self.frame_tra_04, text='Movimentação', bg='blue', width=15, font='Georgia 14 bold',
                               fg='white')
        self.lbl_m1_06.place(x=2, y=2)

        self.frame_tra_05 = Frame(self.tela_Transporte, width=190, height=300)
        self.frame_tra_05.place(x=592, y=106)
        self.lbl_m1_07 = Label(self.frame_tra_05, text='Visualização', bg='blue', width=15, font='Georgia 14 bold',
                               fg='white')
        self.lbl_m1_07.place(x=2, y=2)

        self.frame_tra_06 = Frame(self.tela_Transporte, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_tra_06.place(x=25, y=437)
        self.btn_m1_01 = Button(self.frame_tra_06, text='Configuração', width=18, height=2)
        self.btn_m1_01.pack()

        self.frame_tra_07 = Frame(self.tela_Transporte, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_tra_07.place(x=166, y=437)
        self.btn_m1_02 = Button(self.frame_tra_07, text='Manual', width=18, height=2)
        self.btn_m1_02.pack()

        self.frame_tra_08 = Frame(self.tela_Transporte, width=130, height=50, bg='#000000', bd=2, relief='groove')
        self.frame_tra_08.place(x=640, y=437)
        self.btn_m1_03 = Button(self.frame_tra_08, text='Fechar', width=18, height=2)
        self.btn_m1_03.pack()

        self.tela_Transporte.mainloop()


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()