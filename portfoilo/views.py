import requests
from django.shortcuts import render
from django.views import View


from .forms import ContactForm
from blog import *

def get_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    except:
        return 'Failed to load'

def get_country_flag():
    try:
        ip_address = get_ip()
        # country_response = requests.get('http://ip-api.com/json/?fields=status,message,country,countryCode').json()
        country_response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        country = country_response['country_name']
        country_code = country_response['country_code']
        flag_response = requests.get(f'https://countryflagsapi.com/svg/{country}').text
        return (flag_response, country, country_code)
    except:
        return ('', '', '')


def random_link(portfolio_data):
    import random
    links = [data['link'] for data in portfolio_data if data['link'] != None]
    chosen_link = random.choice(links)
    return chosen_link

from .data import experties, portfolio, testimonials, blog_posts

experties_data = experties
portfolio_data = portfolio
testimonials_data = testimonials
latest_posts = blog_posts[:3]


class PortfolioView(View):

    def get(self, request):
        
        form = ContactForm()

        country_d = get_country_flag()
        random_p_link = random_link(portfolio_data)

        return render(request, 'portfolio/index.html', {
            'form': form,
            'experties_show': experties_data[:3],
            'experties_hide': experties_data[3:],
            'portfolio_data': portfolio_data,
            'testimonials_data': testimonials_data,
            'blog_posts': latest_posts,
            'country_pic': country_d[0],
            'country_name': country_d[1],
            'country_code': country_d[2],
            'random_portfolio_link':  random_p_link,
        })
    

    def post(self, request):
        form = ContactForm(request.POST)

        country_d = get_country_flag()
        random_p_link = random_link(portfolio_data)


        if form.is_valid():
            import smtplib

            user_name = form.cleaned_data['name']
            my_email = "gorgeoustomisin@gmail.com"
            password = "wappucglnhtfimbm"
            receiver_email = 'tomisinerinle4@gmail.com'
            msg_to_send = f"Name: {user_name}, \n User Email: {form.cleaned_data['email']}, \n Message: {form.cleaned_data['message']} \n country: {get_country_flag()[1]} "
            
            try:

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr = my_email,
                        to_addrs = receiver_email,
                        msg = f"Subject: {user_name} Contacting Me \n\n {msg_to_send}")

                success_msg = f"""
                                Thank You Mr/Mrs {user_name},</br>
                                For trying me out,</br>
                                I will try to get back to you as soon as i see your message,

                                Once again thank you for choosing Me.
                            """
                return render(request, 'portfolio/success.html', {'msg': success_msg})

            except:
                return render(request, 'portfolio/error.html', {'msg': 'Something came up while connecting to the server.'})

        
        return render(request, 'portfolio/index.html', {
            'form': form,
            'experties_show': experties_data[:3],
            'experties_hide': experties_data[3:],
            'portfolio_data': portfolio_data,
            'testimonials_data': testimonials_data,
            'blog_posts': latest_posts,
            'country_pic': country_d[0],
            'country_name': country_d[1],
            'country_code': country_d[2],
            'random_portfolio_link':  random_p_link,
        })

# def blog(request):
#     template_name="blog/index.html"
#     return render(request,template_name)    

