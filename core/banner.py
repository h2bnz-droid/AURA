from datetime import datetime

def show_banner():

    print("="*55)
    print("            AURA AI Companion")
    print("             Version 0.0.2")
    print("="*55)

    print("Tanggal :", datetime.now().strftime("%d-%m-%Y"))
    print("Status  : Online")
    print("Model   : Gemma")
    print("="*55)