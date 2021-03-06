# -*- coding: utf-8 -*-
# Copyright (C) 1998-2018 by the Free Software Foundation, Inc.
#
# This file is part of Postorius.
#
# Postorius is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Postorius is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Postorius.  If not, see <http://www.gnu.org/licenses/>.


from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.defaults import page_not_found, server_error

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('list_index'),
        permanent=True)),
    url(r'^postorius/', include('postorius.urls')),
    url(r'', include('django_mailman3.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # Add some testing routes to test 400/500 error pages without having to
    # introduce errors.
    url(r'500/$', server_error),
    url(r'400/$', page_not_found),
    # Django admin
    url(r'^admin/', admin.site.urls),
]
