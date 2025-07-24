import os
import json
import random
import string
file_path="kayit2.json"
def veri_yukle():
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
             return json.load(file)
    return {}
def veri_kaydet(belge):
    with open(file_path,"w") as file:
        json.dump(belge,file)

def sifre_uretim(belge,uygulama,username,password):
    if uygulama in belge:
        return "zaten bu var"
    else:
        belge[uygulama]={"username":username,"password":password}
        veri_kaydet(belge)
        return "veri kaydedildi"


def sifre_arama(belge,uygulama):
    if uygulama in belge:
        for line in belge[uygulama]:
            return f"{belge[uygulama][line]}: {belge[uygulama]['password']}"
def sifre_onerisi(uzunluk):
    if uzunluk < 8:
        print("⚠️ Güvenli olması için şifre en az 8 karakter olmalı.")
        return None

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))#list Comprehensions
    return sifre

