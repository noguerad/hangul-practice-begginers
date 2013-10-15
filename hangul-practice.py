#!/usr/bin/python
# -*- coding: utf-8 -*-

##### ----- Programa creado por David Noguera.
##### ----- Para contactar contacta@noguerad.es
##### ----- Muchas gracias por usar el programa.
##### ----- Si crees que lo puedes mejorar contacta y lo añado.
##### ----- Necesitas el idioma coreano como segundo idioma del SO

import os
import random
import sys
import time

LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"
os.system(LIMPIAR)

#------Versión------
version = "3.1"

#------Diccionario de letras (no presentada)------

equivavocales = {"a":'ㅏ', "ya":'ㅑ', "eo":'ㅓ', "yeo":'ㅕ', "o":'ㅗ', "yo":'ㅛ', "u":'ㅜ', "yu":'ㅠ', "eu":'ㅡ', "i":'ㅣ', "ae":'ㅐ', "yae":'ㅒ', "e":'ㅔ', "ye":'ㅖ', "wa":'ㅘ', "wae":'ㅙ', "oe":'ㅚ', "wo":'ㅝ', "we":'ㅞ', "wi":'ㅟ', "ui":'ㅢ'}
vocales = {1:"a", 2:"ya", 3:"eo", 4:"yeo", 5:"o", 6:"yo", 7:"u", 8:"yu", 9:"eu", 10:"i", 11:"ae", 12:"yae", 13:"e", 14:"ye", 15:"wa", 16:"wae", 17:"oe", 18:"wo", 19:"we", 20:"wi", 21:"ui"}
equivaconsonantes = {"gk":'ㄱ', "n":'ㄴ', "dt":'ㄷ', "rl":'ㄹ', "m":'ㅁ', "bp":'ㅂ', "st":'ㅅ', "hng":'ㅇ', "j":'ㅈ', "ch":'ㅊ', "k":'ㅋ', "t":'ㅌ', "p":'ㅍ', "h":'ㅎ', "kk":'ㄲ', "tt":'ㄸ', "pp":'ㅃ', "ss":'ㅆ', "jj":'ㅉ'}
consonantes = {1:"gk", 2:"n", 3:"dt", 4:"rl", 5:"m", 6:"bp", 7:"st", 8:"hng", 9:"j", 10:"ch", 11:"k", 12:"t", 13:"p", 14:"h", 15:"kk", 16:"tt", 17:"pp", 18:"ss", 19:"jj"}
equivadias = {"Lunes":'월요일', "Martes":'화요일', "Miércoles":'수요일', "Jueves":'목요일', "Viernes":'금요일', "Sábado":'토요일', "Domingo":'일요일'}
dias ={1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}
equivameses = {"Enero":'일월', "Febrero":'이월', "Marzo":'삼월', "Abril":'사월', "Mayo":'오월', "Junio":'육월', "Julio":'칠월', "Agosto":'팔월', "Setiembre":'구월', "Octubre":'십월', "Noviembre":'십일월', "Diciembre":'십이월'}
meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Setiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
equivanum = {"1":'하나', "2":'둘', "3":'셋', "4":'넷', "5":'다섯', "6":'여섯', "7":'일곱', "8":'여덟', "9":'아홉', "10":'열'}
numeros = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10"}

aciertos = []
errores = []
erroresdiames = []
erroresnum = []

#------Variables------
correcto = 0
incorrecto = 0

#------Constantes para loop------
a = 1
b = 1

#------Funciones------

def limpiar():			#Limpia la pantalla
	os.system(LIMPIAR)

def cabecera():			#Cabecera del programa
	os.system(LIMPIAR)
	print ("\n")
	print ("==== Programa para practicar Hangul. ====")
	print ("============== Versión " + version + " ==============\n")
	
def menu1():				#Menú si no hay intentos acertados
	cabecera()
	print ("Que te gustaría practicar? \n")
	print ("1  - Vocales")
	print ("2  - Consonantes")
	print ("3  - Mezcla Vocales y Consonantes")
	print ("4  - Días de la semana")
	print ("5  - Meses del año")
	print ("6  - Números")
	print ("0  - Salir")

def menu2():				#Menú si hay intentos acertados
	cabecera()
	print ("Que te gustaría practicar? \n")
	corr2 = str(correcto)				#Resultados correctos a string
	incorr2 = str(incorrecto)		#Resultados incorrectos a string
	print ("Respuestas correctas = "+corr2)
	print ("Respuestas incorrectas = "+incorr2)
	print (" ")
	print ("1  - Vocales")
	print ("2  - Consonantes")
	print ("3  - Mezcla Vocales y Consonantes")
	print ("4  - Días de la semana")
	print ("5  - Meses del año")
	print ("6  - Números")
	print ("7  - Ver errores cometidos")
	print ("8  - Practicar con los errores de Letras")
	print ("9  - Practicar con los errores de Días/Meses")
	print ("10 - Practicar con los errores de Números")
	print ("0  - Salir")

