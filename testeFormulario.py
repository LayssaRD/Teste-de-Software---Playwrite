import time
from playwright.sync_api import sync_playwright, Playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Acessar a página
    page.goto("https://testpages.herokuapp.com/styled/validation/input-validation.html")
    time.sleep(1)

    # Preencher o formulário
    page.fill("#firstname", "Lay")
    time.sleep(1)

    page.fill("#surname", "Rodrigues Alves")
    time.sleep(1)

    page.fill("#age", "18")
    time.sleep(1)

    page.select_option("#country", "United Kingdom")
    time.sleep(1)

    page.fill("#notes", "Teste automatizado")
    time.sleep(1)

    # Submeter o formulário
    page.click("input[type='submit']")
    time.sleep(2)

    # Esperar o carregamento da página de resposta
    page.wait_for_load_state("networkidle")
    time.sleep(2)

    # Verifica status de envio do formulário
    content = page.content()
    if "Valid Input" in content:
        print("Sucesso na submissão do formulário.")
    else:
        print("Falha ao enviar formulário.")
        print("Erro(s) detectado(s):")

        # Verifica erro de envio do formulário
        error_element = page.query_selector("ul")
        if error_element:
            error_text = error_element.inner_text()
            print(error_text)
        else:

            # Verifica erro do navegador no campo firstname
            firstname_input = page.query_selector("#firstname")
            if firstname_input:
                try:
                    is_valid = firstname_input.evaluate("el => el.checkValidity && el.checkValidity()")
                    if not is_valid:
                        validation_msg = firstname_input.evaluate("el => el.validationMessage")
                        print(f"Primeiro Nome: {validation_msg}")
                except Exception as e:
                    print(f"Erro ao verificar validade de firstname: {e}")
            else:
                print("Campo firstname não encontrado.")

            # Verifica erro do navegador no campo surname
            surname_error = page.query_selector("label[name='surnamevalidation']")
            if surname_error and surname_error.is_visible():
                error_text = surname_error.inner_text()
                print(f"Sobrenome: {error_text}")

            # Verifica erro do navegador no campo age
            age_input = page.query_selector("#age")
            if age_input:
                try:
                    is_valid = age_input.evaluate("el => el.checkValidity && el.checkValidity()")
                    if not is_valid:
                        validation_msg = age_input.evaluate("el => el.validationMessage")
                        print(f"Idade: {validation_msg}")
                except Exception as e:
                    print(f"Erro ao verificar validade de idade: {e}")
            else:
                print("Campo idade não encontrado.")

    # Fechar navegador
    browser.close()
