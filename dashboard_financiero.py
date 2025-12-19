import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Financiero Personal",
    page_icon="💰",
    layout="wide"
)

# Título principal
st.title("💰 Sistema de Gestión Financiera Personal")
st.markdown("---")

# Sidebar para ingresos
st.sidebar.header("📊 Ingresos Mensuales")
ingreso_fijo = st.sidebar.number_input("Ingreso fijo mensual (S/)", min_value=0.0, value=3000.0, step=100.0)
ingreso_variable = st.sidebar.number_input("Ingreso variable mensual (S/)", min_value=0.0, value=500.0, step=100.0)
ingreso_total = ingreso_fijo + ingreso_variable

st.sidebar.markdown(f"**Ingreso Total: S/ {ingreso_total:.2f}**")
st.sidebar.markdown("---")

# Sección de gastos necesarios
st.sidebar.header("🏠 Gastos Necesarios")
gasto_vivienda = st.sidebar.number_input("Vivienda/Alquiler (S/)", min_value=0.0, value=800.0, step=50.0)
alimentacion = st.sidebar.number_input("Alimentación (S/)", min_value=0.0, value=600.0, step=50.0)
servicios = st.sidebar.number_input("Servicios (agua, luz, internet) (S/)", min_value=0.0, value=200.0, step=50.0)
transporte = st.sidebar.number_input("Transporte (S/)", min_value=0.0, value=150.0, step=50.0)
educacion = st.sidebar.number_input("Educación (S/)", min_value=0.0, value=200.0, step=50.0)
salud = st.sidebar.number_input("Salud (S/)", min_value=0.0, value=150.0, step=50.0)

gastos_necesarios = sum([alimentacion, gasto_vivienda, servicios, transporte, educacion, salud])

st.sidebar.markdown("---")

# Sección de gastos discrecionales
st.sidebar.header("🎮 Gastos Discrecionales")
ocio = st.sidebar.number_input("Ocio y entretenimiento (S/)", min_value=0.0, value=300.0, step=50.0)
ropa = st.sidebar.number_input("Ropa (S/)", min_value=0.0, value=150.0, step=50.0)
streaming = st.sidebar.number_input("Streaming y suscripciones (S/)", min_value=0.0, value=80.0, step=10.0)
otros = st.sidebar.number_input("Otros gastos (S/)", min_value=0.0, value=100.0, step=50.0)

gastos_discrecionales = sum([ocio, ropa, streaming, otros])

st.sidebar.markdown("---")

# Ahorro
st.sidebar.header("💵 Ahorro")
ahorro = st.sidebar.number_input("Monto destinado al ahorro (S/)", min_value=0.0, value=500.0, step=50.0)

# Cálculos principales
total_gastos = gastos_necesarios + gastos_discrecionales
balance = ingreso_total - total_gastos - ahorro

porc_necesarios = (gastos_necesarios / ingreso_total) * 100 if ingreso_total > 0 else 0
porc_discrecionales = (gastos_discrecionales / ingreso_total) * 100 if ingreso_total > 0 else 0
porc_ahorro = (ahorro / ingreso_total) * 100 if ingreso_total > 0 else 0

# Regla 50-30-20
ideal_necesarios = ingreso_total * 0.50
ideal_discrecionales = ingreso_total * 0.30
ideal_ahorro = ingreso_total * 0.20

margen_necesarios = ideal_necesarios - gastos_necesarios
margen_discrecionales = ideal_discrecionales - gastos_discrecionales
margen_ahorro = ideal_ahorro - ahorro

# Dashboard principal
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Ingreso Total", f"S/ {ingreso_total:.2f}")

with col2:
    st.metric("Gastos Totales", f"S/ {total_gastos:.2f}")

with col3:
    st.metric("Ahorro", f"S/ {ahorro:.2f}", f"{porc_ahorro:.1f}%")

with col4:
    color = "normal" if balance >= 0 else "inverse"
    st.metric("Balance", f"S/ {balance:.2f}", delta_color=color)

