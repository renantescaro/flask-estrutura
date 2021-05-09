from datetime import datetime as dt

class Converter:
    def ms_para_kh(self, metros_por_segundo):
        return (float(metros_por_segundo) * 3.6)


    def data_atual_string(self):
        data_hoje = dt.today()
        return str(data_hoje.strftime('%d/%m/%Y %H:%M:%S'))