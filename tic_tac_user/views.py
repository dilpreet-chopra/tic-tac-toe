# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json

my_dict={}
def home(request):
	return render(request,'tic_tac_design.html')


def tic_tac_toe(request):
	value=request.GET.get('Value')
	loc=request.GET.get('Id')
	my_dict[loc]=value
	print (my_dict)
	msg=''
	if ((my_dict.get('loc_1',None) =='X' and my_dict.get('loc_2',None) =='X' and my_dict.get('loc_3',None) == 'X') 
	or (my_dict.get('loc_4',None) =='X' and my_dict.get('loc_5',None) =='X' and my_dict.get('loc_6',None) == 'X') 
	or (my_dict.get('loc_7',None) =='X' and my_dict.get('loc_8',None) =='X' and my_dict.get('loc_9',None) == 'X') 
	or (my_dict.get('loc_1',None) =='X' and my_dict.get('loc_4',None) =='X' and my_dict.get('loc_7',None) == 'X') 
	or (my_dict.get('loc_2',None) =='X' and my_dict.get('loc_5',None) =='X' and my_dict.get('loc_8',None) == 'X') 
	or (my_dict.get('loc_3',None) =='X' and my_dict.get('loc_6',None) =='X' and my_dict.get('loc_9',None) == 'X') 
	or (my_dict.get('loc_1',None) =='X' and my_dict.get('loc_5',None) =='X' and my_dict.get('loc_9',None) == 'X') 
	or (my_dict.get('loc_3',None) =='X' and my_dict.get('loc_5',None) =='X' and my_dict.get('loc_7',None) == 'X')):
		msg='Congratulations! player-X you won'
		my_dict.clear()

	elif ((my_dict.get('loc_1',None) =='0' and my_dict.get('loc_2',None) =='0' and my_dict.get('loc_3',None)=='0') 
	or (my_dict.get('loc_4',None) =='0' and my_dict.get('loc_5',None) =='0' and my_dict.get('loc_6',None) == '0') 
	or (my_dict.get('loc_7',None) =='0' and my_dict.get('loc_8',None) =='0' and my_dict.get('loc_9',None) == '0') 
	or (my_dict.get('loc_1',None) =='0' and my_dict.get('loc_4',None) =='0' and my_dict.get('loc_7',None) == '0') 
	or (my_dict.get('loc_2',None) =='0' and my_dict.get('loc_5',None) =='0' and my_dict.get('loc_8',None) == '0') 
	or (my_dict.get('loc_3',None) =='0' and my_dict.get('loc_6',None) =='0' and my_dict.get('loc_9',None) == '0') 
	or (my_dict.get('loc_1',None) =='0' and my_dict.get('loc_5',None) =='0' and my_dict.get('loc_9',None) == '0') 
	or (my_dict.get('loc_3',None) =='0' and my_dict.get('loc_5',None) =='0' and my_dict.get('loc_7',None) == '0')):
		msg='Congratulations! player-0 you won'
		my_dict.clear()

	elif len(my_dict)==9:
		msg='Sorry! its a Draw'	
		my_dict.clear()

	response = HttpResponse(json.dumps(msg))	
	return response
