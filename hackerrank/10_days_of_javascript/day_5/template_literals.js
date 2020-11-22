function sides(literals, ...expressions) {
    let area = expressions[0];
    let perimeter = expressions[1];

    let d = Math.sqrt(perimeter * perimeter - 16 * area);

    let s1 = (perimeter + d) / 4;
    let s2 = area / s1;

    return [s1, s2].sort();
}
