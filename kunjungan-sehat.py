import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://situbondo.epuskesmas.id/")
    page.get_by_role("link", name="ePuskesmas").click()
    page.get_by_role("textbox", name="E-mail / No. HP / ID").fill("loket-pkm@test.go.id")
    page.get_by_role("textbox", name="E-mail / No. HP / ID").press("Tab")
    page.get_by_role("textbox", name="kata kunci").fill("1Sampai9_#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name=" PUSKESMAS SITUBONDO").click()
    page.get_by_role("button", name="Pendaftaran").click()
    page.get_by_role("link", name="Pasien & KK").click()
    page.get_by_role("textbox", name="Cari Nama").click()
    page.get_by_role("textbox", name="Cari Nama").fill("febby ridwan zaelani")
    page.get_by_role("button", name="Cari").click()
    page.get_by_role("cell").nth(3).click()
    page.get_by_role("cell", name="1", exact=True).click()
    page.get_by_role("cell", name="1", exact=True).click()
    page.get_by_role("link", name="Pendaftaran", exact=True).click()
    page.get_by_role("radio", name="KUNJUNGAN SEHAT").check()
    page.get_by_role("checkbox", name="Kondisi stabil").check()
    page.get_by_role("button", name=" Rawat Jalan").click()
    page.get_by_role("button", name="f  KONSELING").click()
    page.get_by_role("button", name="  dr. ANDINI KARTIKA SARI 0/").click()
    page.get_by_role("button", name="f   dr. RARAS SILVIA GAMA 0/").click()
    page.locator("#button_save").click()
    page.get_by_role("button", name="Pelayanan").click()
    page.get_by_role("link", name="Medis").click()
    page.locator("i").first.click()
    page.get_by_role("cell", name="23", exact=True).click()
    page.get_by_role("textbox", name="Pencarian").click()
    page.get_by_role("textbox", name="Pencarian").fill("febby ridwan zaelani")
    page.get_by_role("button", name="Cari").click()
    page.get_by_role("cell", name="1", exact=True).dblclick()
    page.get_by_role("button", name="Ok", exact=True).click()
    page.get_by_role("link", name="Anamnesa", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

