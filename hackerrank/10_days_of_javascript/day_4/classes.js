class Polygon {
    constructor(sides) {
        this.sides = sides;
    }
    perimeter() {
        var sum = 0;
        for(var i=0;i< this.sides.length; i++){
            sum = sum + this.sides[i];
        }
        return sum;
    }
}
