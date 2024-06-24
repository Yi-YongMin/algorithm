function solution(telno) {
    const tel = telno.replace(/-/g,'');//전화번호
    const failure = ["전국", "X"];//실패시에
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
    if(tel.substring(0,3)==="001"||tel.substring(0,3)==="002"){
        if (tel.length > 15 || tel.length < 11) return ["국제전화" , "X"];
        return ["국제전화" , "O"]
    }
    if (tel.length > 11 || tel.length < 9) return failure; //길이가 9미만 또는 11초과일 경우에는 failure 리턴
    else if (tel[0] !== '0') return failure; //또는 첫숫자가 0이 아니어도 failure 리턴

    const top = tel.substring(0, 3); //top는 처음 세개의 숫자
    const ext = tel.substring(tel.length - 4); //ext는 끝에 네개의 숫자

    if (tel[1] === '2') { // 만약 두번째 숫자가 2일때, 
        if (tel.length !== 10) return ["서울", "X"]; //길이가 10이 아니면 서울 X 리턴
        if (ext[0] === ext[1] && ext[1] === ext[2] && ext[2] === ext[3]) return ["서울", "X"];//끝 네자리 같으면 서울 X 리턴
        return ["서울", "O"];//앞에 두 조건 포함안되면, 서울 O리턴
    }
    else if (tel[1] === '1') {//두번째 숫자가 1일때, 
        if (!map[top]) return failure;//map에 해당 키가 비어있으면 실패
        if (tel[2] !== '0') return ["휴대폰", "X"]; //세번째 숫자가 0이 아니면 휴대폰 X
        if (tel.length === 11 && parseInt(tel[3]) % 2 === 0) return ["휴대폰", "O"];//길이가 11이고 가운데 첫수가 짝수면 휴대폰 O리턴
        return ["휴대폰", "X"];//위에 해당사항 없으면 휴대폰 X리턴
    }
    else if (map[top]) {//만약 지역번호가 map에 존재하면
        if (tel.length === 10 && tel[3] === '0') return [map[top], "X"];//길이가 10이고 가운데 첫수가 0일시에 '해당지역' X 리턴
        return [map[top], "O"];//해당 지역 O리턴
    }

    return failure;
}

console.log(solution("010-123-1234"));// 길이가 10이라 휴대폰 X 리턴
console.log(solution("010-2234-1234"));// 휴대폰 O 리턴
console.log(solution("02-1234-1234"));// 서울 O 리턴
console.log(solution("0212341111"));//서울 X리턴
console.log(solution("0311237890"));// 경기 O 리턴
console.log(solution("061-012-7890"));// 전남 X 리턴
console.log(solution("015-0157899"));// 실패 리턴
console.log(solution("042-2123-7890"));// 대전 O 리턴
console.log(solution("002-2123-7890"));//국제전화 O 리턴
console.log(solution("001-2123-780"));//짧아서 국제전화 X 리턴
console.log(solution("001-212113-7118011"));//길어서 국제전화 X 리턴