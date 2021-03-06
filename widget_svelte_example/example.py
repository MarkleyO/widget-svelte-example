#!/usr/bin/env python
# coding: utf-8

from ipywidgets import DOMWidget
from traitlets import Integer, Unicode, List
from ._frontend import module_name, module_version


class ExampleWidget(DOMWidget):
    """Example widget with a counter and increment button."""
    _model_name = Unicode('ExampleModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('ExampleView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)


    value = Integer(0).tag(sync=True)
    unit = Unicode('clicks').tag(sync=True)
    numberList = List([]).tag(sync=True)
