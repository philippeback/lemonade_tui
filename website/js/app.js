/**
 * Main Application Logic for Lemonade TUI Website
 * Handles CLI command builder, clipboard copying, and matrix filtering.
 */
document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy-to-clipboard functionality
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', async () => {
      const targetSelector = btn.getAttribute('data-target');
      let textToCopy = '';
      if (targetSelector) {
        const targetEl = document.querySelector(targetSelector);
        textToCopy = targetEl ? targetEl.textContent.trim() : '';
      } else {
        textToCopy = btn.getAttribute('data-clipboard-text') || '';
      }

      if (!textToCopy) return;

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalHtml = btn.innerHTML;
        btn.innerHTML = '✔ Copied!';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.innerHTML = originalHtml;
          btn.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Failed to copy: ', err);
      }
    });
  });

  // 2. Interactive CLI Command Builder
  const cbStatic = document.getElementById('opt-static');
  const cbDynamic = document.getElementById('opt-dynamic');
  const cbSnapshot = document.getElementById('opt-snapshot');
  const cbTask = document.getElementById('opt-task');
  const cbExport = document.getElementById('opt-export');
  const inputTask = document.getElementById('val-opt-task');
  const inputExport = document.getElementById('val-opt-export');
  const inputLog = document.getElementById('val-opt-log');
  const cmdDisplay = document.getElementById('cli-generated-cmd');

  function updateCommand() {
    if (!cmdDisplay) return;

    let parts = ['uv run python .\\lemonade_tui.py'];

    if (cbStatic && cbStatic.checked) {
      parts.push('--static');
    }
    if (cbDynamic && cbDynamic.checked) {
      parts.push('-w');
    }
    if (cbSnapshot && cbSnapshot.checked) {
      parts.push('--snapshot');
    }
    if (cbTask && cbTask.checked && inputTask) {
      parts.push(`--task ${inputTask.value.trim() || '5376'}`);
    }
    if (cbExport && cbExport.checked && inputExport) {
      parts.push(`--export ${inputExport.value.trim() || 'report.md'}`);
    }

    const logPath = inputLog ? inputLog.value.trim() : '';
    if (logPath) {
      parts.push(`"${logPath}"`);
    }

    cmdDisplay.textContent = parts.join(' ');
  }

  [cbStatic, cbDynamic, cbSnapshot, cbTask, cbExport].forEach(el => {
    el?.addEventListener('change', updateCommand);
  });

  [inputTask, inputExport, inputLog].forEach(el => {
    el?.addEventListener('input', updateCommand);
  });

  updateCommand();

  // 3. Matrix Search Filter
  const matrixSearch = document.getElementById('matrix-search-input');
  if (matrixSearch) {
    matrixSearch.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      document.querySelectorAll('#matrix-table-body tr').forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(q) ? '' : 'none';
      });
    });
  }
});