def explicacion():		#Explición sobre el programa
	cabecera()
	print ("El programa está diseñado para practicar: ")
	print ("   => Vocales y Consonantes. ")
	print ("   => Días y Meses. ")
	print ("   => Números ( 1 al 10 ).\n")
	raw_input(" -> Presiona 'Enter' para empezar. <- ")

def imprimen():			#Imprime los errores cometidos para practicar
	cabecera()
	print ("Escribe Salir para salir del ejercicio. \n")
	print (n)
	resp = raw_input("Escribe en coreano: ")
	return resp

def imperrores():		#Imprime la lista de errores cometidos
	cabecera()
	print ("Errores hasta ahora: \n")
	print ("Letras: ")
	print (errores)
	print ("Días/Mes: ")
	print (erroresdiames)
	print ("Números: ")
	print (erroresnum)
	print (" ")
	raw_input("-> Presiona 'Enter' para continuar. <-")			


	
#------Explicacion programa------

explicacion()

#------Menu y opciones------

while a==b :
	os.system(LIMPIAR)
	
	if correcto==0 :
		menu1()
	else:
		menu2()
	
	eleccion = raw_input(" ")

##### Vocales #####	
	if eleccion=="1" :
		for n in vocales :
			num = random.randint (1, 21)
			primera = (vocales[num])
			segunda = (equivavocales[primera])
			cabecera()
			print ("Escribe Salir para salir del ejercicio. \n")
			print (primera)
			respuesta = raw_input("Escribe la letra en coreano: ")
			if respuesta == segunda :
				print("Correcto! ")
				correcto = correcto + 1
				time.sleep(2)
			elif respuesta=="Salir":
				os.system(LIMPIAR)
				break
			else:
				print("No es correcto. ")
				errores.append(primera)
				incorrecto = incorrecto + 1
				time.sleep(2)	

##### Consonantes #####		
	elif eleccion=="2" :
		for n in consonantes :
			num = random.randint (1, 19)
			primera = (consonantes[num])
			segunda = (equivaconsonantes[primera])
			cabecera()
			print ("Escribe Salir para salir del ejercicio. \n")
			print (primera)
			respuesta = raw_input("Escribe la letra en coreano: ")
			if respuesta == segunda :
				print("Correcto! ")
				correcto = correcto + 1
				time.sleep(2)
			elif respuesta=="Salir":
				os.system(LIMPIAR)
				break
			else:
				print("No es correcto. ")
				errores.append(primera)
				incorrecto = incorrecto + 1
				time.sleep(2)	

##### vocales y consonantes #####		
	elif eleccion=="3" :
		while a==b :
			num = random.randint (1, 2)
			if num==1 :
				num = random.randint (1, 19)
				primera = (consonantes[num])
				segunda = (equivaconsonantes[primera])
				cabecera()
				print ("Escribe Salir para salir del ejercicio. \n")
				print (primera)
				respuesta = raw_input("Escribe la letra en coreano: ")
				if respuesta == segunda :
					print("Correcto! ")
					correcto = correcto + 1
					time.sleep(2)
				elif respuesta=="Salir":
					os.system(LIMPIAR)
					break
				else:
					print("No es correcto. ")
					errores.append(primera)
					incorrecto = incorrecto + 1
					time.sleep(2)
			else:
				num = random.randint (1, 21)
				primera = (vocales[num])
				segunda = (equivavocales[primera])
				cabecera()
				print ("Escribe Salir para salir del ejercicio. \n")
				print (primera)
				respuesta = raw_input("Escribe la letra en coreano: ")
				if respuesta == segunda :
					print("Correcto! ")
					correcto = correcto + 1
					time.sleep(2)
				elif respuesta=="Salir":
					os.system(LIMPIAR)
					break
				else:
					print("No es correcto. ")
					errores.append(primera)
					incorrecto = incorrecto + 1
					time.sleep(2)

##### Días #####	
	if eleccion=="4" :
		for n in dias :
			num = random.randint (1, 7)
			primera = (dias[num])
			segunda = (equivadias[primera])
			cabecera()
			print ("Escribe Salir para salir del ejercicio. \n")
			print (primera)
			respuesta = raw_input("Escribe el día en coreano: ")
			if respuesta == segunda :
				print("Correcto! ")
				correcto = correcto + 1
				time.sleep(2)
			elif respuesta=="Salir":
				os.system(LIMPIAR)
				break
			else:
				print("No es correcto. ")
				erroresdiames.append(primera)
				incorrecto = incorrecto + 1
				time.sleep(2)	

