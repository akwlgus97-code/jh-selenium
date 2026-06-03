# KREAM Login QA Automation

KREAM 웹사이트의 개인 회원 일반 로그인 흐름을 Selenium으로 자동화한 QA 테스트 스크립트입니다.

## 테스트 시나리오

1. KREAM 홈페이지에 접속합니다.
2. 상단 로그인 링크를 클릭해 로그인 페이지로 이동합니다.
3. 이메일과 비밀번호 입력 영역이 활성화되는지 확인합니다.
4. 로그인 버튼을 클릭합니다.
5. 로그인 후 상단 메뉴가 `로그아웃` 상태로 변경되는지 확인합니다.

## 사용 기술

- Python
- Selenium WebDriver
- Chrome WebDriver
- WebDriverWait

## 주요 구현 내용

- Chrome 브라우저 실행 옵션을 `start_driver()` 함수로 분리했습니다.
- 반복되는 CSS selector 탐색을 `find_css()` 함수로 분리했습니다.
- 동적 로딩 대응을 위해 `WebDriverWait` 기반의 대기 함수를 사용했습니다.
- 테스트 종료 시 `finally`에서 `driver.quit()`을 실행해 브라우저 프로세스가 남지 않도록 처리했습니다.
- 로그인 성공 여부는 상단 메뉴의 `로그아웃` 텍스트 표시 여부로 검증합니다.

## 실행 방법

프로젝트 루트에서 아래 명령어를 실행합니다.

```bash
python login.py
```

가상환경을 사용하는 경우:

```bash
.venv/bin/python login.py
```

## 테스트 계정 안내

보안상 실제 로그인 계정 정보는 코드와 저장소에 포함하지 않았습니다.

현재 `login.py`의 이메일/비밀번호 입력값은 빈 문자열로 되어 있으므로, 실제 실행 검증이 필요한 경우 테스트 전용 계정 값을 별도로 입력해야 합니다.

```python
email_id.send_keys("")
pw.send_keys("")
```

실무 환경에서는 실제 계정 정보를 코드에 직접 작성하지 않고 환경변수나 별도 설정 파일로 분리하는 방식을 권장합니다.


