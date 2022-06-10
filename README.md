# 프로젝트 제목: 동국대생을 위한 정보전달 웹사이트 '융알이'

# 프로젝트 내용:
### 프로젝트 개요
![그림 1](https://user-images.githubusercontent.com/101690336/173097715-4a85d96a-c3ea-4734-a859-136ec1f681de.png)  
융알이는 다음과 같이 작동합니다.  
1. 파이썬으로 작성된 크롤링 파일이 깃허브 액션스를 통해 자동으로 실행됩니다. 실행파일은 대상으로 하는 사이트의 지정된 정보를 모두 가져와 json 으로 저장 및 자동으로 덮어쓰기 하여 충돌이 일어나지 않도록 제작했습니다.  
2. 저장된 json 파일은 EC2 내 Node.js 서버를 통해 배포됩니다. 사이트 내에서 유저가 분류를 선택하지 않은 경우 모든 데이터를 출력하며 분류가 선택되면 자바스크립트에서 해당 분류에 따라 json 데이터를 가공하고 출력해줍니다.
3. 구글 캘린더 기능을 이용해 일정을 관리할 수 있습니다.

# 실행환경
### 배포방법: AWS EC2를 통해 배포
### 웹서버: nodejs

# 설치 방법
 * 작업환경
   * 파이썬 3.9.2
   * Node.js 서버
   * EC2

* 파이썬 설치
```c
$ sudo apt-get update
$ sudo apte install python3
$ sudo apt install python3-pip
```
* 파이썬 버전 확인
```c
$ python --version
$ pip -- version
```
* Beautifulsoup4 설치
```c
$ sudo apt-get update
$ pip install beautifulsoup4 
```
* pandas 설치
```c
$ sudo apt-get update
$ pip install pandas 
```
# 팀원 정보(연락처, 역할)
## [고상현] (https://github.com/hyun7520) 
연락처: sanghyun123452@gmail.com  
역할: 크롤링 코드 작성, 데이터 정리 및 분류

## [권석현] (https://github.com/sukhyun205)
연락처: sukhyun205@gmail.com  
역할: 서버 구축, 메뉴, 체크박스 구현, ui 개선- 화면 크기 조절에 따른 동적 변화

## [김동근] (https://github.com/kimdonggeun111)
연락처: kdgk9620@gmail.com  
역할: 크롤링 자동화, 캘린더, 분류기능, UI개선- 마우스 오버 및 클릭 이벤트 추가

## 코드 예제

아이프레임 내부에 값 전달
```c
check = "";
    if (parent.check != ""){
        check = parent.check;// 프레임 외부 값(버튼 선택 시 선택되는 태그)을 받음 // parent. 으로 외부 변수를 받아 올 수 있음
        checkList = check.split(","); // 체크를 구분자,를 기준으로 분해해서 checkList에 삽입
        lenCheckList = checkList.length; // 리스트의 길이를 저장
    }
```  

체크박스
```c

  var check = ""; // 체크 초기 값
  // 확인 버튼 클릭 시 발생하는 이벤트 
  function gettag(){ 
   check = ""; // 체크 초기화
    var storage = document.getElementsByName("tag"); // 태그 값이라는 이름을 가진 구성요소에 접근해서 태그가 붙어있는 문서의 내용만 storage에 저장
    for (i =0;i < storage.length;i++){ // storage수만큼 루프
      if(storage[i].checked == true){ // 만약 체크되어 있으면
        check += storage[i].value; // 아이프레임에 전달할 변수의 값(check)을 체크박스의 값으로 문자열에 추가
        check += "," // 구분자 추가
        //check = storage[i].value; // 아이프레임에 전달할 변수의 값(check)
      }
    }
    document.getElementById("if1").src += ''; //아이프레임 창 새로고침
    document.getElementById("if2").src += '';
    document.getElementById("if3").src += '';
    document.getElementById("if4").src += '';
    document.getElementById("if5").src += '';
    //location.reload(); // 웹페이지 갱신
    /*let passData = check;
    let iframe = document.getElementById('iframe2').contentWindow;
    iframe.postMessage(passData, 'http://127.0.0.1:5502/public/temp/activity.html');*/
  }

```  

ㅇㅇ
```c

```  

ㅇㅇ
```c

```  
## 실제 적용 사례
= json 파일하고 웹페이지 실행 화면
