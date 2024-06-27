# 실수축제

## 자바스크립트의 터미널 입출력

js를 터미널에서 입출력하기 위해서는 node 3.js 라는 명령어를 터미널에 작성해야 한다는 사실을 알았다.  
게다가 입출력을 받기 위한 코드도 엄청 길다.

    const readline = require('readline');

    // readline 인터페이스 생성
    const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
    });

    // 질문 던지기
    rl.question('이름이 무엇인가요? ', (answer) => {
    // 답변 출력
    console.log(`안녕하세요, ${answer}!`);

    // 인터페이스 닫기
    rl.close();
    });

위의 코드를 이용해서 일단 입력이 항상 "200001", 1 이라는 형식으로 들어온다고 가정하고 문제를 풀었다.  
아래와 같이 형식을 바꿔줬다.

    rl.question('형식은 "200001",8 과 같이 날짜와 인원수 : ', (answer) => {
    // 답변 출력
    const param0=answer.substring(1,7);
    const param1=answer[10];

    console.log(`${find(param0,param1)}`);

    // 인터페이스 닫기
    rl.close();

이렇게 바꾼 뒤에 find함수를 작성하였다.  
find함수는 문자열을 리턴한다고 했으므로, ans라는 문자열에 덕지덕지 붙이는 방법을 채택했다.

    function find(param0,param1){
        var index=[];
        param0=parseInt(param0);
        param1=parseInt(param1);
        for(var i=0;i<10;i++){
            if(games[i].start<=param0  && games[i].end>=param0 && games[i].ptcp>=param1) index.push(games[i]);
        }
        index.sort((a,b)=>b.star-a.star);
        var ans="";
        for(var i=0;i<index.length;i++){
            ans+=index[i].name;
            if(index[i].end!==202407){
                ans+="*"
            }
            ans+="("+index[i].genre+") ";
            ans+=index[i].star;
            if(i!==index.length-1){
                ans+=", ";
            }
        }
        return ans;
    }

위와 같이 작성하고 실행했더니, 결국 잘 작동했다.
