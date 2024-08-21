# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:40:00 2024

@author: Burcu İRAN
"""


##########################################################################
import pandas as pd
import os

def single_file_import(file_path, a=0, b=None):
    """
    Verilen dosya yolundan uygun dosya türünü oku ve belirli bir aralıktaki satırları döndür.
    
    Parameters:
    file_path (str): Dosyanın yolu. Desteklenen uzantılar: .csv, .xlsx, .xls, .txt, .json, .html, .parquet, .feather, .orc, .dta, .sas7bdat, .sav, .h5, .pkl, .xml.
    a (int, optional): Başlangıç satır indeksi, varsayılan 0.
    b (int, optional): Bitiş satır indeksi, varsayılan None (son satıra kadar).
    
    Returns:
    DataFrame: Dosya verileri. Dosya bulunamazsa veya okunamazsa None döner.
    """
    try:
        # Dosya uzantısını belirler
        _, file_extension = os.path.splitext(file_path)
        
        # Dosya uzantısına göre uygun pandas okuma fonksiyonunu kullanır
        if file_extension == '.csv':
            veri = pd.read_csv(file_path)
        elif file_extension in ['.xlsx', '.xls']:
            veri = pd.read_excel(file_path)
        elif file_extension == '.txt':
            veri = pd.read_csv(file_path, delimiter='\t')
        elif file_extension == '.json':
            veri = pd.read_json(file_path)
        elif file_extension == '.html':
            veri = pd.read_html(file_path)[0]  # HTML'deki ilk tabloyu okur
        elif file_extension == '.parquet':
            veri = pd.read_parquet(file_path)
        elif file_extension == '.feather':
            veri = pd.read_feather(file_path)
        elif file_extension == '.orc':
            veri = pd.read_orc(file_path)
        elif file_extension == '.dta':
            veri = pd.read_stata(file_path)
        elif file_extension == '.sas7bdat':
            veri = pd.read_sas(file_path)
        elif file_extension == '.sav':
            veri = pd.read_spss(file_path)
        elif file_extension == '.h5':
            veri = pd.read_hdf(file_path)
        elif file_extension == '.pkl':
            veri = pd.read_pickle(file_path)
        elif file_extension == '.xml':
            veri = pd.read_xml(file_path)
        else:
            print(f"Hata: Desteklenmeyen dosya türü -> {file_extension}")
            return None
        
        # Belirtilen satır aralığını döndürür
        return veri.iloc[a:b]
    
    except FileNotFoundError:
        print(f"Hata: Dosya bulunamadı -> {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Hata: Dosya boş -> {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Hata: Dosya bir tablo olarak ayrıştırılamadı -> {file_path}")
        return None
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}")
        return None


###########################################################################

