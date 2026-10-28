# azulene

OpenAI GPT API에 연결된 FastAPI 서버.

## 설정

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env        # 그다음 .env에 OPENAI_API_KEY 입력
```

## 실행

```bash
uvicorn app:app --reload
```

- `GET  /health` — 상태 확인
- `POST /chat` — GPT와 대화
- 문서: http://127.0.0.1:8000/docs

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"안녕!"}]}'
```

`.env`는 `.gitignore`에 포함되어 있어 커밋되지 않습니다.
