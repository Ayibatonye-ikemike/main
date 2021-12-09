from django.shortcuts import render


# Create your views here.
def index(request):
    myclubweb = [
        {"title": "first meet",
         "location": "paris",
         "slug": "a-first-meeting"
         },
        {"title": "second meet",
         "location": "lagos",
         "slug": "a-second-meeting"
         }
    ]

    return render(request, 'myclubweb/index.html', {"show_meeting": True,
                   "meetups": myclubweb
                   })

def meetups_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup'
        }
    return render(request, 'myclubweb/meetup-detail.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })    




 
