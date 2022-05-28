## 풍월량에게 이런 댓글을

> 풍월량의 토토 이렇게 하면 역배 성공?!
> 
> Twitch에서 생방송 중인 종겜스 [풍월량](https://www.twitch.tv/hanryang1125?lang=ko)! 불완전 놀이터인 포인트 토토에서 '이것!' 말해주니 풍월량이 이긴다? 

트위치의 주요 채팅 기능 중 하나인 [채널 포인트 예측](https://help.twitch.tv/s/article/channel-points-predictions?language=ko)을 통해 트위치의 포인트로 토토를 할 수 있습니다. 이곳에서 스트리머가 승리하는 토토에는 어떤 채팅이 올라오는지, 실패하는 토토에는 어떤 채팅이 올라오는지 알아봅시다. 그리고 이 데이터들을 통해서 댓글로 풍월량의 승리를 기원해 봅시다.

 ## 프로젝트 설명
프로젝트는 구글 [코랩](https://colab.research.google.com/github/JangHanjun/Hanryang_Win_Formula/blob/main/PoongWinPercent.ipynb)을 사용해서 제작했습니다. 채팅 로그는 아래 추출 프로그램을 통해 직접 추출한 뒤 분류를 했으며 전부 [슈퍼 마리오 메이커 2](https://www.nintendo.co.kr/software/switch/baaqa/pc/) 플레이중 나온 채팅 로그들을 분석했습니다. 분석을 하면서 **ExtractChat**파일을 통해서 'ㄹㅇㅋㅋ', 'ㅗㅜㅑ'와 같이 많이 나오는 단어들은 1회 등장으로 제한을 했으며 'ㅋㅋㅋㅋㅋ...'와 같은 다수의 ㅋ 이 나오는것은 제거를 했습니다.



코랩에서 파일을 실행할 시 추가 데이터 로드 없이 깃허브, 구글 드라이브를 통해서 채팅 로그 csv 파일과 최고 정확도의 모델을 다운받을 수 있게 처리했습니다. 아직 실행파일을 빼는 법을 몰라 이렇게 진행되어 있는 점 안타깝게 되었습니다.



 ### 프로젝트 참여자

 - [Husk](https://github.com/JangHanjun) : 프로젝트 개설

 ### 사용 기술
 - NLP (with Python-Pytorch)

### 프로젝트 참고 자료 (+오픈소스)

https://wikidocs.net/44249 - 네이버 영화 리뷰 감성 추출기

Mecab - 형태소 분석기중 본 데이터에 정확도가 가장 높아 konlpy 에서 사용하게 되었습니다.

 ### 채팅 로그 추출
 학습용으로 사용하는 채팅 로그는 아래 공개 프로그램인 TwitchDownloader를 사용해서 다운로드 했습니다! txt 파일로 다운되는 채팅 로그를 채팅 정제, 라벨링을 통해서 훈련용 데이터로 사용할 예정입니다.
 - [lay295/TwitchDownloader](https://github.com/lay295/TwitchDownloader)

### 프로젝트 로그
- 2022.05.03 : 프로젝트 repo 개설
- 2022.05:09 : 트위치 포인트 토토 시스템 변경으로 인해 목표 변경
- 2022.05.28 : 해당 강의 최종 과제 제출
