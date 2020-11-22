function getCount(objects) {
    var i;
    var count=0;
    for(i=0;i<objects.length;i++){
        if(objects[i].x==objects[i].y){
            count++;
        }
    }
    return count;
}
