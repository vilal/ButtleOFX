from quickmamba.patterns import Signal


class ParamInt(object):
    """
        Core class, which represents an int parameter.
        Contains : 
            - _tuttleParam : link to the corresponding tuttleParam
            - _paramType : the name of the type of this parameter
            - _defaultValue : the default value for the input
            - _value : the value contained by the input
            - _minimum : the min we can have for the value
            - _maximum : the max we can have for the value
            - _text : the label of the input
    """

    def __init__(self, tuttleParam):
        self._tuttleParam = tuttleParam

        self.changed = Signal()

    #################### getters ####################

    def getTuttleParam(self):
        return self._tuttleParam

    def getParamType(self):
        return "ParamInt"

    def getDefaultValue(self):
        return self._tuttleParam.getIntValue()

    def getValue(self):
        return self._tuttleParam.getIntValue()

    def getMinimum(self):
        return self._tuttleParam.getProperties().fetchProperty("OfxParamPropDisplayMin").getStringValue(0) # != OfxParamPropMin

    def getMaximum(self):
        return self._tuttleParam.getProperties().fetchProperty("OfxParamPropDisplayMax").getStringValue(0) # != OfxParamPropMax

    def getText(self):
        return self._tuttleParam.getName()

    #################### setters ####################

    def setValue(self, value):
        self._tuttleParam.setValue(int(value))
        self.changed()

        print "TuttleParam new Value : ", self.getValue()