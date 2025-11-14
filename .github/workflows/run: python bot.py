name: Run Discord Bot

on:
  workflow_dispatch:   # تشغيل يدوي من Actions
  schedule:
    - cron: '*/30 * * * *'   # تشغيل كل 30 دقيقة

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run bot
        env:
          DISCORD_TOKEN: ${{ secrets.DISCORD_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python main.py
