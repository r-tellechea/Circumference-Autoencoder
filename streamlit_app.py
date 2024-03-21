import streamlit as st
st.set_page_config(
	page_title='Autoencoder', 
	page_icon='⚗️', 
	layout='centered', 
	initial_sidebar_state='auto'
)

# Text
from circumference_app.text import text

# Title
st.title('Autoencoder')

st.markdown(text.intro)

# Seed
seed = st.number_input(
	label='Set the manual seed:', 
	key='seed', 
	value=31415, 
	min_value=0, 
	max_value=1_000_000
)

########################################
# Data configuration
########################################

st.subheader('Crear los datos')

st.markdown(text.circumference)

from circumference_app.A_data_configuration import data_configuration
data = data_configuration(seed)

########################################
# Neural Networks Configuration
########################################

st.subheader('Arquitectura del autoencoder')

st.markdown(text.autoencoder_architecture)

from circumference_app.B_autoencoder_configuration import autoencoder_configuration
encoder_arch, decoder_arch, n_bottleneck_neurons = autoencoder_configuration(seed, data)

st.markdown(text.autoencoder_architecture_code)
# TODO: Cambiar este código dinámicamente.
with open('temporal_autoencoder_code.py') as filestream:
	st.code(filestream.read().replace('\t', '    '), language='python')

########################################
# Train the network
########################################

st.subheader('Train the networks')

from circumference_app.C_autoencoder_build_and_train import autoencoder_build_and_train
network_trained, encoder, decoder, autoencoder, loss_values = autoencoder_build_and_train(seed, data, encoder_arch, decoder_arch, n_bottleneck_neurons)

########################################
# Autoencoded data
########################################

st.subheader('Reconstruct the data with the autoencoder')

from circumference_app.D_reconstruct_data import reconstruct_data
reconstruct_data(data, autoencoder, network_trained)
