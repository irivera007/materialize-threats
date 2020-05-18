from .GraphObj import GraphObj


class UserObject(GraphObj):
    def __init__(self, sid, gid, **kwargs):
        super(UserObject, self).__init__(sid, gid)
        data = **kwargs

    def text_to_mx_value(self):
        value = ""
        last_text = len(self.texts) - 1
        for i, t in enumerate(self.texts):
            style = t.get_mx_style()
            value += "<p style='" + style + "'>" + t.text + "</p>"
            if i != last_text:
                value += "<hr size='1'/>"
        return value