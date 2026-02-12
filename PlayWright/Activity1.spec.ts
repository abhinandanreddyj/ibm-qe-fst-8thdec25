import { test, expect } from "@playwright/test";

test("Activity 1 - Navigate to About Page", async ({ page }) => {

  // Increase timeout for slow website
  test.setTimeout(60000);

  // Step 1: Go to homepage
  await page.goto("https://training-support.net", {
    waitUntil: "domcontentloaded"
  });

  // Step 2: Verify homepage loaded
  await expect(page).toHaveURL(/training-support/);

  // Step 3: Click on About link (stable locator)
  await page.locator('a[href*="about"]').first().click();

  // Step 4: Verify URL contains /about
  await expect(page).toHaveURL(/about/);

  // Step 5: Verify heading is visible
  await expect(page.locator("h1")).toBeVisible();

  // Optional: Validate heading text (more strong validation)
  const headingText = await page.locator("h1").textContent();
  console.log("Heading Text:", headingText);

});