st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribución de Ingresos")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    categorias = ["Necesarios", "Discrecionales", "Ahorro"]
    valores = [gastos_necesarios, gastos_discrecionales, ahorro]
    ideales = [ideal_necesarios, ideal_discrecionales, ideal_ahorro]
    
    x = range(len(categorias))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], valores, width, label='Real', color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax.bar([i + width/2 for i in x], ideales, width, label='Ideal (50-30-20)', color=['#FFA07A', '#98D8C8', '#87CEEB'], alpha=0.7)
    
    ax.set_ylabel('Monto (S/)')
    ax.set_title('Comparación: Real vs Ideal (Regla 50-30-20)')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    st.pyplot(fig)

with col2:
    st.subheader("🥧 Distribución Porcentual")
    
    fig, ax = plt.subplots(figsize=(8, 8))
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    if sum([gastos_necesarios, gastos_discrecionales, ahorro]) > 0:
        ax.pie(
            [gastos_necesarios, gastos_discrecionales, ahorro],
            labels=["Necesarios", "Discrecionales", "Ahorro"],
            autopct='%1.1f%%',
            startangle=90,
            colors=colores
        )
        ax.set_title('Distribución del Ingreso')
    else:
        ax.text(0.5, 0.5, 'Sin datos', ha='center', va='center', transform=ax.transAxes)
    
    st.pyplot(fig)

st.markdown("---")

# Recomendaciones
st.subheader("💡 Recomendaciones según la Regla 50-30-20")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏠 Gastos Necesarios")
    st.markdown(f"**Real:** {porc_necesarios:.1f}% | **Ideal:** 50%")
    if margen_necesarios >= 0:
        st.success(f"✅ Gastos adecuados. Margen disponible: S/ {margen_necesarios:.2f}")
    else:
        st.error(f"⚠️ Gastos excedidos en S/ {abs(margen_necesarios):.2f}. Reducir gastos fijos.")

with col2:
    st.markdown("### 🎮 Gastos Discrecionales")
    st.markdown(f"**Real:** {porc_discrecionales:.1f}% | **Ideal:** 30%")
    if margen_discrecionales >= 0:
        st.success(f"✅ Gastos controlados. Margen disponible: S/ {margen_discrecionales:.2f}")
    else:
        st.warning(f"⚠️ Gastos excedidos en S/ {abs(margen_discrecionales):.2f}. Moderar gastos.")

with col3:
    st.markdown("### 💵 Ahorro")
    st.markdown(f"**Real:** {porc_ahorro:.1f}% | **Ideal:** 20%")
    if margen_ahorro <= 0:
        st.success(f"✅ Nivel de ahorro adecuado.")
    else:
        st.info(f"💡 Incrementar ahorro en al menos S/ {margen_ahorro:.2f}")

st.markdown("---")

# Tabla detallada
st.subheader("📋 Detalle de Gastos Mensuales")

datos_tabla = {
    "Categoría": [
        "Vivienda", "Alimentación", "Servicios", "Transporte", 
        "Educación", "Salud", "Ocio", "Ropa", "Streaming", "Otros"
    ],
    "Monto (S/)": [
        gasto_vivienda, alimentacion, servicios, transporte,
        educacion, salud, ocio, ropa, streaming, otros
    ],
    "Tipo": [
        "Necesario", "Necesario", "Necesario", "Necesario",
        "Necesario", "Necesario", "Discrecional", "Discrecional",
        "Discrecional", "Discrecional"
    ]
}

df = pd.DataFrame(datos_tabla)
st.dataframe(df, use_container_width=True)

# Resumen final
st.markdown("---")
st.subheader("📊 Resumen Financiero")

resumen_col1, resumen_col2 = st.columns(2)

with resumen_col1:
    st.markdown(f"""
    - **Ingreso Total:** S/ {ingreso_total:.2f}
    - **Gastos Necesarios:** S/ {gastos_necesarios:.2f} ({porc_necesarios:.1f}%)
    - **Gastos Discrecionales:** S/ {gastos_discrecionales:.2f} ({porc_discrecionales:.1f}%)
    """)

with resumen_col2:
    st.markdown(f"""
    - **Ahorro:** S/ {ahorro:.2f} ({porc_ahorro:.1f}%)
    - **Gasto Total:** S/ {total_gastos:.2f}
    - **Balance Final:** S/ {balance:.2f}
    """)

# Footer
st.markdown("---")
st.markdown(f"*Fecha de elaboración: {datetime.now().strftime('%d/%m/%Y')}*")
st.markdown("*Dashboard basado en la Regla 50-30-20 de gestión financiera*")