/**
 * Interactive Textual TUI Engine Simulator for Lemonade TUI Website
 * Implements keyboard shortcuts, state machine, and fixed-width layout stabilization.
 */
(function () {
  const TASK_ID_WIDTH = 6;
  const datasets = window.LEMONADE_DATASETS;

  let currentIdx = 0;
  let activeTab = 1;
  let isDynamic = true;
  let pollerInterval = null;

  function padTaskId(id, width = TASK_ID_WIDTH) {
    const s = String(id);
    return s.padEnd(width, ' ');
  }

  function formatIndexCounter(curr, total) {
    const currStr = String(curr + 1).padStart(2, ' ');
    return `[${currStr}/${total}]`;
  }

  function renderClock() {
    const now = new Date();
    const clockEl = document.getElementById('sim-clock');
    if (clockEl) {
      clockEl.textContent = now.toTimeString().split(' ')[0];
    }
  }

  function renderTask() {
    const t = datasets[currentIdx];
    if (!t) return;

    // 1. Task Bar updates
    const idEl = document.getElementById('sim-task-id');
    const statusEl = document.getElementById('sim-task-status');
    const counterEl = document.getElementById('sim-counter');

    if (idEl) idEl.textContent = `Task #${padTaskId(t.taskId)}`;
    if (statusEl) {
      statusEl.textContent = t.statusText;
      statusEl.className = `tui-task-status-badge ${t.statusClass}`;
    }
    if (counterEl) {
      counterEl.textContent = formatIndexCounter(currentIdx, datasets.length);
    }

    // 2. Dynamic mode toggle button
    const modeBtn = document.getElementById('sim-btn-dynamic');
    if (modeBtn) {
      if (isDynamic) {
        modeBtn.textContent = '● Dynamic [d]';
        modeBtn.className = 'tui-btn tui-btn-mode';
      } else {
        modeBtn.textContent = '⏸ Static  [d]';
        modeBtn.className = 'tui-btn tui-btn-mode static';
      }
    }

    // 3. KPI Ribbon HUD Cards
    const valTask = document.getElementById('sim-val-task');
    const valDecode = document.getElementById('sim-val-decode');
    const valPrefill = document.getElementById('sim-val-prefill');
    const valTokens = document.getElementById('sim-val-tokens');
    const valMtp = document.getElementById('sim-val-mtp');
    const valGraph = document.getElementById('sim-val-graph');

    if (valTask) {
      const tag = t.isStreaming ? ' ●' : (t.status === 'ABORTED' ? ' ✖' : '');
      valTask.textContent = `#${padTaskId(t.taskId, 4)} (Slot ${t.slotId})${tag}`;
      valTask.className = `tui-kpi-val ${t.status === 'ABORTED' ? 'red' : 'green'}`;
    }

    if (valDecode) {
      if (t.decodeTps > 0) {
        valDecode.textContent = `${t.decodeTps.toFixed(1)} t/s (${t.msPerToken.toFixed(1)}ms)`;
        valDecode.className = 'tui-kpi-val';
      } else {
        valDecode.textContent = t.status === 'ABORTED' ? 'Aborted' : 'N/A';
        valDecode.className = 'tui-kpi-val red';
      }
    }

    if (valPrefill) {
      if (t.prefillTps > 0) {
        valPrefill.textContent = `${Math.round(t.prefillTps)} t/s (${t.ttftSec.toFixed(1)}s)`;
        valPrefill.className = 'tui-kpi-val orange';
      } else {
        valPrefill.textContent = 'N/A';
        valPrefill.className = 'tui-kpi-val red';
      }
    }

    if (valTokens) {
      const star = t.isStreaming ? '*' : '';
      const pIn = String(t.promptTokens).padStart(5, ' ');
      const gOut = String(t.genTokens + star).padStart(5, ' ');
      valTokens.textContent = `In:${pIn} / Out:${gOut}`;
    }

    if (valMtp) {
      if (t.draftAcceptance > 0) {
        valMtp.textContent = `${t.draftAcceptance.toFixed(1)}% (len ${t.draftMeanLen.toFixed(2)})`;
        valMtp.className = 'tui-kpi-val green';
      } else {
        valMtp.textContent = 'N/A';
        valMtp.className = 'tui-kpi-val';
      }
    }

    if (valGraph) {
      valGraph.textContent = `${t.graphsReused.toLocaleString()} hits`;
      valGraph.className = 'tui-kpi-val';
    }

    // 4. Update Tab Contents
    renderTabContent(t);

    // 5. Update table row selection in Tab 1
    const rows = document.querySelectorAll('#sim-task-rows tr');
    rows.forEach((row, i) => {
      if (i === currentIdx) {
        row.classList.add('selected');
      } else {
        row.classList.remove('selected');
      }
    });
  }

  function renderTabContent(t) {
    // Tab 1: Overview timeline
    const qW = Math.max(2, Math.min(10, (t.queueDelaySec / 25) * 100));
    const pW = Math.max(15, Math.min(45, (t.prefillSec / 25) * 100));
    const dW = Math.max(20, 100 - qW - pW);

    const barQ = document.getElementById('sim-bar-q');
    const barP = document.getElementById('sim-bar-p');
    const barD = document.getElementById('sim-bar-d');

    if (barQ) {
      barQ.style.width = `${qW}%`;
      barQ.textContent = `Queue: ${t.queueDelaySec.toFixed(2)}s`;
    }
    if (barP) {
      barP.style.width = `${pW}%`;
      barP.textContent = `Prefill: ${t.prefillSec.toFixed(1)}s (${t.prefillTps.toFixed(0)} t/s)`;
    }
    if (barD) {
      barD.style.width = `${dW}%`;
      barD.textContent = `Decode: ${t.decodeSec.toFixed(1)}s (${t.decodeTps.toFixed(0)} t/s)`;
    }

    // Tab 3: Tokens
    const tokPromptEl = document.getElementById('sim-tok-prompt');
    const tokGenEl = document.getElementById('sim-tok-gen');
    const tokAcceptEl = document.getElementById('sim-tok-accept');
    const tokSpeedupEl = document.getElementById('sim-tok-speedup');

    if (tokPromptEl) tokPromptEl.textContent = `${t.promptTokens.toLocaleString()} tokens`;
    if (tokGenEl) tokGenEl.textContent = `${t.genTokens.toLocaleString()} tokens`;
    if (tokAcceptEl) tokAcceptEl.textContent = `${t.draftAcceptance.toFixed(1)}%`;
    if (tokSpeedupEl) tokSpeedupEl.textContent = `~${t.draftMeanLen.toFixed(1)}x Speedup`;

    // Tab 4: Context
    const ctxTokensEl = document.getElementById('sim-ctx-tokens');
    const ctxGraphsEl = document.getElementById('sim-ctx-graphs');
    const ctxQueueEl = document.getElementById('sim-ctx-queue');

    if (ctxTokensEl) ctxTokensEl.textContent = `${t.retainedTokens.toLocaleString()} tokens`;
    if (ctxGraphsEl) ctxGraphsEl.textContent = `${t.graphsReused.toLocaleString()} hits`;
    if (ctxQueueEl) ctxQueueEl.textContent = `${t.queueDelaySec.toFixed(3)}s`;

    // Tab 6: Raw log
    const rawEl = document.getElementById('sim-raw-log');
    if (rawEl) rawEl.textContent = t.rawLog;
  }

  function switchTab(tabNum) {
    activeTab = tabNum;
    document.querySelectorAll('.tui-tab-btn').forEach(btn => {
      btn.classList.toggle('active', parseInt(btn.dataset.tab, 10) === tabNum);
    });
    document.querySelectorAll('.tui-pane').forEach(pane => {
      pane.classList.toggle('active', parseInt(pane.dataset.tab, 10) === tabNum);
    });
  }

  function nextTask() {
    currentIdx = (currentIdx + 1) % datasets.length;
    renderTask();
  }

  function prevTask() {
    currentIdx = (currentIdx - 1 + datasets.length) % datasets.length;
    renderTask();
  }

  function firstTask() {
    currentIdx = 0;
    renderTask();
  }

  function lastTask() {
    currentIdx = datasets.length - 1;
    renderTask();
  }

  function toggleDynamic() {
    isDynamic = !isDynamic;
    renderTask();
  }

  function openJumpModal() {
    const modal = document.getElementById('sim-jump-modal');
    const input = document.getElementById('sim-jump-input');
    if (modal && input) {
      modal.classList.add('active');
      input.value = '';
      input.focus();
    }
  }

  function closeJumpModal() {
    const modal = document.getElementById('sim-jump-modal');
    if (modal) modal.classList.remove('active');
  }

  function applyJump() {
    const input = document.getElementById('sim-jump-input');
    if (!input) return;
    const targetId = parseInt(input.value.trim(), 10);
    const foundIdx = datasets.findIndex(x => x.taskId === targetId);
    if (foundIdx !== -1) {
      currentIdx = foundIdx;
      renderTask();
    }
    closeJumpModal();
  }

  function startDynamicPoller() {
    if (pollerInterval) clearInterval(pollerInterval);
    pollerInterval = setInterval(() => {
      if (!isDynamic) return;
      const inFlightTask = datasets.find(x => x.isStreaming);
      if (inFlightTask) {
        inFlightTask.genTokens += Math.floor(Math.random() * 3) + 2;
        inFlightTask.decodeTps = 58.0 + (Math.random() * 2 - 1);
        if (datasets[currentIdx].taskId === inFlightTask.taskId) {
          renderTask();
        }
      }
    }, 1500);
  }

  // Keyboard navigation
  window.addEventListener('keydown', function (e) {
    // Only capture if simulator or body is active and not typing in modal
    const modal = document.getElementById('sim-jump-modal');
    const isModalOpen = modal && modal.classList.contains('active');

    if (isModalOpen) {
      if (e.key === 'Escape') {
        closeJumpModal();
      } else if (e.key === 'Enter') {
        applyJump();
      }
      return;
    }

    if (document.activeElement && ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      return;
    }

    switch (e.key.toLowerCase()) {
      case 't':
        e.preventDefault();
        nextTask();
        break;
      case 'p':
        e.preventDefault();
        prevTask();
        break;
      case 'd':
        e.preventDefault();
        toggleDynamic();
        break;
      case 'g':
        e.preventDefault();
        openJumpModal();
        break;
      case 'r':
        e.preventDefault();
        renderTask();
        break;
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
        e.preventDefault();
        switchTab(parseInt(e.key, 10));
        break;
    }
  });

  // Wire UI Buttons
  document.addEventListener('DOMContentLoaded', () => {
    setInterval(renderClock, 1000);
    renderClock();

    // Nav controls
    document.getElementById('sim-btn-first')?.addEventListener('click', firstTask);
    document.getElementById('sim-btn-prev')?.addEventListener('click', prevTask);
    document.getElementById('sim-btn-next')?.addEventListener('click', nextTask);
    document.getElementById('sim-btn-end')?.addEventListener('click', lastTask);
    document.getElementById('sim-btn-goto')?.addEventListener('click', openJumpModal);
    document.getElementById('sim-btn-dynamic')?.addEventListener('click', toggleDynamic);

    // Modal controls
    document.getElementById('sim-modal-submit')?.addEventListener('click', applyJump);
    document.getElementById('sim-modal-cancel')?.addEventListener('click', closeJumpModal);

    // Tab buttons
    document.querySelectorAll('.tui-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        switchTab(parseInt(btn.dataset.tab, 10));
      });
    });

    // Overview Table rows click
    document.querySelectorAll('#sim-task-rows tr').forEach((tr, i) => {
      tr.addEventListener('click', () => {
        currentIdx = i;
        renderTask();
      });
    });

    renderTask();
    startDynamicPoller();
  });
})();
