import android
from android.widget import Button, LinearLayout, RelativeLayout, TextView, EditText
from com.android.volley import toolbox
from com.android.volley.toolbox import Volley

class OnClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)

class OnResponse(implements=com.android.volley.Response[Listener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onResponse(self, response: java.lang.Object) -> void:
        self.callback(*self.args, **self.kwargs, response=response)

class OnError(implements=com.android.volley.Response[ErrorListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onErrorResponse(self, error: com.android.volley.VolleyError) -> void:
        self.callback(*self.args, **self.kwargs, error=error)

class MainApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)
        self.queue = Volley.newRequestQueue(self._activity)

    def onCreate(self):
        self.vlayout = LinearLayout(self._activity)
        self.vlayout.setOrientation(LinearLayout.VERTICAL)

        self.entrytext = EditText(self._activity)
        self.entrytext.setHint('Write a url to request')
        self.vlayout.addView(self.entrytext)

        button_send = Button(self._activity)
        button_send.setText('Request GET')
        button_send.setOnClickListener(OnClick(self.send_request))
        self.vlayout.addView(button_send)

        self.result = TextView(self._activity)
        self.result.setText('Waiting a request')
        self.vlayout.addView(self.result)

        self._activity.setContentView(self.vlayout)

    def listener(self, response):
        response = str(response)
        self.result.setText("Response is: " + response[0:200])

    def listener_error(self, error):
        self.result.setText('Request failed, error: ' + error.getMessage())

    def send_request(self):
        self.result.setText('Loading request')
        url = str(self.entrytext.getText())
        stringRequest = toolbox.StringRequest(
            url,
            OnResponse(self.listener),
            OnError(self.listener_error)
            )
        self.queue.add(stringRequest)

def main():
    MainApp()
