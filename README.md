# 소방서에서 가장 가까운 고등학교는 어디?

고등학교 프로젝트용 저장소입니다. 

전국의 119안전센터와 고등학교의 위도와 경도 차이로 거리를 계산해서 각 고등학교마다 가장 가까운 119안전센터 이름과 그 거리가 포함된 csv 파일을 저장합니다.

## 데이터 출처

- 전국 고등학교 목록 `schoolList_2020_04_hig.json`: 학교알리미
- 전국 119안전센터 목록 `119centers_with_ll.csv`: 공공데이터 포털 + 카카오맵 API

## 프로그램 설명

- `get_loc_kakao.py`: `119centers.csv`의 센터 이름을 읽어, 위도와 경도를 카카오맵 API로부터 가져옵니다. `119centers_with_ll.csv`로 출력합니다.
- `calculate.py`: 고등학교별로 가장 가까운 센터와 그 거리를 계산해 `schools_w_least.csv`로 저장합니다.

## 보고서

미흡한 보고서는 파일 목록 중 `소방서에서 가장 가까운 고등학교는?.pdf`으로 볼 수 있습니다. 수준미달의 급히 쓴 보고서입니다.

