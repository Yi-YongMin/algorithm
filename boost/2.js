function play(param0){
    var par=param0;
    var cnt=0;
    var arr=Array(16).fill(0);
    var ans=Array(4).fill(0);
    var pos=Array(4).fill(0);
    arr[0]=1;
    while(cnt!==15 && par.length){//맵이 아직 다 안찼고, 배열도 남아있으면,
        const p = par.shift();//배열 앞단을 떼어와서
        for(var i=0;i<4;i++){//A,B,C,D 다 확인
            pos[i]+=p[i];//일단 이동하는데
            if(pos[i]>15){
                pos[i]-=16;
            }
            if (arr[pos[i]]!==1){//만약 이동할 곳이 아직 안선점되었으면
                arr[pos[i]]=1;//선점하고
                cnt+=1;//맵 하나 채우고
                ans[i]+=1;//해당 선수의 건물 수 +1
            }
        }
    }
    let result = {
        "A": ans[0],
        "B": ans[1],
        "C": ans[2],
        "D": ans[3]
    };
    return result;
}


function generateRandomArray(rows, cols, min, max) {
    let array = [];
    for (let i = 0; i < rows; i++) {
        let row = [];
        for (let j = 0; j < cols; j++) {
            row.push(Math.floor(Math.random() * (max - min + 1)) + min);
        }
        array.push(row);
    }
    return array;
}

const param0 = generateRandomArray(10, 4, 1, 4);
console.log(param0);
console.log(play(param0));