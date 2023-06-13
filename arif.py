import streamlit as st
from streamlit_option_menu import option_menu
import math
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


with st.sidebar :
    selected = option_menu ("Pilih Jenis Rangkaian OP-AMP",
    ["Home",
    "Non-Inverting Amplifier",
    "Inverting Amplifier",],
    default_index=0)

if(selected == "Home") :
    st.header("Kalkulator Perhitungan Vo pada OP-AMP dan Sinyal Output Hasil Keluaran")
    st.subheader("By Arif Tresnadi (11-2021-018)")
    st.write("Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T")
   
if(selected == "Non-Inverting Amplifier") :
    st.title("Contoh Rangkaian Non-Inverting Amplifier")
    st.image("fixed1.jpg", width = 500)
    st.subheader("Perhitungan Vo dan Sinyal Output pada Rangkaian Non-Inverting Amplifier")

    a=st.number_input("Masukkan Nilai VCC (Volt)",0)
    b=st.number_input("Masukkan Nilai Rf (Ohm)",0)
    c=st.number_input("Masukkan Nilai R1 (Ohm)",0)
    g=st.number_input("Masukkan nilai Vi (Volt)",0)
    z=st.number_input("Masukkan nilai frekuensi Vi (Hz)")
    hitung = st.button("Vo dan Sinyal Output")

    if hitung :
        vo = (1+(b/c))*g
        av = (1+(b/c))
        st.write("HASIL PERHITUNGAN NILAI VO")
        st.write(f"Nilai Penguatan Tegangan = {av} kali")
        st.write(f"Nilai VO = {vo} Volt")
        
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = g * np.sin(2 * np.pi * z * t + np.deg2rad(phase_shift))
            hasil_Vo = vo * np.sin(2 * np.pi * z * t + np.deg2rad(phase_shift))

            if hitung:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)
                ax1.set_xlim(-0.05,0.05)
                
                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)

                plt.xlim(-0.05, 0.05)
                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()


if(selected == "Inverting Amplifier") :
    st.title("Contoh Rangkaian Inverting Amplifier")
    st.image("fixed.jpg", width = 500)
    st.subheader("Perhitungan Vo dan Sinyal Output pada Rangkaian Inverting Amplifier")

    a=st.number_input("Masukkan Nilai VCC (Volt)",0)
    b=st.number_input("Masukkan Nilai Rf (Ohm)",0)
    c=st.number_input("Masukkan Nilai R1 (Ohm)",0)
    g=st.number_input("Masukkan nilai Vi (Volt)",0)
    z=st.number_input("Masukkan nilai frekuensi Vi (Hz)")
    hitung = st.button("Vo dan Sinyal Output")

    if hitung :
        vo = -(b/c)*g
        av = (b/c)
        st.write("HASIL PERHITUNGAN NILAI VO")
        st.write(f"Nilai Penguatan Tegangan = {av} kali")
        st.write(f"Nilai VO = {vo} Volt")
        
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = g * np.sin(2 * np.pi * z * t + np.deg2rad(phase_shift))
            hasil_Vo = -1 * vo * np.sin(2 * np.pi * z * t )

            if hitung:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)
                ax1.set_xlim(-0.05,0.05)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)

                plt.xlim(-0.05, 0.05)
                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()
