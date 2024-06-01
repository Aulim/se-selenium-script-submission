const { Builder, By, Key, until } = require('selenium-webdriver');
const assert = require('assert');

(async function example() {
  let driver = await new Builder().forBrowser('chrome').build();
  try {
    await driver.get('https://your-website-testing-page.com');

    const pageTitle = await driver.getTitle();
    assert.strictEqual(pageTitle, 'Website Testing Page');

    const inputField = await driver.findElement(By.id('input-field'));
    await inputField.sendKeys('Test Input');
    const inputValue = await inputField.getAttribute('value');
    assert.strictEqual(inputValue, 'Test Input');

    const submitButton = await driver.findElement(By.id('submit-button'));
    await submitButton.click();
    const successMessage = await driver.findElement(By.id('success-message'));
    assert.ok(await successMessage.isDisplayed());
  } finally {
    await driver.quit();
  }
})();
