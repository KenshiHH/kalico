from kalico import Kalico, gcode_macro, event_handler


@gcode_macro
def assert_event_handler_ran(k: Kalico):
    assert assert_event_handler_ran.vars["ready"]


@event_handler("klippy:ready")
def on_ready(k: Kalico):
    assert_event_handler_ran.vars["ready"] = True
