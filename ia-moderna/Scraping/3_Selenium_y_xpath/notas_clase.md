Selenium pro:
- Repaso Idea Selenium + Zoom

Ejercicio Twitter
Ejemplo Linkedin
Ejemplo Spotify, probar variacioens


XPATH en navegador:
  - probar xpath en navegador
  - copy XPATH

Selenium:
- cookies
- screenshot
- wait to be clickable
- actionchains
- chromedriver manager

- Intento Zoom
- By.xpath(
- switch window
- 2captcha
- proxies

import undetected_chromedriver as uc

NoSuchElementException
TimeoutException
ElementNotVisibleException
ElementNotSelectableException
ElementClickInterceptedException
ElementNotInteractableException


https://stackoverflow.com/questions/21335136/how-to-re-enable-right-click-so-that-i-can-inspect-html-elements-in-chrome

javascript:function enableContextMenu(aggressive = true) { void(document.ondragstart=null); void(document.onselectstart=null); void(document.onclick=null); void(document.onmousedown=null); void(document.onmouseup=null); void(document.body.oncontextmenu=null); enableRightClickLight(document); if (aggressive) { enableRightClick(document); removeContextMenuOnAll('body'); removeContextMenuOnAll('img'); removeContextMenuOnAll('td'); } } function removeContextMenuOnAll(tagName) { var elements = document.getElementsByTagName(tagName); for (var i = 0; i < elements.length; i++) { enableRightClick(elements[i]); enablePointerEvents(elements[i]); } } function enableRightClickLight(el) { el || (el = document); el.addEventListener('contextmenu', bringBackDefault, true); } function enableRightClick(el) { el || (el = document); el.addEventListener('contextmenu', bringBackDefault, true); el.addEventListener('dragstart', bringBackDefault, true); el.addEventListener('selectstart', bringBackDefault, true); el.addEventListener('click', bringBackDefault, true); el.addEventListener('mousedown', bringBackDefault, true); el.addEventListener('mouseup', bringBackDefault, true); } function restoreRightClick(el) { el || (el = document); el.removeEventListener('contextmenu', bringBackDefault, true); el.removeEventListener('dragstart', bringBackDefault, true); el.removeEventListener('selectstart', bringBackDefault, true); el.removeEventListener('click', bringBackDefault, true); el.removeEventListener('mousedown', bringBackDefault, true); el.removeEventListener('mouseup', bringBackDefault, true); } function bringBackDefault(event) { event.returnValue = true; (typeof event.stopPropagation === 'function') && event.stopPropagation(); (typeof event.cancelBubble === 'function') && event.cancelBubble(); } function enablePointerEvents(el) {  if (!el) return; el.style.pointerEvents='auto'; el.style.webkitTouchCallout='default'; el.style.webkitUserSelect='auto'; el.style.MozUserSelect='auto'; el.style.msUserSelect='auto'; el.style.userSelect='auto'; enablePointerEvents(el.parentElement); } enableContextMenu();