##### Meses #####
	elif eleccion=="5" :
		for n in meses :
			num = random.randint (1, 12)
			primera = (meses[num])
			segunda = (equivameses[primera])
			cabecera()
			print ("Escribe Salir para salir del ejercicio. \n")
			print (primera)
			respuesta = raw_input("Escribe el mes en coreano: ")
			if respuesta == segunda :
				print("Correcto! ")
				correcto = correcto + 1
				time.sleep(2)
			elif respuesta=="Salir":
				os.system(LIMPIAR)
				break
			else:
				print("No es correcto. ")
				erroresdiames.append(primera)
				incorrecto = incorrecto + 1
				time.sleep(2)

##### Números #####
	elif eleccion=="6" :
		for n in numeros :
			num = random.randint (1, 10)
			primera = (numeros[num])
			segunda = (equivanum[primera])
			cabecera()
			print ("Escribe Salir para salir del ejercicio. \n")
			print (primera)
			respuesta = raw_input("Escribe el número en coreano: ")
			if respuesta == segunda :
				print("Correcto! ")
				correcto = correcto + 1
				time.sleep(2)
			elif respuesta=="Salir":
				os.system(LIMPIAR)
				break
			else:
				print("No es correcto. ")
				erroresnum.append(primera)
				incorrecto = incorrecto + 1
				time.sleep(2)

##### Ver errores #####	
	elif eleccion=="7" :
		if (len(errores)>=1) or (len(erroresdiames)>=1) or (len(erroresnum)>=1) :
			imperrores()
		else:
			print("No hay errores! Buen trabajo. ")
			time.sleep(2)

##### Practicar errores letras #####			
	elif eleccion=="8" :
		while len(errores)>=1 :
			for n in errores : 	
				vo = equivavocales.has_key(n) 
				if vo==True :
					segunda = (equivavocales[n])
					respuesta = imprimen()
					if respuesta == segunda :
						print("Correcto! ")
						incorrecto = incorrecto - 1
						errores.remove(n)
						time.sleep(2)
						
					elif respuesta=="Salir":
						os.system(LIMPIAR)
						break
					else:
						print("No es correcto. ")
						#incorrecto = incorrecto + 1
						time.sleep(2)
						
				else:
					segunda = (equivaconsonantes[n])
					respuesta = imprimen()
					if respuesta == segunda :
						print("Correcto! ")
						incorrecto = incorrecto - 1
						errores.remove(n)
						time.sleep(2)
						
					elif respuesta=="Salir":
						os.system(LIMPIAR)
						break
					else:
						print("No es correcto. ")
						#incorrecto = incorrecto + 1
						time.sleep(2)	

##### Practicar errores dias/mes #####
	elif eleccion=="9" :
		while len(erroresdiames)>=1 :
			for n in erroresdiames : 	
				vo = equivadias.has_key(n) 
				if vo==True :
					segunda = (equivadias[n])
					respuesta = imprimen()
					if respuesta == segunda :
						print("Correcto! ")
						incorrecto = incorrecto - 1
						erroresdiames.remove(n)
						time.sleep(2)
						
					elif respuesta=="Salir":
						os.system(LIMPIAR)
						break
					else:
						print("No es correcto. ")
						#incorrecto = incorrecto + 1
						time.sleep(2)
						
				else:
					segunda = (equivames[n])
					respuesta = imprimen()
					if respuesta == segunda :
						print("Correcto! ")
						incorrecto = incorrecto - 1
						erroresdiames.remove(n)
						time.sleep(2)
						
					elif respuesta=="Salir":
						os.system(LIMPIAR)
						break
					else:
						print("No es correcto. ")
						#incorrecto = incorrecto + 1
						time.sleep(2)

##### Practicar errores Números #####
	elif eleccion=="10" :
		while len(erroresnum)>=1 :
			for n in erroresnum : 	
				segunda = (equivanum[n])
				respuesta = imprimen()
				if respuesta == segunda :
					print("Correcto! ")
					incorrecto = incorrecto - 1
					erroresnum.remove(n)
					time.sleep(2)
					
				elif respuesta=="Salir":
					os.system(LIMPIAR)
					break
				else:
					print("No es correcto. ")
					#incorrecto = incorrecto + 1
					time.sleep(2)

##### Salir #####	
	elif eleccion=="0" :
		break	

##### Error de selección #####
# Lo dejo sin sleep para que no se vea, por ahora. Me gusta más así.		
	else :
		print ("La opción no és válida. ")
		print ("Debes elegir una opción. ")
		#time.sleep(1)

os.system(LIMPIAR)




	






