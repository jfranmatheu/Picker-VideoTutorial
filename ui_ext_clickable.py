

class Clickable:
    def _on_event(self, event: 'Event', mouse: 'Vector'):
        if not self._on_hover(mouse):
            return
        
        if event.type == 'LEFTMOUSE':
            if event.value == 'PRESS':
                self.on_leftmouse_press(event, mouse)
            elif event.value == 'RELEASE':
                self.on_leftmouse_release(event, mouse)
            return True
        return self.on_event(event, mouse)

    def on_leftmouse_press(self, event: 'Event', mouse: 'Vector'):
        pass

    def on_leftmouse_release(self, event: 'Event', mouse: 'Vector'):
        pass
