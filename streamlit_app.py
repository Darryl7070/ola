import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import random as rn
import os as o

def Generar_Ingresos():
    mes = ["1-Enero","2-Febrero","3-Marzo","4-Abril","5-Mayo","6-Junio","7-Julio","8-Agosto","9-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
    MontoMensual = 0
    for i in range(2000,2025):
        if not o.path.exists(f"Proyecto1\IngresosMensuales\Año {i}"):
            o.mkdir(f"Proyecto1\IngresosMensuales\Año {i}")
        
        for x in range(12):
            if not o.path.exists(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}"):
                o.mkdir(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}")
                Archivo = open(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}\IngresosDelMes.txt","x")

            Archivo = open(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}\IngresosDelMes.txt","w")
            if MontoMensual == 0:
                MontoMensual = rn.randint(1000,10000)
            
            else:
                MontoMensual = rn.randint(int(MontoMensual * 0.9),int(MontoMensual * 1.1))
                print(MontoMensual)
            
            Archivo.write(str(MontoMensual))

Generar_Ingresos()
