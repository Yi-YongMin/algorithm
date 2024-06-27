const games=[
    {"name":"Kong",
        "genre":"Adventure",
        "star":4.1,
        "ptcp":1,
        "start":197001,
        "end":198104
    },
    {"name":"Ace",
        "genre":"Board",
        "star":3.8,
        "ptcp":4,
        "start":198707,
        "end":202407
    },
    {"name":"Mario",
        "genre":"RPG",
        "star":3.3,
        "ptcp":2,
        "start":200109,
        "end":200711        
    },
    {"name":"Prince",
        "genre":"RPG",
        "star":4.8,
        "ptcp":1,
        "start":198303,
        "end":200205        
    },
    {"name":"Dragons",
        "genre":"Fight",
        "star":3.4,
        "ptcp":4,
        "start":199005,
        "end":199512        
    },
    {"name":"Civil",
        "genre":"Simulation",
        "star":4.2,
        "ptcp":1,
        "start":200206,
        "end":202407    
    },
    {"name":"Teken",
        "genre":"Fight",
        "star":4.0,
        "ptcp":2,
        "start":199807,
        "end":200912       
    },
    {"name":"GoCart",
        "genre":"Sports",
        "star":4.6,
        "ptcp":8,
        "start":200612,
        "end":202407      
    },
    {"name":"Football",
        "genre":"Sports",
        "star":2.9,
        "ptcp":8,
        "start":199406,
        "end":202407       
    },
    {"name":"Brave",
        "genre":"RPG",
        "star":4.2,
        "ptcp":1,
        "start":198006,
        "end":198501       
    },
]
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
// readline 모듈 불러오기
const readline = require('readline');

// readline 인터페이스 생성
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// 질문 던지기
rl.question('형식은 "200001",8 과 같이 날짜와 인원수 : ', (answer) => {
  // 답변 출력
  const param0=answer.substring(1,7);
  const param1=answer[10];

  console.log(`${find(param0,param1)}`);
  
  // 인터페이스 닫기
  rl.close();
});