from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import random

from .models import user_info, vice_President_vote_count, President_vote_count, senator_vote_count
from django.contrib import messages


from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        return render(request, 'index.html')
    return render(request, 'login_registration.html')

def login_rigister(request):
    return render(request, 'login_registration.html')







@csrf_exempt
def check_the_otp(request):

    if request.method == 'POST':  # This is a POST Request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print('email')
        print(email)
        emal_add = email



        otp_num = random.randint(11111, 99999)
        generated_otp_num_str = str(otp_num)
        print('generated_otp_num_str')
        print(generated_otp_num_str)

        email_for_otp = render_to_string(
            'otp_send_email.html',
            {
                'generated_otp_num_str': generated_otp_num_str,

            }
        )

        send_mail(
            'Election Poll - Thank You',  # subject
            email_for_otp,  # massage
            '',  # from email
            [emal_add],  # to email
            fail_silently=True,
        )




        contex = {
            'username':username,
            'email':email,
            'password1':password1,
            'generated_otp_num_str':generated_otp_num_str,

        }
        return render(request, 'otp_filed.html', contex)


    else:
        return render(request, 'users/register.html')







def save_the_user_info(request):
    if request.method == 'POST':  # This is a POST Request
        username = request.POST.get('username_2')
        email = request.POST.get('email_2')
        password1 = request.POST.get('password1_2')

        get_info = user_info(Mobel_User_Name=username, Mobel_Email_Address=email, Mobel_Password=password1)
        get_info.save()

        return redirect('login_rigister')

    else:
        return render(request, 'login_registration.html')





@csrf_exempt
def check_login_info(request):
    print('i am muuuuuuuuu')

    if request.method == 'POST':  # This is a POST Request
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('i am m mma')

        k = user_info.objects.filter(Mobel_User_Name=username)
        if k:
            l = user_info.objects.get(Mobel_User_Name=username)
            print('l.Mobel_Password')
            print(l.Mobel_Password)
            if l.Mobel_Password == password:
                request.session['session_user_id'] = l.id
                print('i am m 2222222222')
                return redirect('index')
            else:
                m = 'Password are not match!'
        else:
            m = 'username are not match!'


        return render(request, 'login_registration.html', {'m': m})

    else:
        return redirect('login_rigister')


@csrf_exempt
def logout(request):
    request.session.clear()
    return redirect('login_rigister')


def forget_pass(request):
    print('ikkkk')
    return render(request, 'forget_pass.html')



