# Batt_Power = input('Enter Batt Power : ')
# Batt_Egy = input('Enter Energy : ')
# crate = int(Batt_Power) / int(Batt_Egy)
# print(f'C-rate for specified application is {crate}')

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('logo.png')
st.image(image)

selection = st.selectbox('Calculate', ('--','c-rate','Autonomy','BESS Power','BESS Energy'))
# st.selectbox for dropdown menu

if selection == '--':
	st.info("Select a option")

elif selection =='c-rate':
	Batt_Pow = st.number_input('Enter BESS Power(in kW)')
	Batt_Egy = st.number_input('Enter BESS Energy(in kWh)')
	try: 
		crate = Batt_Pow / Batt_Egy
	except:
		st.text('Enter some value')

elif selection =='Autonomy':
	Batt_Pow = st.number_input('Enter BESS Power(in kW)')
	Batt_Egy = st.number_input('Enter BESS Energy(in kWh)')
	try: 
		autonomy = Batt_Egy / Batt_Pow
	except:
		st.text('Enter some value')

elif selection =='BESS Power':
	choice = st.radio('Select', ('c-rate','Autonomy'))
	
	if choice == 'c-rate':
		Batt_Egy = st.number_input('Enter BESS Energy(in kWh)')
		c_rate = st.number_input('Enter required c-rate')
		try:
			bess_pow = c_rate*Batt_Egy
		except:
			st.text('Enter some value')
	else:
		Batt_Egy = st.number_input('Enter BESS Energy(in kWh)',value = 0.00)
		Autonomy = st.number_input('Enter required Autonomy(in mins)')
		try:
			bess_pow = Batt_Egy/(Autonomy/60)
		except:
			st.text('Enter some value')
else:
	choice = st.radio('Select', ('c-rate','Autonomy'))
	
	if choice == 'c-rate':
		Batt_Pow = st.number_input('Enter BESS Power(in kW)')
		c_rate = st.number_input('Enter required c-rate')
		try:
			bess_egy = Batt_Pow / c_rate
		except:
			st.text('Enter some value')
	else:
		Batt_Pow = st.number_input('Enter BESS Power(in kW)')
		Autonomy = st.number_input('Enter required Autonomy(in mins)')
		try:
			bess_egy = Batt_Pow * (Autonomy/60)
		except:
			st.text('Enter some value')

if (st.button('Calculate')):
	if selection == 'c-rate':
		try: 
			st.success("c-rate is {}".format(crate))
		except:
			st.error('Enter some value')
	
	elif selection == 'Autonomy':
		try: 
			st.success("Autonomy is {} mins".format(autonomy*60))
		except:
			st.error('Enter some value')
	
	elif selection == 'BESS Power':
		if choice == 'c-rate':
			try: 
				st.success("BESS Power is {} kW".format(bess_pow))
			except:
				st.error('Enter some value')
		else:
			try: 
				st.success("BESS Power is {} kW".format(bess_pow))
			except:
				st.error('Enter some value')
	else:
		if choice == 'c-rate':
			try: 
				st.success("BESS Energy is {} kWh".format(bess_egy))
			except:
				st.error('Enter some value')
		else:
			try: 
				st.success("BESS Energy is {} kWh".format(bess_egy))
			except:
				st.error('Enter some value')


