Project ``StairX``
=======================
2018 POSTECH Hackathon

Members
-----------

- [Dajin Lee](https://github.com/leerubi)
  - Swift for recording and sending iPhone data
  - Python for data processing and finding stairs location
  - Javascript for search view and finding pathes using Kakao Map and T Map API

- [Namwon Kim](https://github.com/NowWhy)
  - Javascript for search view and finding pathes using Kakao Map and T Map API
  - HTML & CSS for visualizing data and design the served map


Progress Report
-------------

### Milestone 1 : Get iPhone sensor data!

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|    2 units     | 2 units   | I_S01 | 실시간 GPS 데이터 기록     |
|    2 units   | 5 units  | I_S02 | FlightsClimbed 데이터 추출 or 실시간 기록  |
|    1 units    | 3 units  | I_S03 | 실시간 Relative Altitude 기록  |
|    1 units    | 3 units  | I_S04 | 실시간 Pressure 기록  |
|    2 units    | 10 units  | I_S05 | 모든 데이터들을 관리하는 애플리케이션 구현(기록시작 버튼, 데이터 추출 버튼 등)  |

- Email 전송방법 대신 서버에 전송하고 싶으나 아직 서버가 없음


### Milestone 2 : Find the stairs location!

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|    4 units    | 1 units   | P_S01 | 받은 4개 데이터 통합     |
|    1 units   | 2 units  | P_S02 | Flights Climbed 데이터의 변화 순간에 해당하는 통합 데이터 따로 저장  |
|    Pass    | 7 units  | P_S03 | 통합 데이터 중 GPS 위치들을 기반으로 계단 위치 지정(면적화) |
|    Pass     | 4 units  | P_S04 | P_S01~03에 대한 여러 sample 들을 중복시켜 특정 임계값을 넘는 면적 계산 |
|    4 units    | 4 units  | P_S05 | 무게중심 GPS 위치 계산 및 추가 정보 입력(계단 크기, 경사) |

- raw_data 기반으로 계단 위치 추정 결과
  - 위치 인식 훌륭
  - 계단 인식 훌륭
  - 계단 인식 시작 시간 훌륭
  - ``계단 인식 끝 시간을 정하는 기준을 모르겠음``
  
- 계단 위치 정확도를 높이기 위한 방법
  - isStair 정확도
    - ``임계값을 주었더니 정확해짐!``
    - 데이터가 많을 수록 임계값 대신 voting법 등으로 계단 위치 추정도 가능해질 듯
  - GPS 정확도 -> 이미 높음
  - 내려가는 계단도 인식하기 -> Health App 내부 알고리즘 모르는 채로 힘듦
  - 낮으 계단이나 턱도 인식하기 -> 거의 불가능
  

### Milestone 3 : Convert technologies to a nice service!

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|    3 units     |    3 units     |    M_S01   |     Web 지도 상에 추정한 계단 위치 띄우기      |
|    Fail    |     8 units      |   M_S02    |       계단을 피하는 경로 계산      |
|    5 units     |      5 units     |   M_S03    |       경로 찾기 (+ 계단 위치 동시에 띄우기)    |
|    2 units     |      2 units     |   M_S04    |       UI 디자인    |

- M_S01: Kakao Map의 경우 쉬웠으나, T Map의 경우 오래 걸림
- M_S02의 문제점과 해결책
  - 직접 경로 찾기 알고리즘을 구현하는 것이 아닌, API를 활용하기로 하였음
    - 직접 경로를 찾을 경우 이를 서비스화된 지도 위에 구현하는 것이 어려울 것으로 예상하였기 때문
  - API에서 경유지 설정은 가능하였지만, 회피 장소 설정이나 제약식 추가 기능은 없었음
    - 경유지를 기점으로 우회하는 알고리즘 이용 -> 경로가 비효율적, 구현이 어려움
    - 기존 경로와 계단 위치를 겹쳐서 보여주기로 함
      - 사용자가 자신의 경로에 계단이 어디에 있는지 확인 가능!
