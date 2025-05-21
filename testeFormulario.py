import time
from playwright.sync_api import sync_playwright, Playwright


def teste_formulario(nome, sobrenome, idade, pais, notas):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Acessar a página
        page.goto("https://testpages.herokuapp.com/styled/validation/input-validation.html")
        time.sleep(1)

        # Preencher o formulário
        page.fill("#firstname", nome)
        time.sleep(1)

        page.fill("#surname", sobrenome)
        time.sleep(1)

        page.fill("#age", str(idade))
        time.sleep(1)

        page.select_option("#country", pais)
        time.sleep(1)

        page.fill("#notes", notas)
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

# Possiveis casos de teste
print("\nTestando caso Válido, sucesso na submissão do formulario...")
teste_formulario("Layla", "Rodrigues Alves", 18, "Brazil", "Teste automatizado")

# print("\nTestando caso Válido, com sobrenome vazio...")
# teste_formulario("Layssa", "", 21, "Brazil", "Teste automatizado")

print("\nTestando caso Inválido, com nome vazio e idade menor que 18...")
teste_formulario("", "Rodrigues Alves", 16, "Brazil", "Teste automatizado")

print("\nTestando caso Inválido, com primeiro nome curto...")
teste_formulario("Lay", "Rodrigues Alves", 18, "Brazil", "Teste automatizado")

print("\nTestando caso inválido, com sobrenome curto...")
teste_formulario("Layla", "Alves", 18, "Brazil", "Teste automatizado")

# print("\nTestando caso Inválido, com nome vazio...")
# teste_formulario("", "Rodrigues Alves", 18, "Brazil", "Teste Automatizado")

# print("\nTestando caso Inválido, idade maior que 80...")
# teste_formulario("Layla", "Rodrigues Alves", 81, "Brazil", "Teste automatizado")

# print("\nTestando caso Inválido, com idade menor de 18...")
# teste_formulario("Layla", "Rodrigues Alves", 17, "Brazil", "Teste automatizado")

