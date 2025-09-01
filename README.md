# Projeto de Automação Web -- Selenium + OpenCV (POM + PyTest)

Um projeto completo para praticar **automação de navegador com
Selenium** usando o padrão **Page Object Model (POM)**, testes com
**PyTest**, esperas inteligentes, relatórios, e um módulo opcional de
**visão computacional** (OpenCV + PyAutoGUI) para clicar por imagem.
Inclui ainda OCR com Tesseract.

------------------------------------------------------------------------

## 🎯 Objetivo do projeto

1.  Acessar um site de demonstração (login) e autenticar.
2.  Navegar até área logada, gerar relatório e baixar arquivo.
3.  Validar o resultado (texto ou arquivo).
4.  (Opcional) Usar visão computacional para localizar/clicar por
    imagem.
5.  (Opcional) Usar OCR para validar conteúdo de PDF/imagem.

------------------------------------------------------------------------

## 🗂️ Estrutura de pastas

    automacao-web/
     ┣ 📂 src/
     ┃ ┣ 📂 pages/
     ┃ ┣ 📂 tests/
     ┃ ┣ 📂 utils/
     ┃ ┣ 📂 config/
     ┣ 📂 reports/
     ┣ 📂 downloads/
     ┣ .env
     ┣ requirements.txt
     ┣ pytest.ini
     ┗ README.md

------------------------------------------------------------------------

## 📦 requirements.txt

    selenium==4.23.1
    webdriver-manager==4.0.2
    pytest==8.3.2
    pytest-html==4.1.1
    python-dotenv==1.0.1
    pyautogui==0.9.54
    opencv-python==4.10.0.84
    pytesseract==0.3.13

------------------------------------------------------------------------

## ⚙️ pytest.ini

    [pytest]
    addopts = -q --html=reports/report.html --self-contained-html
    pythonpath = src
    markers =
        smoke: smoke tests (rápidos)
        e2e: end-to-end tests (fluxos completos)

------------------------------------------------------------------------

## 🔐 .env (exemplo)

    BASE_URL=https://exemplo.com
    LOGIN_URL=https://exemplo.com/login
    USER_EMAIL=usuario@teste.com
    USER_PASSWORD=senha123
    DOWNLOAD_DIR=downloads
    HEADLESS=true
    TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

------------------------------------------------------------------------

## ▶️ Executando

``` bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.\.venv\Scripts\Activate.ps1  # Windows

pip install -r requirements.txt

pytest -m smoke
pytest -m e2e
```

Gerar relatório HTML:

``` bash
pytest --html=reports/report.html --self-contained-html
```

------------------------------------------------------------------------

## ✅ Checklist

-   [ ] Configurar venv e instalar dependências
-   [ ] Ajustar `.env` com URLs reais
-   [ ] Mapear seletores das páginas
-   [ ] Implementar validações no Dashboard
-   [ ] Criar fluxo de relatório + download
-   [ ] Adicionar screenshots em erros
-   [ ] (Opcional) Clique por imagem com OpenCV
-   [ ] (Opcional) OCR no arquivo baixado
-   [ ] (Bônus) CI com GitHub Actions e Docker

------------------------------------------------------------------------

## 🧠 Boas práticas

-   Use **Page Object Model (POM)**: seletores ficam nas classes de
    página, não nos testes.
-   Prefira **esperas explícitas** ao invés de `time.sleep`.
-   Centralize configurações em `.env` e `settings.py`.
-   Cada teste deve rodar de forma **isolada**.

------------------------------------------------------------------------

## 📘 Licença

Projeto para fins educacionais. Pode ser usado e adaptado livremente.