def profile(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        u = user_info.objects.get(id=session_user_id)
        contex = {
            'u':u,
        }
        return render(request, 'profile.html', contex)

    return redirect('login_rigister')

@csrf_exempt
def lets_save(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = user_info.objects.get(id=session_user_id)
        u.Mobel_User_Name = username
        u.Mobel_Email_Address = email
        u.Mobel_Password = password
        u.save()
        return redirect('index')

    return redirect('login_rigister')




@csrf_exempt
def reset_pass(request):
    if request.method == 'POST':
        reset_user = request.POST.get('reset_user')
        otp_num = random.randint(11111, 99999)
        generated_otp_num_str = str(otp_num)
        print('generated_otp_num_str')
        print(generated_otp_num_str)
        emal_add=reset_user
        # send a email here

        email_for_otp = render_to_string(
            'otp_send_email.html',
            {
                'generated_otp_num_str': generated_otp_num_str,

            }
        )

        send_mail(
            'Election Poll - Thank You',  # subject
            email_for_otp,  # massage
            '',  # from email
            [emal_add],  # to email
            fail_silently=True,
        )


        contex = {
            'generated_otp_num_str':generated_otp_num_str,
            'reset_user':reset_user,

        }
        return render(request, 'reset_pass_otp.html', contex)

    return redirect('login_rigister')





@csrf_exempt
def type_reset_pass(request):
    if request.method == 'POST':
        print('ooooooo')
        reset_user = request.POST.get('reset_user')
        print('ppppp')
        contex = {
            'reset_user':reset_user,
        }

        return render(request, 'type_reset_pass.html', contex)

    return redirect('login_rigister')




@csrf_exempt
def savereset_pass(request):
    if request.method == 'POST':

        reset_user = request.POST.get('reset_user')
        password = request.POST.get('password')
        print('reset_user')
        print(reset_user)

        k = user_info.objects.filter(Mobel_Email_Address=reset_user)
        print('k')
        print(k)
        if k:
            kk = user_info.objects.get(Mobel_Email_Address=reset_user)
            print('kk')
            print(kk)
            kk.Mobel_Password = password
            kk.save()

        return redirect('login_rigister')

    return redirect('login_rigister')






# all voting part and result here



@csrf_exempt
def go_for_poll(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        user = user_info.objects.get(id=session_user_id)
        is_present = vice_President_vote_count.objects.filter(user_con=user)
        is_President_present = President_vote_count.objects.filter(user_con=user)
        is_senator_present = senator_vote_count.objects.filter(user_con=user)
        print('user')
        print(user)
        print('is_present')
        print(is_present)
        vice_President = ''
        if is_present:
            print('i mmmp ooo')
            vice_President='yes'

        President=''
        if is_President_present:

            President = 'yes'
        senator=''
        if is_senator_present:
            senator = 'yes'

        contex = {
            'vice_President':vice_President,
            'President':President,
            'senator':senator,
        }
        return render(request, 'go_for_poll.html', contex)

    return redirect('login_rigister')


@csrf_exempt
def Vice_President_vote(request):
    print('dd')
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        user = user_info.objects.get(id=session_user_id)
        is_present = vice_President_vote_count.objects.filter(user_con=user)
        if is_present:

            return redirect('go_for_poll')
        else:
            return render(request, 'Vice_President_vote.html')




    return redirect('login_rigister')




@csrf_exempt
def save_the_v_p_v(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        if request.method == 'POST':
            choice = request.POST.get('choice')
            user = user_info.objects.get(id=session_user_id)
            save_vote = vice_President_vote_count(user_con=user, person_get_vote=choice)
            save_vote.save()
            return redirect('go_for_poll')
        else:
            return render(request, 'Vice_President_vote.html')
    return redirect('login_rigister')







@csrf_exempt
def Vice_President_result(request):

    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        k = vice_President_vote_count.objects.all()
        one=0
        two=0
        three=0
        four=0
        five=0
        six=0
        seven=0
        eight=0
        nine=0
        ten=0
        el_11=0
        t_12=0
        for i in k:
            if i.person_get_vote == '1':
                one = one+1
            if i.person_get_vote == '2':
                two = two+1
            if i.person_get_vote == '3':
                three = three+1
            if i.person_get_vote == '4':
                four = four+1
            if i.person_get_vote == '5':
                five = five+1
            if i.person_get_vote == '6':
                six = six+1
            if i.person_get_vote == '7':
                seven = seven+1
            if i.person_get_vote == '8':
                eight = eight+1
            if i.person_get_vote == '9':
                nine = nine+1
            if i.person_get_vote == '10':
                ten = ten+1
            if i.person_get_vote == '11':
                el_11 = el_11+1
            if i.person_get_vote == '12':
                t_12 = t_12+1
        contex = {
            'one':one,
            'two':two,
            'three':three,
            'four':four,
            'five':five,
            'six':six,
            'seven':seven,
            'eight':eight,
            'nine':nine,
            'ten':ten,
            'el_11':el_11,
            't_12':t_12,

        }
        return render(request, 'Vice_President_result.html', contex)
    return redirect('login_rigister')



@csrf_exempt
def President_vote(request):

    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        return render(request, 'President_vote.html')
    return redirect('login_rigister')


@csrf_exempt
def save_the_president_v(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        if request.method == 'POST':
            choice = request.POST.get('choice')
            user = user_info.objects.get(id=session_user_id)
            save_vote = President_vote_count(user_con=user, person_get_vote=choice)
            save_vote.save()
            return redirect('go_for_poll')
        else:
            return redirect('go_for_poll')
    return redirect('login_rigister')



@csrf_exempt
def President_result(request):
    print('dd')
    session_user_id = request.session.get('session_user_id')
    if session_user_id:

        k = President_vote_count.objects.all()
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        ten = 0
        el_11 = 0
        t_12 = 0
        for i in k:
            if i.person_get_vote == '1':
                one = one + 1
            if i.person_get_vote == '2':
                two = two + 1
            if i.person_get_vote == '3':
                three = three + 1
            if i.person_get_vote == '4':
                four = four + 1
            if i.person_get_vote == '5':
                five = five + 1
            if i.person_get_vote == '6':
                six = six + 1
            if i.person_get_vote == '7':
                seven = seven + 1
            if i.person_get_vote == '8':
                eight = eight + 1
            if i.person_get_vote == '9':
                nine = nine + 1
            if i.person_get_vote == '10':
                ten = ten + 1
            if i.person_get_vote == '11':
                el_11 = el_11 + 1
            if i.person_get_vote == '12':
                t_12 = t_12 + 1
        contex = {
            'one': one,
            'two': two,
            'three': three,
            'four': four,
            'five': five,
            'six': six,
            'seven': seven,
            'eight': eight,
            'nine': nine,
            'ten': ten,
            'el_11': el_11,
            't_12': t_12,

        }

        return render(request, 'President_result.html', contex)
    return redirect('login_rigister')



@csrf_exempt
def Senator_vote(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        return render(request, 'Senator_vote.html')
    return redirect('login_rigister')




@csrf_exempt
def save_the_sanetor_v(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        if request.method == 'POST':
            Sanator_1 = request.POST.get('Sanator_1')
            Sanator_2 = request.POST.get('Sanator_2')
            Sanator_3 = request.POST.get('Sanator_3')
            Sanator_4 = request.POST.get('Sanator_4')
            Sanator_5 = request.POST.get('Sanator_5')
            Sanator_6 = request.POST.get('Sanator_6')
            Sanator_7 = request.POST.get('Sanator_7')
            Sanator_8 = request.POST.get('Sanator_8')
            Sanator_9 = request.POST.get('Sanator_9')
            Sanator_10 = request.POST.get('Sanator_10')
            Sanator_11 = request.POST.get('Sanator_11')
            Sanator_12 = request.POST.get('Sanator_12')
            Sanator_13 = request.POST.get('Sanator_13')
            Sanator_14 = request.POST.get('Sanator_14')
            Sanator_15 = request.POST.get('Sanator_15')
            Sanator_16 = request.POST.get('Sanator_16')
            Sanator_17 = request.POST.get('Sanator_17')
            Sanator_18 = request.POST.get('Sanator_18')
            Sanator_19 = request.POST.get('Sanator_19')
            Sanator_20 = request.POST.get('Sanator_20')
            Sanator_21 = request.POST.get('Sanator_21')
            Sanator_22 = request.POST.get('Sanator_22')
            Sanator_23 = request.POST.get('Sanator_23')
            Sanator_24 = request.POST.get('Sanator_24')
            Sanator_25 = request.POST.get('Sanator_25')
            user = user_info.objects.get(id=session_user_id)
            save_vote = senator_vote_count(user_con=user, person_get_vote_1=Sanator_1, person_get_vote_2=Sanator_2, person_get_vote_3=Sanator_3, person_get_vote_4=Sanator_4, person_get_vote_5=Sanator_5, person_get_vote_6=Sanator_6, person_get_vote_7=Sanator_7, person_get_vote_8=Sanator_8, person_get_vote_9=Sanator_9, person_get_vote_10=Sanator_10, person_get_vote_11=Sanator_11, person_get_vote_12=Sanator_12, person_get_vote_13=Sanator_13, person_get_vote_14=Sanator_14, person_get_vote_15=Sanator_15, person_get_vote_16=Sanator_16, person_get_vote_17=Sanator_17, person_get_vote_18=Sanator_18, person_get_vote_19=Sanator_19, person_get_vote_20=Sanator_20, person_get_vote_21=Sanator_21, person_get_vote_22=Sanator_22, person_get_vote_23=Sanator_23, person_get_vote_24=Sanator_24, person_get_vote_25=Sanator_25 )
            save_vote.save()
            return redirect('go_for_poll')
        else:
            return redirect('go_for_poll')
    return redirect('login_rigister')



@csrf_exempt
def Senator_result(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        k = senator_vote_count.objects.all()
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        ten = 0
        el_11 = 0
        t_12 = 0
        t_13=0
        f_14=0
        f_15=0
        s_16=0
        s_17=0
        e_18=0
        n_19=0
        t_20=0
        t_21 = 0
        t_22 = 0
        t_23 = 0
        t_24 = 0
        t_25 = 0
        for i in k:
            if i.person_get_vote_1 == 'Sanator_1':
                one = one + 1
            if i.person_get_vote_2 == 'Sanator_2':
                two = two + 1
            if i.person_get_vote_3 == 'Sanator_3':
                three = three + 1
            if i.person_get_vote_4 == 'Sanator_4':
                four = four + 1
            if i.person_get_vote_5 == 'Sanator_5':
                five = five + 1
            if i.person_get_vote_6 == 'Sanator_6':
                six = six + 1
            if i.person_get_vote_7 == 'Sanator_7':
                seven = seven + 1
            if i.person_get_vote_8 == 'Sanator_8':
                eight = eight + 1
            if i.person_get_vote_9 == 'Sanator_9':
                nine = nine + 1
            if i.person_get_vote_10 == 'Sanator_10':
                ten = ten + 1
            if i.person_get_vote_11 == 'Sanator_11':
                el_11 = el_11 + 1
            if i.person_get_vote_12 == 'Sanator_12':
                t_12 = t_12 + 1
            if i.person_get_vote_13 == 'Sanator_13':
                t_13 = t_13 + 1
            if i.person_get_vote_14 == 'Sanator_14':
                f_14 = f_14 + 1
            if i.person_get_vote_15 == 'Sanator_15':
                f_15 = f_15 + 1
            if i.person_get_vote_16 == 'Sanator_16':
                s_16 = s_16 + 1
            if i.person_get_vote_17 == 'Sanator_17':
                s_17 = s_17 + 1
            if i.person_get_vote_18 == 'Sanator_18':
                e_18 = e_18 + 1
            if i.person_get_vote_19 == 'Sanator_19':
                n_19 = n_19 + 1
            if i.person_get_vote_20 == 'Sanator_20':
                t_20 = t_20 + 1
            if i.person_get_vote_21 == 'Sanator_21':
                t_21 = t_21 + 1
            if i.person_get_vote_22 == 'Sanator_22':
                t_22 = t_22 + 1
            if i.person_get_vote_23 == 'Sanator_23':
                t_23 = t_23 + 1
            if i.person_get_vote_24 == 'Sanator_24':
                t_24 = t_24 + 1
            if i.person_get_vote_25 == 'Sanator_25':
                t_25 = t_25 + 1
        contex = {
            'one': one,
            'two': two,
            'three': three,
            'four': four,
            'five': five,
            'six': six,
            'seven': seven,
            'eight': eight,
            'nine': nine,
            'ten': ten,
            'el_11': el_11,
            't_12': t_12,
            't_13': t_13,
            'f_14': f_14,
            'f_15': f_15,
            's_16': s_16,
            's_17': s_17,
            'e_18': e_18,
            'n_19': n_19,
            't_20': t_20,
            't_21': t_21,
            't_22': t_22,
            't_23': t_23,
            't_24': t_24,
            't_25': t_25,


        }

        return render(request, 'Senator_result.html', contex)
    return redirect('login_rigister')

