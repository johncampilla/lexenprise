from django.shortcuts import render
from dataconversion.models import egazette

# Create your views here.

def gazettelist(request):
    publications = egazette.objects.all()


    context = {
        'gazette' : publications,
    }

    return render(request, 'tmwatch/publicationlist.html', context)

# def clientlist(request):
#     access_code = request.user.user_profile.userid
#     user_id = User.id

#     user_message_id = request.user.user_profile.id
#     alertmessages = inboxmessage.objects.filter(
#         messageto_id=user_message_id, status="UNREAD")
#     countalert = alertmessages.count()
#     srank = request.user.user_profile.rank
#     username = request.user.username

#     if 'q' in request.GET:
#         q = request.GET['q']
#         #clients = Client_Data.objects.filter(client_name__icontains=q)
#         multiple_q = Q(Q(client_name__icontains=q) | Q(main_contact__icontains=q) | Q(email__icontains=q) | Q(
#             address__icontains=q) | Q(industry__industry__icontains=q) | Q(status__icontains=q) | Q(country__country__icontains=q))
#         clients = Client_Data.objects.filter(
#             multiple_q).order_by("client_name")
#     else:
#         clients = Client_Data.objects.all().order_by("client_name")

#     noofclients = clients.count()
#     paginator = Paginator(clients, 11)
#     page = request.GET.get('page')
#     all_clients = paginator.get_page(page)

#     context = {
#         'page': page,
#         'noofclients': noofclients,
#         'clients': all_clients,
#         'alertmessages': alertmessages,
#         'noofalerts': countalert,
#         'username': username,
#     }

#     return render(request, 'adminapps/clientlist.html', context)

