import pycuber as pc

class MyCube(pc.Cube):
    """
    Redefine the __str__ for RE retrival
    """
    def __str__(self):
        result = ""
        colors = {
            "[y]":"U",
            "[g]":"F",
            "[r]":"L",
            "[o]":"R",
            "[w]":"D",
            "[b]":"B",
        }
        for layer in [self.U,self.L,self.F,self.R,self.B,self.D]:
            for i in range(3):
                result += "".join(str(square) for square in layer[i])
        for key, values in colors.items():
            result = result.replace(key, values)
        return result
