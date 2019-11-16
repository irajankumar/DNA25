from django.shortcuts import render
from . import dna_analyzer as da
# Create your views here.

def index(req):
    if req.method == 'POST':
        # we got the input from user
        dna = req.POST["dna"]
        # cleaning dna 
        mod_dna = ""
        for i in dna:
            if i.isalpha():
                mod_dna += i
        protin = da.generate_protin(mod_dna)
        message = ""
        if protin == "":
            message = "This doesnt looks like a valid DNA sample."
        else:
            message = "Protin structure result is ready."

        return render(req, 'dmain/index.html', {'ans':protin, 'message': message})
    return render(req, 'dmain/index.html')