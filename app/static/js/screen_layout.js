(() => {
  const stage = document.createElement('div');
  stage.className = 'screen-stage';
  const content = document.createElement('div');
  content.className = 'screen-content';
  for (const element of [...document.body.children]) {
    if (element.matches('script, .game-ambience, .motion-toggle, .instructions-trigger, .result-popup, .error-popup, .countdown-track')) continue;
    content.append(element);
  }
  stage.append(content);
  document.body.append(stage);
  document.body.classList.add('screen-fit');
  const guidePages = [...document.querySelectorAll('.instructions-steps')].map(guide => {
    const steps = [...guide.children];
    if (steps.length < 2) return null;
    let index = 0;
    const controls = document.createElement('nav');
    controls.className = 'page-controls';
    controls.setAttribute('aria-label', 'Instruction pages');
    const back = document.createElement('button');
    const next = document.createElement('button');
    const count = document.createElement('span');
    back.type = next.type = 'button';
    back.textContent = '← BACK';
    next.textContent = 'NEXT →';
    controls.append(back, count, next);
    guide.after(controls);
    function render() {
      const paged = window.innerHeight < 500;
      steps.forEach((step, page) => { step.hidden = paged && page !== index; });
      controls.hidden = !paged;
      count.textContent = `${index + 1} / ${steps.length}`;
      back.disabled = index === 0;
      next.disabled = index === steps.length - 1;
    }
    back.addEventListener('click', () => { index--; render(); });
    next.addEventListener('click', () => { index++; render(); });
    render();
    return render;
  }).filter(Boolean);
  let scheduled = false;
  function fit() {
    scheduled = false;
    const stageStyle = getComputedStyle(stage);
    const viewportHeight = window.visualViewport?.height || window.innerHeight;
    const stageHeight = Math.max(1, viewportHeight - parseFloat(stageStyle.top) - (document.body.classList.contains('landing-page') ? 12 : 58));
    if (stage.style.height !== `${stageHeight}px`) stage.style.height = `${stageHeight}px`;
    const available = stage.clientHeight;
    const height = content.scrollHeight;
    const scale = Math.min(1, available / Math.max(1, height));
    content.style.transform = `translateX(-50%) scale(${scale})`;
    content.style.top = `${Math.max(0, (available - height * scale) / 2)}px`;
    content.dataset.scale = scale.toFixed(3);
    document.querySelectorAll('.result-popup:not(.hidden), .error-popup:not(.hidden)').forEach(popup => {
      const box = popup.querySelector('.result-box, .error-box');
      if (!box) return;
      const ratio = Math.min(1, (popup.clientHeight - 24) / Math.max(1, box.scrollHeight));
      box.style.transform = `scale(${ratio})`;
    });
  }
  function scheduleFit() {
    if (!scheduled) { scheduled = true; requestAnimationFrame(fit); }
  }
  new ResizeObserver(scheduleFit).observe(content);
  new ResizeObserver(scheduleFit).observe(stage);
  new MutationObserver(scheduleFit).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ['class', 'hidden'] });
  document.fonts.ready.then(scheduleFit);
  document.addEventListener('load', scheduleFit, true);
  window.visualViewport?.addEventListener('resize', scheduleFit);
  window.addEventListener('resize', () => { guidePages.forEach(render => render()); scheduleFit(); });
  fit();
})();
