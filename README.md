# SecureCloud9Workspace

## Well-Architected Scenario

### Security(보안) Scenario
허가되지 않은 접근 시도에 대한 차단 및 로깅
| 시나리오 항목 | 내용 |
|----|----|
|Source(자극원)                 |SSM요청을 위한 권한이 부여되지 않은 IAM user|
|Stimulus(자극)                 |SSM API 요청 ['[StartSession](https://docs.aws.amazon.com/ko_kr/systems-manager/latest/APIReference/API_StartSession.html)', '[SendCommand](https://docs.aws.amazon.com/ko_kr/systems-manager/latest/APIReference/API_SendCommand.html)']|
|Artifact(대상)                 |SecureCloud9Workspace를 이용해서 배포된 Cloud9 자원들|
|Environment(환경)              |정상적인 운영 상황|
|Response(반응)                 |요청이 거부되며 시도를 로깅|
|Response Measure(반응 측정)    |보안 리포트 생성|

## 배포 가이드

1. 사전 준비

AWS CLI 및 Nodejs 환경이 설치되어 있어야 합니다.
- AWS CLI 설치: https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-install.html
- Nodejs 설치: https://nodejs.org/ko/download/

2. CDK
npm 을 사용해서 CDK 설치
```bash
npm install -g aws-cdk
cdk --version
```

3. Python Virtual Environment 구성 및 의존성 패키지 설치
```bash
python -m venv .venv

# linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate.bat

pip install --upgrade pip && pip install -r requirements.txt
```

4. aws credential 설정
```bash
aws configure
```
5. CDK 프로젝트 배포
```bash
cdk synth
cdk deploy
```

6. SSM plugin 설치
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html

7. 포트포워딩 터널링
```bash
aws ssm start-session --target {instance-id} --document-name AWS-StartPortForwardingSession --parameters "portNumber=22, localPortNumber=4022"
```
