"""Test for my functions."""

import random
from functions import begin_character, cyan_saber, emitter, finish


def test_begin_character():

	assert callable(begin_character)
	assert begin_character is not None

def test_cyan_saber():
	assert callable(cyan_saber)
	assert cyan_saber is not None

def test_emitter():
	assert callable(emitter)
	assert emitter is not None


def test_finish():

    	assert callable(finish)
	assert finish is not None
	assert finish('Darth', 'Jacob', 'curved-handled', 'blue', 'magus', 'BB') == 	"Generated character: Darth Jacob who wields a curved-handled blue" 
	+ " lightsaber with a magus emitter, and a BB companion."


#!pytest test_functions/
    



                 
    