Algoritmo Sistema_Gestion_Financiera_Personal
	// =========================
	// DECLARACIÓN DE VARIABLES
	// =========================
	Definir ingreso_fijo, ingreso_variable, ingreso_total Como Real
	Definir gasto_alimentacion, gasto_vivienda, gasto_servicios Como Real
	Definir gasto_transporte, gasto_educacion, gasto_salud Como Real
	Definir gasto_ocio, gasto_ropa, gasto_streaming, gasto_otros Como Real
	Definir gastos_necesarios, gastos_discrecionales Como Real
	Definir ahorro_actual Como Real
	Definir porcentaje_necesarios, porcentaje_discrecionales, porcentaje_ahorro Como Real
	// =========================
	// ENTRADA DE DATOS
	// =========================
	Escribir '=== SISTEMA DE GESTIÓN FINANCIERA PERSONAL ==='
	Escribir 'Ingrese su ingreso fijo mensual:'
	Leer ingreso_fijo
	Escribir 'Ingrese su ingreso variable mensual:'
	Leer ingreso_variable
	ingreso_total <- ingreso_fijo+ingreso_variable
	Escribir ''
	Escribir '=== INGRESO DE GASTOS NECESARIOS ==='
	Escribir 'Gasto en alimentación:'
	Leer gasto_alimentacion
	Escribir 'Gasto en vivienda (alquiler o mantenimiento):'
	Leer gasto_vivienda
	Escribir 'Gasto en servicios (agua, luz, internet):'
	Leer gasto_servicios
	Escribir 'Gasto en transporte:'
	Leer gasto_transporte
	Escribir 'Gasto en educación:'
	Leer gasto_educacion
	Escribir 'Gasto en salud:'
	Leer gasto_salud
	gastos_necesarios <- gasto_alimentacion+gasto_vivienda+gasto_servicios+gasto_transporte+gasto_educacion+gasto_salud
	Escribir ''
	Escribir '=== INGRESO DE GASTOS DISCRECIONALES ==='
	Escribir 'Gasto en ocio y entretenimiento:'
	Leer gasto_ocio
	Escribir 'Gasto en ropa:'
	Leer gasto_ropa
	Escribir 'Gasto en streaming y suscripciones:'
	Leer gasto_streaming
	Escribir 'Otros gastos:'
	Leer gasto_otros
	gastos_discrecionales <- gasto_ocio+gasto_ropa+gasto_streaming+gasto_otros
	Escribir ''
	Escribir 'Ingrese el monto que destina al ahorro mensual:'
	Leer ahorro_actual
	// =========================
	// PROCESO
	// =========================
	porcentaje_necesarios <- (gastos_necesarios/ingreso_total)*100
	porcentaje_discrecionales <- (gastos_discrecionales/ingreso_total)*100
	porcentaje_ahorro <- (ahorro_actual/ingreso_total)*100
	// =========================
	// SALIDA DE RESULTADOS
	// =========================
	Escribir ''
	Escribir '=== RESUMEN FINANCIERO MENSUAL ==='
	Escribir 'Ingreso total: S/ ', ingreso_total
	Escribir 'Gastos necesarios: S/ ', gastos_necesarios, ' (', porcentaje_necesarios, '%)'
	Escribir 'Gastos discrecionales: S/ ', gastos_discrecionales, ' (', porcentaje_discrecionales, '%)'
	Escribir 'Ahorro mensual: S/ ', ahorro_actual, ' (', porcentaje_ahorro, '%)'
	Escribir ''
	Escribir '=== EVALUACIÓN SEGÚN REGLA 50?30?20 ==='
	Si porcentaje_necesarios<=50 Entonces
		Escribir 'Gastos necesarios dentro del rango recomendado.'
	SiNo
		Escribir 'Gastos necesarios superan el 50% recomendado.'
	FinSi
	Si porcentaje_discrecionales<=30 Entonces
		Escribir 'Gastos discrecionales dentro del rango recomendado.'
	SiNo
		Escribir 'Gastos discrecionales superan el 30% recomendado.'
	FinSi
	Si porcentaje_ahorro>=20 Entonces
		Escribir 'Ahorro adecuado según la regla 50?30?20.'
	SiNo
		Escribir 'Se recomienda aumentar el porcentaje de ahorro.'
	FinSi
	Escribir ''
	Escribir 'Gracias por utilizar el sistema.'
FinAlgoritmo
