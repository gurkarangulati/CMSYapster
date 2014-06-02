from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from admins.models import Profile, CmsUser
from admins.decorators import user_has_perm, active_and_login_required
from admins.signals import *
import logging

logger = logging.getLogger(__name__)


def login_user(request):
    """
    Display login page. Redirect to homepage if success

    TODO: Add yapster profile in session?
    """
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        current_user = authenticate(username=username, password=password)
        current_cms_user = CmsUser.objects.get(pk=current_user)
        if current_cms_user is not None:
            if current_cms_user.is_active:
                login(request, current_user)
                #request.session['account'] = CmsUser.objects.get(user=current_user)
                return HttpResponseRedirect('/home/')
    return render(request, 'admins/login.html', {})


@active_and_login_required
@user_has_perm
def users_manage(request):
    """
    List of users. Create and view users
    """
    users = CmsUser.objects.filter(is_active=True)
    inactive_users = CmsUser.objects.filter(is_active=False)
    groups = GroupPermission.objects.all()

    if 'btn_delete' in request.POST:
        username = request.POST['username']
        user = CmsUser.objects.get(username=username)
        user.is_active = False
        user.save()
        return HttpResponseRedirect('/cmsusers/')

    if 'btn_active' in request.POST:
        username = request.POST['username']
        user = CmsUser.objects.get(username=username)
        user.is_active = True
        user.save()
        return HttpResponseRedirect('/cmsusers/')

    if 'btn_new' in request.POST:
        if request.POST['password'] == request.POST['password2'] \
                and request.POST['email'] == request.POST['email2']:
            username = request.POST['username']
            first = request.POST['firstname']
            last = request.POST['lastname']
            password = request.POST['password']
            email = request.POST['email']
            dep = request.POST['department']
            occ = request.POST['occupation']
            id_group = request.POST['group']
            group = GroupPermission.objects.get(pk=id_group)
            CmsUser.new_user(username=username, first_name=first, last_name=last,
                             email=email, password=password, department=dep,
                             occupation=occ, group=group)
            return HttpResponseRedirect('/cmsusers/')
    return render(request, 'admins/users_manage.html',
                  {'users': users, 'inactive_users': inactive_users,
                   'groups':groups})

@active_and_login_required
@user_has_perm
def cmsuser(request, username):
    """
    Display CMS user info + change permissions/name/username
    """
    cmsuser = CmsUser.objects.get(username=username)
    own = cmsuser.username == username
    return render(request, 'admins/cmsuser.html',
                  {"cmsuser": cmsuser, "own": own})


@active_and_login_required
@user_has_perm
def edit_cmsuser(request, username):
    """
    Edit Cms User infos
    """

    cmsuser = CmsUser.objects.get(username=username)
    d_args = {}
    if 'btn_newinfos' in request.POST:
        if request.POST['firstname']:
            d_args['first_name'] = request.POST['firstname']
        if request.POST['lastname']:
            d_args['last_name'] = request.POST['lastname']
        if request.POST['username']:
            d_args['username'] = request.POST['username']
        if request.POST['email'] and \
                request.POST['email2'] and \
                (request.POST['email'] == request.POST['email2']):
            d_args['email'] = request.POST['email']
        if request.POST['password'] and \
                request.POST['password2'] and \
                (request.POST['password'] == request.POST['password2']):
            d_args['password'] = request.POST['password']
        cmsuser.update(**d_args)
        return HttpResponseRedirect('')
    return render(request, 'admins/edit_cmsuser.html', {"cmsuser": cmsuser})


@active_and_login_required
def profile(request, username):
    """
    Display Yapster user profile. With info/stats
    """
    prof = Profile.objects.get(user__username=username)

    return render(request, 'admins/profile.html', {'profile': prof})