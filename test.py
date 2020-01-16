import pycuber as pc

class MyCube(pc.Cube):
    """
    Redefine the __str__ for RE retrival
    """
    def __str__(self):
        result = pc.Cube.__str__(self)
        colors = {
            "[y]":"U",
            "[g]":"F",
            "[r]":"L",
            "[o]":"R",
            "[w]":"D",
            "[b]":"B",
        }
        for key, values in colors.items():
            result = result.replace(key, values)
        return result.replace(' ', '').replace('\n', '').strip()

if __name__ == "__main__":
    mycube = MyCube()
    mycube("R U R' U'")

    print(mycube)