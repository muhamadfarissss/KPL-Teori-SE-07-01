class ShapeFactory:
    @staticmethod
    def getshape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")
        
ShapeFactory.getshape("circle")