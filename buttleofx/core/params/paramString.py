from quickmamba.patterns import Signal


class ParamString(object):
    """
        Core class, which represents a string parameter.
        Contains :
            - _paramType : the name of the type of this parameter
            - _defaultValue : the default value for the input
            - _value : the value contained by the input
            - _stringType : the type of the string (url, path...)
            - _text : the label of the input
    """

    def __init__(self, tuttleParam):
        self._tuttleParam = tuttleParam
        print tuttleParam

        self.changed = Signal()

    #################### getters ####################

    def getTuttleParam(self):
        return self._tuttleParam

    def getParamType(self):
        return "ParamString"

    def getDefaultValue(self):
        return self._tuttleParam.getProperties().fetchProperty("OfxParamPropDefault").getStringValue(0)

    def getValue(self):
        return self._tuttleParam.getStringValue()

    def getStringType(self):
        # OfxParamPropStringFilePathExists
        # OfxParamStringIsSingleLine
        # OfxParamStringIsMultiLine
        # OfxParamStringIsFilePath
        # OfxParamStringIsDirectoryPath
        # OfxParamStringIsLabel
        return self._tuttleParam.getProperties().fetchProperty("OfxParamPropStringMode").getStringValue(0)

    def getText(self):
        return self._tuttleParam.getName()

    #################### setters ####################

    def setValue(self, value):
        self._tuttleParam.setValue(str(value))
        self.changed()
        from buttleofx.data import ButtleDataSingleton
        buttleData = ButtleDataSingleton().get()
        buttleData.updateMapAndViewer()
