import pandas as pd
import numpy as np

target = 98 ##NILAI MASKSIMAL KESELURUHAN

## MEMBUAT DATA SET
nilai = {'NIM':['1810631103','1810631104','1810631105','1810631106','1810631107',
'1810631108','1810631109','1810631110','1810631111','1810631112',],
        'Nama': ['Eril','Cindy','Natasha','Willy','Wonka','Sabith','Ertamda',
'Biqusdi','Utultilda','Kureto'],
        'Uts': [85,90,75,60,40,65,70,35,90,78],
        'Uas' : [98,57,78,78,56,89,79,40,80,70]}

## UBAH MENJADI DATAFRAME
nilai_df = pd.DataFrame(nilai)

## MENGUBAH NILAI AKHIR DENGAN MENGALIKAN 40% UTS DAN 60% UAS
nilai["total"] = (nilai_df["Uts"]*0.4) + (nilai_df["Uas"]*0.6)
nilai_total = np.array(nilai["total"])
##print(nilai_total)

##MENAMBAH NILAI TOTAL AGAR TIDAK ADA YANG DIBAWAH B
def hitungNilai(nilai_total):
    limit_atas = 100                                        ##BATAS MAKSIMUM NILAI
    rataan_nilai = nilai_total.mean()                       ##MENCARI RATA-RATA
    tambahan_nilai = target - rataan_nilai
    nilai_baru = nilai_total + tambahan_nilai
    return np.clip(nilai_baru,nilai_total, limit_atas)      ##SIMPAN NILAI DENGAN BATASAN NP.CLIP

nilai_df['akhir'] = pd.array(hitungNilai(nilai_total))         ##MENGAMBIL FUNGSI DEF
print(nilai_df['akhir'])                                       

##MENGGANTI FUNGSI IF ELSE
nilai_df.loc[nilai_df['akhir']<= 100, 'grade'] = 'A'        ### Nilai diberi huruf
nilai_df.loc[nilai_df['akhir']<= 80, 'grade'] = 'B'         ### menambahhkan tabel grade
nilai_df.loc[nilai_df['akhir']< 70, 'grade'] = 'C'
nilai_df.loc[nilai_df['akhir']< 60, 'grade'] = 'D'
nilai_df.loc[nilai_df['akhir']< 50, 'grade'] = 'E'

print(nilai_df)
