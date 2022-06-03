from collections import namedtuple

from kivy.uix.button import Button
from kivy.app import App

class TouchPanel(Button):
    text: str
    current: int = 0
    _max: int = 0

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, current_):
        if self._max < current_:
            self._max = current_

    # Button interface implementation
    def on_touch_down(self, touch):
        '''Fired when a touch event occurs, then update self.touches
        '''
        if self.collide_point(*touch.pos): # check if touch event is within the panel

            self.current += 1
            self.max = self.current
            self.text = f"Current: {self.current}\nMax:{self.max}"

            return False # panel position has been released

 
    def on_touch_up(self, touch):
        '''Fired when a touch event ceases, then update self.touches
        '''
        if self.collide_point(*touch.pos): # check if touch event was within the panel
            self.current -= 1
            self.text = f"Current: {self.current}\nMax:{self.max}"

            return False # panel position has been touched
 
class TouchTester(App):
    def build(self):
        app_panel = TouchPanel(text="Current: 0")

        return app_panel

       
if __name__ == '__main__':
    TouchTester().run()