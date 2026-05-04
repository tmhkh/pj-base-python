import { test, expect } from '@playwright/test';

test.describe('Echo Feature', () => {
  test('should successfully send a message and receive an echo', async ({ page }) => {
    // 1. トップページにアクセス
    await page.goto('/');

    // 2. タイトルの確認
    await expect(page.locator('h1')).toHaveText('PJ-base');

    // 3. フォームにメッセージを入力 ("Message" というプレースホルダを持つテキストボックス)
    const input = page.getByPlaceholder('Type your message here');
    await input.fill('Hello from Playwright Automated Test!');

    // 4. 送信ボタンをクリック ("Send to API" というボタン)
    const sendButton = page.getByRole('button', { name: 'Send to API' });
    await sendButton.click();

    // 5. エコーされたメッセージが画面に表示されるか検証
    const resultMessage = page.getByText('Echo: Hello from Playwright Automated Test!');
    await expect(resultMessage).toBeVisible();
  });
});
