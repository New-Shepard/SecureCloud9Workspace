# SecureCloud9Workspace

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
