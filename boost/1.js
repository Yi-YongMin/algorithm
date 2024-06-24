function solution(telno) {
    const tel = telno;
    const failure = ["전국", "X"];
    const map = {
        "010": "휴대폰",
        "011": "휴대폰", "016": "휴대폰", "017": "휴대폰", "018": "휴대폰", "019": "휴대폰",
        "031": "경기", "032": "인천", "033": "강원",
        "041": "충청", "042": "대전", "044": "세종",
        "051": "부산", "052": "울산", "053": "대구",
        "054": "경북", "055": "경남",
        "061": "전남", "062": "광주", "063": "전북",
        "064": "제주"
    };

    if (tel.length > 11 || tel.length < 9) return failure; //길이가 9미만 또는 11초과일 경우에는 failure 리턴
    else if (tel[0] !== '0') return failure; //또는 첫숫자가 0이 아니어도 failure 리턴

    const top = tel.substring(0, 3); //top는 처음 세개의 숫자
    const ext = tel.substring(tel.length - 4); //ext는 첫 네개의 숫자를 제외한 숫자

    if (tel[1] === '2') { // 만약 두번째 숫자가 2일때, 
        if (tel.length !== 10) return ["서울", "X"]; //길이가 10이 아니면 서울 X 리턴
        if (ext[0] === ext[1] && ext[1] === ext[2] && ext[2] === ext[3]) return ["서울", "X"];
        return ["서울", "O"];
    }
    else if (tel[1] === '1') {
        if (!map[top]) return failure;
        if (tel[2] !== '0') return ["휴대폰", "X"];
        if (tel.length === 11 && parseInt(tel[3]) % 2 === 0) return ["휴대폰", "O"];
        return ["휴대폰", "X"];
    }
    else if (map[top]) {
        if (tel.length === 10 && tel[3] === '0') return [map[top], "X"];
        return [map[top], "O"];
    }

    return failure;
}

console.log(solution("010-123-1234"));
console.log(solution("010-2234-1234"));
console.log(solution("02-1234-1234"));
console.log(solution("0212341111"));
console.log(solution("0311237890"));
console.log(solution("061-012-7890"));
console.log(solution("015-0157899"));
console.log(solution("042-2123-7890"));
