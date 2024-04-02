from django import template

register = template.Library()

@register.filter(name='video_no_prev')
def video_no_prev(serial_no):
    
    if int(serial_no) == 1:
        return  1
    else:
        return int(serial_no)-1
    

@register.filter(name='video_no_next')
def video_no_next(serial_no):
    
    if (serial_no)-1 !=int(serial_no):
        return  int(serial_no)+1
    else:
        return int(serial_no)



