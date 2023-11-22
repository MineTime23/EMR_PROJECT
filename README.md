# EMR_Project
2023 09~12

## 환경 설정 및 시작

1. **프로젝트 클론:**
    ```bash
    git clone https://github.com/MineTime23/EMR_Project.git
    ```

2. **가상 환경 만들기 및 활성화:**
    ```bash
    cd CSE3010-EMR
    python -m venv venv
    .\venv\Scripts\activate  # 윈도우에서는 이 명령어를 사용합니다.
    ```

3. **의존성 패키지 설치:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Node.js 설치:**
    [Node.js 다운로드](https://nodejs.org/en/)에서 LTS 버전을 다운로드하여 설치합니다.

5. **Node.js 환경변수 추가:**
    시스템 환경변수에서 `C:\Program Files\nodejs\` 경로를 `PATH`에 추가합니다.

***다른 CMD 창을 열고***

6. **npm 패키지 설치 및 빌드:**
    ```bash
    cd your_project_directory  # package.json 파일이 있는 디렉토리로 이동
    npm install
    npm run build
    ```

7. **Vue.js 개발 서버 실행:**
    ```bash
    npm run serve
    ```

8. **Django 서버 실행:**
    ```bash
    python manage.py runserver
    ```

9. **PyCharm 등에서 Node.js Interpreter 설정:**
    PyCharm에서 프로젝트를 열어서 Settings 또는 Preferences로 이동하여, Project: your_project_name -> Python Interpreter에서 `Node.js`의 경로를 추가해줍니다.

10. **만일 8080 포트를 기존에 사용하고 있다면 검색 후 제거**
