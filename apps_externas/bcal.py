from calendar import isleap
import datetime
import itertools
from menu.models import Tarea


def get_bcal(year, month, day):
    request_day = day
    today = datetime.datetime.today()
    current_month = str(today.month)
    current_year = str(today.year)
    month_events = Tarea.objects.filter(fecha_alta__year=year).filter(fecha_alta__month=month)
    weekday_key = datetime.date(int(year), int(month), 1).weekday()
    is_leap = isleap(int(year))
    month_list = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }
    month_name = month_list[int(month)]
    thirties = ('4', '6', '9', '11')
    date_range = dict.fromkeys(range(1, 32), '')
    """ Iterate through the Event month queryset and update dictionary with individual Event objects.
     day_link will be linked to a ListView that filters on the requested day. """
    for event in month_events:
        event_url = event.get_absolute_url()
        client = ''
        if event.estado == 'Abierta':
            client = '<a class="badge badge-pill badge-info" href="%s">%s</a><br />' % (event_url, event.titulo)
        else:
            client = '<a class="badge badge-pill badge-warning" href="%s">%s</a><br />' % (event_url, event.titulo)
        # ESTO ES PARA QUE SOLO EL TUTOR CORRESPONDIENTE VEA SU CORRESPONDIENTES TAREAS Y EL ADMIN TODAS PERO ME DIJO
        # BIANCA QUE DEJE QUE TODOS VEAN TODAS NOMAS...
        #
        # if user.is_staff:
        #     if event.estado == 'Abierta':
        #         client = '<a class="badge badge-pill badge-info" href="%s">%s</a><br />' % (event_url, event.titulo)
        #     else:
        #         client = '<a class="badge badge-pill badge-warning" href="%s">%s</a><br />' % (event_url, event.titulo)
        # else:
        #     if str(event.tutor_asignado.dni) == str(user):
        #         if event.estado == 'Abierta':
        #             client = '<a class="badge badge-pill badge-info" href="%s">%s</a><br />' % (event_url, event.titulo)
        #         else:
        #             client = '<a class="badge badge-pill badge-warning" href="%s">%s</a><br />' % (event_url, event.titulo)
        # HASTA ACA
        #
        # client = '<button class="badge badge-pill badge-info" data-toggle="modal" data-target="#exampleModalCenter">%s</button><br />' \
        #             '<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">' \
        #                 '<div class="modal-dialog modal-dialog-centered" role="document">' \
        #                     '<div class="modal-content">' \
        #                         '<div class="modal-header">' \
        #                             '<h5 class="modal-title" id="exampleModalLongTitle">Tarea: %s</h5>' \
        #                             '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' \
        #                             '<span aria-hidden="true">&times;</span>' \
        #                             '</button>' \
        #                         '</div>' \
        #                         '<div class="modal-body">' \
        #                             '<div class="container">' \
        #                                 '<div class="row">' \
        #                                     '<div class="col">' \
        #                                         '<div class="card-body">' \
        #                                             '<ul class="list-group list-group-flush">' \
        #                                                 '<li class="list-group-item">Tarea: %s</li>' \
        #                                                 '<li class="list-group-item">Descripción: %s</li>' \
        #                                                 '<li class="list-group-item">Fecha programada: %s</li>' \
        #                                                 '<li class="list-group-item">Estado: %s</li>' \
        #                                                 '<li class="list-group-item">Tutor asignado: %s</li>' \
        #                                             '</ul>' \
        #                                         '</div>' \
        #                                     '</div>' \
        #                                 '</div>' \
        #                             '</div>' \
        #                         '</div>' \
        #                         '<div class="modal-footer">' \
        #                             '<button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>' \
        #                             '<button type="button" class="btn btn-primary">Editar tarea</button>' \
        #                         '</div>' \
        #                     '</div>' \
        #                 '</div>' \
        #             '</div>' \
        #          % (event.titulo, event.titulo, event.titulo, event.descripcion, event.fecha_alta.date(), event.estado, event.tutor_asignado)
        day = event.fecha_alta.day
        for key, value in date_range.items():
            if key == day:
                date_range[day] += client
    row_today = "<div id=\"cal-today\" class=\"col cal-day\"><a href=\"/agenda/%s/%s/%s\">%s</a><br />%s</div>"
    row_request_day = "<div id=\"cal-req-day\" class=\"col cal-day\">%s<br />%s</div>"
    row_day = "<div class=\"col cal-day\"><a href=\"/agenda/%s/%s/%s\">%s</a><br />%s</div>"
    empty_day = "<div class =\"col cal-day\">&nbsp;</div>"
    sixth_row = False

    if weekday_key is 0:  # 1st falls on Monday -> example August 2016
        row1 = ""
        before = empty_day
        for key, value in itertools.islice(date_range.items(), 0, 6):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 6, 13):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 13, 20):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 20, 27):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 27, 28
            remainder = empty_day * 6
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 27, 29
            remainder = empty_day * 5
        elif month in thirties:  # 30 days
            start, end = 27, 30
            remainder = empty_day * 4
        else:  # 31 days
            start, end = 27, 31
            remainder = empty_day * 3
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 1:  # 1st falls on Tuesday -> example November 2016
        row1 = ""
        before = empty_day * 2
        for key, value in itertools.islice(date_range.items(), 0, 5):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 5, 12):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 12, 19):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 19, 26):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 26, 28
            remainder = empty_day * 5
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 26, 29
            remainder = empty_day * 4
        elif month in thirties:  # 30 days
            start, end = 26, 30
            remainder = empty_day * 3
        else:  # 31 days
            start, end = 26, 31
            remainder = empty_day * 2
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 2:  # 1st falls on Wednesday -> example February 2017

        row1 = ""
        before = empty_day * 3
        for key, value in itertools.islice(date_range.items(), 0, 4):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 4, 11):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 11, 18):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 18, 25):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 25, 28
            remainder = empty_day * 4
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 25, 29
            remainder = empty_day * 3
        elif month in thirties:  # 30 days
            start, end = 25, 30
            remainder = empty_day * 2
        else:  # 31 days
            start, end = 25, 31
            remainder = empty_day * 1
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 3:  # 1st falls on Thursday -> example Dec 2016
        row1 = ""
        before = empty_day * 4
        for key, value in itertools.islice(date_range.items(), 0, 3):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 3, 10):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 10, 17):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 17, 24):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 24, 28
            remainder = empty_day * 3
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 24, 29
            remainder = empty_day * 2
        elif month in thirties:  # 30 days
            start, end = 24, 30
            remainder = empty_day * 1
        else:  # 31 days
            start, end = 24, 31
            remainder = ""
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)

    elif weekday_key is 4:  # 1st falls on Friday -> example July 2016
        row1 = ""
        before = empty_day * 5
        for key, value in itertools.islice(date_range.items(), 0, 2):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 2, 9):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 9, 16):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 16, 23):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 23, 28
            remainder = empty_day * 2
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 23, 29
            remainder = empty_day * 1
        elif month in thirties:  # 30 days
            start, end = 23, 30
            remainder = ""
        else:  # 31 days
            start, end = 23, 30
            remainder = ""
            sixth_row = True
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
        if sixth_row:
            row6 = ""
            remainder = empty_day * 6
            for key, value in itertools.islice(date_range.items(), 30, 31):
                if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (
                        int(key) == int(today.day)):
                    row6 += row_today % (year, month, key, key, str(value))
                elif str(key) == str(request_day):
                    row6 += row_request_day % (
                        str(key), str(value))
                else:
                    row6 += row_day % (year, month, key, key, str(value))
            row6 = "%s%s" % (row6, remainder)

    elif weekday_key is 5:  # 1st falls on Saturday -> e.g. April 2017
        row1 = ""
        before = empty_day * 6
        for key, value in itertools.islice(date_range.items(), 0, 1):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row1 = "%s%s" % (before, row1)
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 1, 8):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 8, 15):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 15, 22):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 22, 28
            remainder = empty_day * 1
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 22, 29
            remainder = ""
        elif month in thirties:  # 30 days
            start, end = 22, 29
            remainder = ""
            sixth_row = True
            row6start, row6end = 29, 30
            row6remainder = empty_day * 6
        else:  # 31 days
            start, end = 22, 29
            remainder = ""
            sixth_row = True
            row6start, row6end = 29, 31
            row6remainder = empty_day * 5
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
        if sixth_row:
            row6 = ""
            for key, value in itertools.islice(date_range.items(), row6start,
                                               row6end):
                if year == current_year and month == current_month and key == today.day:
                    row6 += row_today % (year, month, key, key, str(value))
                elif str(key) == str(request_day):
                    row6 += row_request_day % (
                        str(key), str(value))
                else:
                    row6 += row_day % (year, month, key, key, str(value))
            row6 = "%s%s" % (row6, row6remainder)

    elif weekday_key is 6:  # 1st Falls on Sunday --> October 2017
        row1 = ""
        for key, value in itertools.islice(date_range.items(), 0, 7):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row1 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row1 += row_request_day % (str(key), str(value))
            else:
                row1 += row_day % (year, month, key, key, str(value))
        row2 = ""
        for key, value in itertools.islice(date_range.items(), 7, 14):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row2 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row2 += row_request_day % (str(key), str(value))
            else:
                row2 += row_day % (year, month, key, key, str(value))
        row3 = ""
        for key, value in itertools.islice(date_range.items(), 14, 21):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row3 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row3 += row_request_day % (str(key), str(value))
            else:
                row3 += row_day % (year, month, key, key, str(value))
        row4 = ""
        for key, value in itertools.islice(date_range.items(), 21, 28):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row4 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row4 += row_request_day % (str(key), str(value))
            else:
                row4 += row_day % (year, month, key, key, str(value))
        row5 = ""
        if month is '2' and is_leap is False:  # 28 days
            start, end = 28, 28
            remainder = ""
        elif month is '2' and is_leap is True:  # 29 days
            start, end = 28, 29
            remainder = empty_day * 6
        elif month in thirties:  # 30 days
            start, end = 28, 30
            remainder = empty_day * 5
        else:  # 31 days
            start, end = 28, 31
            remainder = empty_day * 4
        for key, value in itertools.islice(date_range.items(), start, end):
            if (int(year) == int(current_year)) and (int(month) == int(current_month)) and (int(key) == int(today.day)):
                row5 += row_today % (year, month, key, key, str(value))
            elif str(key) == str(request_day):
                row5 += row_request_day % (str(key), str(value))
            else:
                row5 += row_day % (year, month, key, key, str(value))
        row5 = "%s%s" % (row5, remainder)
    # Create Next Month and Previous Month Links
    nav = '<a class="btn btn-default" href="/agenda/%s/%s/1">%s</a>'
    right_chevron = '<i class="push-right fa fa-chevron-right" aria-hidden="true"></i>'
    left_chevron = '<i class="push-right fa fa-chevron-left" aria-hidden="true"></i>'
    if int(month) == 12:
        next_year = int(year) + 1
        next_month = 1
        ch1 = right_chevron
        next_month_link = nav % (next_year, next_month, ch1)
    else:
        next_month = int(month) + 1
        ch1 = right_chevron
        next_month_link = nav % (year, next_month, ch1)

    if int(month) == 1:
        prev_year = int(year) - 1
        prev_month = 12
        ch2 = left_chevron
        prev_month_link = nav % (prev_year, prev_month, ch2)
    else:
        prev_month = int(month) - 1
        ch2 = left_chevron
        prev_month_link = nav % (year, prev_month, ch2)

    links = "<div class='row'>" \
            "<div class='col-auto mr-auto'>" \
            "<h3>%s %s, %s</h3>" \
            "</div>" \
            "<div class='col-auto'>" \
            "<h3>%s %s</h3>" \
            "</div>" \
            "</div>" % (
        month_name, request_day, year, prev_month_link, next_month_link
    )
    sun = "<div class=\"col cal-header\">Domingo</div>\n"
    mon = "<div class=\"col cal-header\">Lunes</div>\n"
    tue = "<div class=\"col cal-header\">Martes</div>\n"
    wed = "<div class=\"col cal-header\">Miercoles</div>\n"
    thu = "<div class=\"col cal-header\">Jueves</div>\n"
    fri = "<div class=\"col cal-header\">Viernes</div>\n"
    sat = "<div class=\"col cal-header\">Sabado</div>\n"
    header = "<div class=\"row\">%s%s%s%s%s%s%s</div>\n" % (
        sun, mon, tue, wed, thu, fri, sat
    )
    one = "<div class=\"row\">%s</div>\n" % row1
    two = "<div class=\"row\">%s</div>\n" % row2
    three = "<div class=\"row\">%s</div>\n" % row3
    four = "<div class=\"row\">%s</div>\n" % row4
    five = "<div class=\"row\">%s</div>\n" % row5
    if sixth_row:
        six = "<div class=\"row\">%s</div>\n" % row6
        return "%s%s%s%s%s%s%s%s" % (
        links, header, one, two, three, four, five, six
        )
    else:
        return "%s%s%s%s%s%s%s" % (links, header, one, two, three, four, five)