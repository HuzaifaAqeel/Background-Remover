# 🖼️ Background Remover

Remove image backgrounds in one click — a Streamlit app powered by `rembg`.

> **Attribution:** This project is based on [vluz/RemoveBackground](https://github.com/vluz/RemoveBackground) (CC0-1.0). I extended it with selectable model quality and cleaned up the dependencies.

## What it does

- 📤 Upload a PNG
- 🤖 Pick a model: **u2netp** (fast, 4.7MB, runs anywhere) or **u2net** (high quality, 176MB, needs more RAM)
- ✨ Get a transparent-background PNG back instantly

## What changed from the original

- Added a **model-quality selector** — the original always used the heavy `u2net` model, which can OOM small machines; now `u2netp` is the default
- Removed the unnecessary `torch` import (the ONNX runtime does the work)
- Cleaned up `requirements.txt`

## Quick start

```bash
pip install -r requirements.txt
streamlit run delbg.py
```

Upload a PNG, hit **Remove**, and download the result.

## License

CC0-1.0 — see [LICENSE](LICENSE) (original license by vluz, preserved).
