#from django.shortcuts import render
from django.http import HttpResponse, Http404

from preguntasyrespuestas.models import Pregunta
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from preguntasyrespuestas.form import PreguntaForm

# Create your views here.
def index(request):
	preguntas = Pregunta.objects.all()
	# respuesta_string = "Preguntas <br/>"
	# respuesta_string += '<br/>'.join(["id: %s, asunto: %s" % 
	# 	(p.id, p.asunto) for p in preguntas])
	# return HttpResponse(respuesta_string)
	#print render({'preguntas': preguntas}, 'detail.html')
	return render_to_response('preguntas.html',{'preguntas': preguntas})

def pregunta_detalle(request, pregunta_id):
	# try:
	# 	pregunta = Pregunta.objects.get(pk=pregunta_id)
	# except Pregunta.DoesNotExist as dne:
	# 	print dne
	# 	raise Http404
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	#return HttpResponse("%s?" % pregunta.asunto)
	return render_to_response('pregunta_detalle.html',{'pregunta': pregunta})

def pregunta_crear(request):
	if request.method == 'POST':
		form = PreguntaForm(request.POST)
		if form.is_valid():
			# pregunta = Pregunta(asunto=form.cleaned_data['asunto'],
			# 	descripcion=form.cleaned_data['descripcion'],
			# 	fecha_publicacion=timezone.now())
			# pregunta.save()
			form.save()
			return redirect('preguntas')
	else: 
		form = PreguntaForm()	
	return render_to_response('pregunta_crear.html', 
		{'form':form},
		context_instance=RequestContext(request)) #aseguracion de las variables mandados por HTTP

def pregunta_editar(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	if request.method == 'POST':
		form = PreguntaForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect('pregunta_detalle', pregunta_id)
	else:
		form = PreguntaForm(instance=pregunta)
	return render_to_response('pregunta_editar.html',
		{'form': form},
		context_instance=RequestContext(request))