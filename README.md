# Projeto de Automação Web — Selenium + OpenCV (POM + PyTest)

Um projeto completo para praticar **automação de navegador com Selenium** usando o padrão **Page Object Model (POM)**,
testes com **PyTest**, esperas inteligentes, relatórios, e um módulo opcional de **visão computacional** (OpenCV + PyAutoGUI)
para clicar por imagem. Inclui ainda OCR com Tesseract.

## 🗂️ Estrutura
```
automacao-web/
 ┣ src/
 ┃ ┣ pages/
 ┃ ┣ tests/
 ┃ ┣ utils/
 ┃ ┣ config/
 ┣ reports/
 ┣ downloads/
 ┣ .env
 ┣ requirements.txt
 ┣ pytest.ini
 ┗ README.md
```

## ▶️ Como executar
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

# Smoke
pytest -m smoke

# E2E
pytest -m e2e

# Relatório HTML (também gerado via addopts)
pytest --html=reports/report.html --self-contained-html
```
> Dica: Ajuste as URLs e credenciais no arquivo `.env`.

## 🔧 Tecnologias
- Selenium 4, webdriver-manager
- PyTest + pytest-html
- python-dotenv para configurar via `.env`
- (Opcional) OpenCV + PyAutoGUI para clique por imagem
- (Opcional) OCR via pytesseract

## ✅ Checklist
- [ ] Configurar venv e instalar dependências
- [ ] Ajustar `.env` com URLs reais
- [ ] Mapear seletores das páginas
- [ ] Implementar validações no Dashboard
- [ ] Criar fluxo de relatório + download
- [ ] Adicionar screenshots em erros
- [ ] (Opcional) Clique por imagem com OpenCV
- [ ] (Opcional) OCR no arquivo baixado
- [ ] (Bônus) CI com GitHub Actions e Docker
