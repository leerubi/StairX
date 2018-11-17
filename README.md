Project ``StairX``
=======================
2018 POSTECH Hackathon

Members
-----------

- [Dajin Lee](https://github.com/leerubi)
  - Swift for iOS
  - Python for data processing and visualization

- [Namwon Kim](https://github.com/NowWhy)
  - Python for data processing and visualization


Progress Report
-------------

### Milestone 1

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|    2 units     | 2 units   | I_S01 | 실시간 GPS 데이터 기록     |
|    2 units   | 5 units  | I_S02 | FlightsClimbed 데이터 추출 or 실시간 기록  |
|    1 units    | 3 units  | I_S03 | 실시간 Relative Altitude 기록  |
|    1 units    | 3 units  | I_S04 | 실시간 Pressure 기록  |
|    2 units    | 10 units  | I_S05 | 모든 데이터들을 관리하는 애플리케이션 구현(기록시작 버튼, 데이터 추출 버튼 등)  |


### Milestone 2

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|    4 units    | 1 units   | P_S01 | 받은 4개 데이터 통합     |
|    1 units   | 2 units  | P_S02 | Flights Climbed 데이터의 변화 순간에 해당하는 통합 데이터 따로 저장  |
|         | 7 units  | P_S03 | 통합 데이터 중 GPS 위치들을 기반으로 계단 위치 지정(면적화) |
|         | 4 units  | P_S04 | P_S01~03에 대한 여러 sample 들을 중복시켜 특정 임계값을 넘는 면적 계산 |
|         | 4 units  | P_S05 | 무게중심 GPS 위치 계산 및 추가 정보 입력(계단 크기, 경사) |

- raw_data 기반으로 계단 위치 추정 결과
  - 위치 인식 훌륭
  - 계단 인식 훌륭
  - 계단 인식 시작 시간 훌륭
  - 계단 인식 끝 시간을 정하는 기준을 모르겠음
  
- 계단 위치 정확도를 높이기 위한 방법
  - isStair 정확도 -> Milestone 3
  - GPS 정확도 -> 이미 높음
  - 내려가는 계단도 인식하기
  - 낮으 계단이나 턱도 인식하기
  

### Milestone 3

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|         |           |    D_S01   |             |
|         |           |       |             |

- 딥러닝을 활용한 계단 위치 추정


### Milestone 4

| actual  | estimated | story | description |
| ------  | --------- | ----- | ----------- |
|         |           |       |             |
|         |           |       |             |

- Web 지도 상에 추정한 계단 위치 띄우기
- 계단을 피하는 경로 찾기 기능
