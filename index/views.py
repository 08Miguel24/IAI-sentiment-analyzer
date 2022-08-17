from django.shortcuts import render



# Create your views here.
def index(request):
    if request.method == "POST":
        field_1 = request.POST['field-1']

        
        # clf = joblib.load("clf.pkl")
        # feed the request payload into perhaps a dataframe that the
        # model can take in as input
        # prediction = clf.predict(<input>)
        # context = {'output': prediction}
        context = {'output': field_1}
    else:
        context = {'output': 'none'}
    return render(request, 'index/form.html', context)








